import os
import subprocess
import tempfile
import shutil
import sys

class ManimRenderer:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.animations_dir = os.path.join(self.base_dir, "..", "animations")
        self.scenes_dir = os.path.join(self.animations_dir, "scenes")
        self.videos_dir = os.path.join(self.animations_dir, "videos")
        
        # Create directories
        os.makedirs(self.scenes_dir, exist_ok=True)
        os.makedirs(self.videos_dir, exist_ok=True)
    
    def render(self, job_id, manim_code):
        scene_file = os.path.join(self.scenes_dir, f"{job_id}.py")
        
        try:
            # Write code to file
            with open(scene_file, 'w') as f:
                f.write(manim_code)
            
            # Render with Manim
            cmd = [
                sys.executable, '-m', 'manim', 
                scene_file, 
                'AnimationScene',
                '-pql',  # Preview quality, low resolution
                '--media_dir', os.path.join(self.animations_dir, 'media')
            ]
            
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                timeout=300,
                cwd=self.scenes_dir
            )
            
            if result.returncode == 0:
                # Find and move the generated video
                video_source = self._find_output_video(job_id)
                if video_source:
                    video_target = os.path.join(self.videos_dir, f"{job_id}.mp4")
                    shutil.copy2(video_source, video_target)
                    return video_target
                else:
                    raise Exception("Generated video file not found")
            else:
                error_msg = result.stderr or result.stdout
                raise Exception(f"Manim rendering failed: {error_msg}")
                
        except subprocess.TimeoutExpired:
            raise Exception("Rendering timed out (5 minutes limit)")
        except Exception as e:
            raise Exception(f"Rendering error: {str(e)}")
    
    def _find_output_video(self, job_id):
        # Look for generated video in media directory
        media_dir = os.path.join(self.animations_dir, 'media')
        
        for root, dirs, files in os.walk(media_dir):
            for file in files:
                if file.endswith('.mp4') and 'AnimationScene' in file:
                    return os.path.join(root, file)
        
        # Fallback: look for any recent mp4 file
        for root, dirs, files in os.walk(media_dir):
            for file in files:
                if file.endswith('.mp4'):
                    return os.path.join(root, file)
                    
        return None

