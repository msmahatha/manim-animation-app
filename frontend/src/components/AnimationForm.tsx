import React, { useState } from 'react';
import axios from 'axios';

interface Props {
  onSubmit: (jobId: string) => void;
}

const AnimationForm: React.FC<Props> = ({ onSubmit }) => {
  const [description, setDescription] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!description.trim()) return;

    setIsSubmitting(true);
    
    try {
      // Updated to use relative URL with proxy configuration
      const response = await axios.post('/api/generate', {
        description
      });

      if (response.data.job_id) {
        onSubmit(response.data.job_id);
      } else {
        alert('Error starting animation generation');
      }
    } catch (error: any) {
      alert('Connection error: ' + error.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  const examples = [
    "A red circle moving from left to right",
    "Text saying 'Hello Manim' appearing with fade in effect",
    "A blue square transforming into a green circle",
    "Graph of y = x² with a moving point",
    "Two vectors being added geometrically"
  ];

  return (
    <div className="animation-form">
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="description">Describe your 2D animation:</label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="e.g., Create an animation showing a bouncing ball that changes color"
            rows={4}
            disabled={isSubmitting}
          />
        </div>
        
        <button 
          type="submit" 
          disabled={isSubmitting || !description.trim()}
          className="generate-btn"
        >
          {isSubmitting ? '🔄 Generating...' : '🎬 Generate Animation'}
        </button>
      </form>
      
      <div className="examples">
        <h3>💡 Try these examples:</h3>
        <ul>
          {examples.map((example, index) => (
            <li 
              key={index}
              onClick={() => setDescription(example)}
              className="example-item"
            >
              {example}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default AnimationForm;

