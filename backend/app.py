from flask import Flask, request, jsonify, send_file, make_response
from flask_cors import CORS
import os
import uuid
import threading
from llm_service import LlamaGenerator
from manim_service import ManimRenderer

app = Flask(__name__)

# Enhanced CORS configuration to handle preflight requests and 403 errors
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000", "http://127.0.0.1:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization", "X-Requested-With", "Accept"],
        "supports_credentials": True
    }
})

# Configure Flask settings
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# Add explicit OPTIONS handler for preflight requests
@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return response

# Initialize services
llama_generator = LlamaGenerator()
manim_renderer = ManimRenderer()

# Storage for job status
job_status = {}

# Debug endpoint to test connection
@app.route('/api/debug', methods=['GET', 'POST', 'OPTIONS'])
def debug_endpoint():
    return jsonify({
        'method': request.method,
        'headers': dict(request.headers),
        'status': 'Flask backend is accessible',
        'message': 'Connection successful!'
    })

@app.route('/api/generate', methods=['POST', 'OPTIONS'])
def generate_animation():
    if request.method == 'OPTIONS':
        return make_response('', 200)
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        user_input = data.get('description', '')
        
        if not user_input.strip():
            return jsonify({'error': 'Description is required'}), 400
        
        # Generate unique job ID
        job_id = str(uuid.uuid4())
        job_status[job_id] = {'status': 'processing', 'progress': 0}
        
        # Start background processing
        thread = threading.Thread(
            target=process_animation,
            args=(job_id, user_input)
        )
        thread.daemon = True  # Make thread daemon so it closes with main program
        thread.start()
        
        return jsonify({'job_id': job_id, 'status': 'started'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/status/<job_id>', methods=['GET', 'OPTIONS'])
def get_status(job_id):
    if request.method == 'OPTIONS':
        return make_response('', 200)
        
    if job_id in job_status:
        return jsonify(job_status[job_id])
    return jsonify({'error': 'Job not found'}), 404

@app.route('/api/video/<job_id>', methods=['GET', 'OPTIONS'])
def get_video(job_id):
    if request.method == 'OPTIONS':
        return make_response('', 200)
        
    video_path = f"../animations/videos/{job_id}.mp4"
    if os.path.exists(video_path):
        return send_file(video_path, as_attachment=True, mimetype='video/mp4')
    return jsonify({'error': 'Video not found'}), 404

def process_animation(job_id, user_input):
    try:
        # Update status
        job_status[job_id]['progress'] = 25
        job_status[job_id]['message'] = 'Generating code with Llama 3.2...'
        
        # Generate Manim code using Llama 3.2
        manim_code = llama_generator.generate_code(user_input)
        
        job_status[job_id]['progress'] = 50
        job_status[job_id]['code'] = manim_code
        job_status[job_id]['message'] = 'Rendering animation with Manim...'
        
        # Render animation
        video_path = manim_renderer.render(job_id, manim_code)
        
        job_status[job_id]['progress'] = 100
        job_status[job_id]['status'] = 'completed'
        job_status[job_id]['video_path'] = video_path
        job_status[job_id]['message'] = 'Animation ready!'
        
    except Exception as e:
        job_status[job_id]['status'] = 'error'
        job_status[job_id]['error'] = str(e)
        print(f"Animation processing error: {str(e)}")  # Debug logging

if __name__ == '__main__':
    # Ensure animations directory exists
    os.makedirs("../animations/videos", exist_ok=True)
    os.makedirs("../animations/scenes", exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
