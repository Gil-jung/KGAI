import React, { useState } from 'react';
import axios from 'axios';
import SearchComponent from './components/SearchComponent';
import GraphVisualization from './components/GraphVisualization';
import NodeDetails from './components/NodeDetails';
import './App.css';

function App() {
  const [selectedNode, setSelectedNode] = useState(null);
  const [graphData, setGraphData] = useState(null);

  const handleNodeSelect = async (nodeId) => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_API_URL}/nodes/${nodeId}/with_connections`);
      setGraphData(response.data);
      setSelectedNode(response.data.nodes.find(node => node.id === nodeId));
    } catch (error) {
      console.error('노드 정보 가져오기 오류:', error);
    }
  };

  const handleSearch = async (query, category) => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_API_URL}/search`, {
        params: { query, category }
      });
      if (response.data.length > 0) {
        const nodeId = response.data[0].id;
        handleNodeSelect(nodeId);
      } else {
        console.log('No results found');
        setGraphData(null);
        setSelectedNode(null);
      }
    } catch (error) {
      console.error('검색 중 오류 발생:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <SearchComponent onSearch={handleSearch} />
      </header>
      <main className="App-main">
        <div className="graph-container">
          {graphData ? (
            <GraphVisualization data={graphData} onNodeSelect={handleNodeSelect} />
          ) : (
            <div className="graph-placeholder">검색어를 입력하세요...</div>
          )}
        </div>
        <div className="details-container">
          <NodeDetails nodeId={selectedNode?.id} />
        </div>
      </main>
    </div>
  );
}

export default App;