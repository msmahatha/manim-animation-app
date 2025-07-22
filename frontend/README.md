# 🎬 AI-Powered Manim Animation Generator

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![React](https://img.shields.io/badge/React-18.0+-61DAFB.svg)](https://reactjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-4.9+-3178C6.svg)](https://typescriptlang.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-000000.svg)](https://flask.palletsprojects.com)
[![Manim](https://img.shields.io/badge/Manim-0.17+-FF6B35.svg)](https://manim.community)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Create stunning 2D mathematical animations using natural language descriptions powered by Llama 3.2 and Manim**

Transform your ideas into beautiful mathematical animations with the power of AI! Simply describe what you want to animate, and watch as Llama 3.2 generates Manim code that brings your vision to life.

## ✨ Features

- 🤖 **AI-Powered Code Generation**: Uses Llama 3.2 locally to generate Manim code
- 🎨 **2D Mathematical Animations**: Create complex mathematical visualizations
- 🌐 **Modern Web Interface**: Clean React + TypeScript frontend
- ⚡ **Real-time Progress Tracking**: Watch your animation render in real-time
- 🎥 **Instant Video Generation**: Download your animations immediately
- 🔒 **Privacy-First**: All processing happens locally on your machine
- 💰 **Cost-Free**: No API calls, no subscriptions, completely free to use

## 🎥 Demo

![Animation Generator Demo](https://via.placeholder.com/800x400?text=Demo+GIF+Here)

*Example: "A red circle moving from left to right" → Generated Manim code → Beautiful animation*

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** with pip
- **Node.js 16+** with npm
- **FFmpeg** (for video rendering)
- **Ollama** with Llama 3.2 model

### 1. Clone the Repository

git clone https://github.com/msmahatha/manim-animation-app.git
cd manim-animation-app



### 2. Setup Ollama + Llama 3.2

Install Ollama (visit ollama.com for your OS)
curl -fsSL https://ollama.com/install.sh | sh

Download Llama 3.2 model
ollama pull llama3.2:latest

Test the model
ollama run llama3.2:latest "Hello, can you generate Python code?"


### 3. Setup Backend

cd backend

Create virtual environment
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt



### 4. Setup Frontend

cd ../frontend

Install dependencies
npm install



### 5. Run the Application

**Terminal 1 - Start Backend:**

cd backend
source venv/bin/activate
python app.py


**Terminal 2 - Start Frontend:**

cd frontend
npm start


🎉 **Open your browser to `http://localhost:3000` and start creating animations!**

## 💡 Example Animations

Try these example descriptions to get started:

| Description | Result |
|-------------|--------|
| `"A red circle moving from left to right"` | Simple object movement |
| `"Text saying 'Hello Manim' appearing with fade in effect"` | Text animations |
| `"A blue square transforming into a green circle"` | Shape transformations |
| `"Graph of y = x² with a moving point"` | Mathematical plots |
| `"Two vectors being added geometrically"` | Vector mathematics |

## 🏗️ Architecture
manim-animation-app/
├── backend/ # Flask API server
│ ├── app.py # Main Flask application
│ ├── llm_service.py # Llama 3.2 integration
│ ├── manim_service.py # Manim rendering service
│ └── requirements.txt # Python dependencies
├── frontend/ # React application
│ ├── src/
│ │ ├── components/ # React components
│ │ ├── App.tsx # Main app component
│ │ └── App.css # Styling
│ └── package.json # Node.js dependencies
└── animations/ # Generated content
├── scenes/ # Generated Manim code
└── videos/ # Rendered animations



## 🛠️ Configuration

### Backend Configuration

Create `backend/.env` for custom settings:
FLASK_DEBUG=True
OLLAMA_MODEL=llama3.2:latest
MAX_CONTENT_LENGTH=16777216
ANIMATION_TIMEOUT=300


### Frontend Configuration

The frontend uses a proxy configuration in `package.json`:

{
"proxy": "http://localhost:5000"
}


## 📚 API Documentation

### Generate Animation

POST /api/generate
Content-Type: application/json

{
"description": "A red circle moving from left to right"
}


### Check Status


## 🐛 Troubleshooting

### Common Issues

**Port 5000 already in use (macOS):**


Disable AirPlay Receiver in System Preferences
Or kill the process:
sudo kill -9 $(lsof -ti:5000)


**Connection errors:**
- Ensure both frontend and backend are running
- Check that Ollama service is active: `ollama list`
- Verify proxy configuration in `frontend/package.json`

**Manim rendering errors:**
- Check FFmpeg installation: `ffmpeg -version`
- Ensure sufficient disk space for video generation
- Verify Python virtual environment is activated

### Performance Tips

- **GPU Acceleration**: Use CUDA-compatible GPU for faster Llama 3.2 inference
- **Model Size**: Use `llama3.2:3b` for faster generation, `llama3.2:8b` for better quality
- **Video Quality**: Adjust Manim quality settings in `manim_service.py`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Manim Community](https://manim.community) - For the amazing animation library
- [Ollama](https://ollama.com) - For making LLM deployment simple
- [Meta](https://ai.meta.com) - For the Llama 3.2 model
- [React](https://reactjs.org) & [Flask](https://flask.palletsprojects.com) communities

## 📈 Roadmap

- [ ] 3D animation support
- [ ] Animation templates library
- [ ] Batch animation processing
- [ ] Custom Manim themes
- [ ] Animation sharing platform
- [ ] Mobile responsive design
- [ ] Docker containerization

---

<div align="center">
  <strong>Made with ❤️ by developers who love mathematics and AI</strong>
  <br>
  <sub>Star ⭐ this repo if you find it helpful!</sub>
</div>


Create Additional Files
Create backend/.env.example:
# Flask Configuration
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

# Ollama Configuration
OLLAMA_MODEL=llama3.2:latest
OLLAMA_TIMEOUT=120

# Application Settings
MAX_CONTENT_LENGTH=16777216
ANIMATION_TIMEOUT=300

# Paths
ANIMATIONS_DIR=../animations
SCENES_DIR=../animations/scenes
VIDEOS_DIR=../animations/videos


Create docker-compose.yml (Optional):
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    volumes:
      - ./animations:/app/animations
      - ./backend:/app
    environment:
      - FLASK_DEBUG=True
    depends_on:
      - ollama

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend/src:/app/src
    depends_on:
      - backend

  ollama:
    image: ollama/ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama:/root/.ollama

volumes:
  ollama:





