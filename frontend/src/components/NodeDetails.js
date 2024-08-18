import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import { Typography, Paper } from '@mui/material';
import axios from 'axios';

const NodeDetails = ({ nodeId }) => {
  const [markdownContent, setMarkdownContent] = useState('');

  useEffect(() => {
    const fetchMarkdown = async () => {
      if (!nodeId) return;
      
      try {
        const response = await axios.get(`${process.env.REACT_APP_API_URL}/nodes/${nodeId}/markdown`);
        setMarkdownContent(response.data.content);
      } catch (error) {
        console.error('Error fetching markdown:', error);
        setMarkdownContent('Failed to load markdown content.');
      }
    };

    fetchMarkdown();
  }, [nodeId]);

  if (!nodeId) return null;

  return (
    <Paper elevation={3} sx={{ p: 2 }}>
      <Typography variant="h5" gutterBottom>Node Details</Typography>
      <ReactMarkdown>{markdownContent}</ReactMarkdown>
    </Paper>
  );
};

export default NodeDetails;