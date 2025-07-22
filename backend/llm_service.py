import subprocess
import json
import re

class LlamaGenerator:
    def __init__(self):
        self.model_name = "llama3.2:latest"
        
    def generate_code(self, user_input):
        # Create optimized prompt for Manim
        prompt = self._create_manim_prompt(user_input)
        
        try:
            # Use Ollama CLI to generate code
            result = subprocess.run([
                'ollama', 'run', self.model_name, prompt
            ], capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0:
                generated_code = result.stdout.strip()
                return self._clean_code(generated_code)
            else:
                raise Exception(f"Ollama error: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            raise Exception("Code generation timed out")
        except FileNotFoundError:
            raise Exception("Ollama not found. Please install Ollama first.")
    
    def _create_manim_prompt(self, user_input):
        return f"""You are a Manim expert. Generate clean, executable Python code using the Manim library for 2D animation.

REQUIREMENTS:
- Import: from manim import *
- Class name: AnimationScene
- Inherit from Scene class
- Use construct method
- Include clear comments
- Make sure code is complete and runnable
- Focus on 2D animations only
- Keep animations simple and clear

USER REQUEST: {user_input}

Generate ONLY the Python code, no explanations:

from manim import *

class AnimationScene(Scene):
    def construct(self):
        # Animation code here

PYTHON CODE:"""

    def _clean_code(self, code):
        # Extract code block if wrapped in markdown
        code_pattern = r'``````'
        match = re.search(code_pattern, code, re.DOTALL)
        if match:
            code = match.group(1).strip()
        
        # Basic validation and fixes
        if 'from manim import' not in code and 'import manim' not in code:
            code = 'from manim import *\n\n' + code
            
        if 'class AnimationScene' not in code:
            # If no class, wrap in basic structure
            if 'def construct' not in code:
                code = f"""from manim import *

class AnimationScene(Scene):
    def construct(self):
        {code}"""
                
        return code

