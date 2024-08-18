import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import './NodeDetails.css';

const NodeDetails = ({ nodeId }) => {
  const [markdownContent, setMarkdownContent] = useState('');

  useEffect(() => {
    const fetchMarkdown = async () => {
      if (!nodeId) return;
      
      try {
        const response = await axios.get(`${process.env.REACT_APP_API_URL}/nodes/${nodeId}/markdown`);
        setMarkdownContent(response.data.content);
      } catch (error) {
        console.error('마크다운 가져오기 오류:', error);
        setMarkdownContent('마크다운 내용을 불러오는 데 실패했습니다.');
      }
    };

    fetchMarkdown();
  }, [nodeId]);

  if (!nodeId) return <div className="node-details-placeholder">노드를 선택하세요...</div>;

  return (
    <div className="node-details">
      <h2>노드 상세 정보</h2>
      <div className="markdown-content">
        <ReactMarkdown>{markdownContent}</ReactMarkdown>
      </div>
    </div>
  );
};

export default NodeDetails;