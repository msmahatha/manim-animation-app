import React, { useState, useEffect } from 'react';
import axios from 'axios';
import AnimationForm from './components/AnimationForm';
import StatusDisplay from './components/StatusDisplay';
import VideoPlayer from './components/VideoPlayer';
import './App.css';

// Configure axios defaults to prevent 403 errors
axios.defaults.headers.post['Content-Type'] = 'application/json';
axios.defaults.headers.common['Accept'] = 'application/json';
axios.defaults.timeout = 60000; // 60 second timeout

function App() {
  const [currentJob, setCurrentJob] = useState<string | null>(null);
  const [jobStatus, setJobStatus] = useState<any>(null);

  const handleSubmission = (jobId: string) => {
    setCurrentJob(jobId);
    setJobStatus({ status: 'processing', progress: 0 });
  };

  const handleStatusUpdate = (status: any) => {
    setJobStatus(status);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🎬 AI-Powered Manim Animation Generator</h1>
        <p>Powered by Llama 3.2 + Manim - Describe your animation and watch AI bring it to life!</p>
      </header>
      
      <main className="container">
        <AnimationForm onSubmit={handleSubmission} />
        
        {currentJob && (
          <StatusDisplay
            jobId={currentJob}
            onStatusUpdate={handleStatusUpdate}
          />
        )}
        
        {jobStatus?.status === 'completed' && (
          <VideoPlayer jobId={currentJob} />
        )}
      </main>
    </div>
  );
}

export default App;
