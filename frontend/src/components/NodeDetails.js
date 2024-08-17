import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import { Typography, Paper, Button, CircularProgress } from '@mui/material';
import axios from 'axios';

const NodeDetails = ({ node, onExpandNode }) => {
  const [details, setDetails] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (node) {
      fetchNodeDetails(node.id);
    }
  }, [node]);

  const fetchNodeDetails = async (nodeId) => {
    setLoading(true);
    try {
      const response = await axios.get(`${process.env.REACT_APP_API_URL}/nodes/${nodeId}`);
      setDetails(response.data);
    } catch (error) {
      console.error('노드 상세 정보 가져오기 오류:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleExpand = () => {
    if (node) {
      onExpandNode(node.id);
    }
  };

  if (!node) {
    return <Typography>노드를 선택해주세요.</Typography>;
  }

  if (loading) {
    return <CircularProgress />;
  }

  return (
    <Paper elevation={3} sx={{ p: 2 }}>
      <Typography variant="h5" gutterBottom>{node.label}</Typography>
      {details && (
        <>
          <Typography variant="subtitle1">속성:</Typography>
          {Object.entries(details.properties).map(([key, value]) => (
            <Typography key={key} variant="body2">{`${key}: ${value}`}</Typography>
          ))}
          <Typography variant="subtitle1" sx={{ mt: 2 }}>상세 내용:</Typography>
          <ReactMarkdown>{details.markdown_content}</ReactMarkdown>
          <Button variant="contained" color="primary" onClick={handleExpand} sx={{ mt: 2 }}>
            노드 확장
          </Button>
        </>
      )}
    </Paper>
  );
};

export default NodeDetails;