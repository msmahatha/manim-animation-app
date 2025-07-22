import React from 'react';

interface Props {
  jobId: string | null;
}

const VideoPlayer: React.FC<Props> = ({ jobId }) => {
  if (!jobId) return null;

  // Updated to use relative URL with proxy configuration
  const videoUrl = `/api/video/${jobId}`;
  
  return (
    <div className="video-player">
      <h3>🎥 Your Animation is Ready!</h3>
      <video 
        controls 
        width="100%" 
        style={{ maxWidth: '800px', borderRadius: '8px' }}
      >
        <source src={videoUrl} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      
      <div className="video-actions">
        <a 
          href={videoUrl} 
          download={`animation-${jobId}.mp4`}
          className="download-btn"
        >
          📥 Download Video
        </a>
      </div>
    </div>
  );
};

export default VideoPlayer;

