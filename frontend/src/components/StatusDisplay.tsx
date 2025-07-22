import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Props {
  jobId: string;
  onStatusUpdate: (status: any) => void;
}

const StatusDisplay: React.FC<Props> = ({ jobId, onStatusUpdate }) => {
  const [status, setStatus] = useState<any>({ status: 'processing', progress: 0 });

  useEffect(() => {
    const pollStatus = async () => {
      try {
        // Updated to use relative URL with proxy configuration
        const response = await axios.get(`/api/status/${jobId}`);
        const newStatus = response.data;
        setStatus(newStatus);
        onStatusUpdate(newStatus);

        // Continue polling if still processing
        if (newStatus.status === 'processing') {
          setTimeout(pollStatus, 2000);
        }
      } catch (error) {
        console.error('Status polling error:', error);
      }
    };

    pollStatus();
  }, [jobId, onStatusUpdate]);

  const getStatusEmoji = () => {
    switch (status.status) {
      case 'processing': return '⚙️';
      case 'completed': return '✅';
      case 'error': return '❌';
      default: return '⏳';
    }
  };

  return (
    <div className="status-display">
      <h3>Animation Status {getStatusEmoji()}</h3>
      
      <div className="progress-bar">
        <div 
          className="progress-fill" 
          style={{ width: `${status.progress || 0}%` }}
        ></div>
      </div>
      
      <p className="status-message">
        {status.message || 'Processing...'}
      </p>
      
      {status.status === 'error' && (
        <div className="error-message">
          <strong>Error:</strong> {status.error}
        </div>
      )}
      
      {status.code && (
        <details className="generated-code">
          <summary>View Generated Code</summary>
          <pre><code>{status.code}</code></pre>
        </details>
      )}
    </div>
  );
};

export default StatusDisplay;
