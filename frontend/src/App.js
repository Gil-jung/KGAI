import React, { useState } from 'react';
import axios from 'axios';
import SearchComponent from './components/SearchComponent';
import GraphVisualization from './components/GraphVisualization';
import NodeDetails from './components/NodeDetails';
import './App.css';

function App() {
  const [selectedNode, setSelectedNode] = useState(null);
  const [graphData, setGraphData] = useState({ nodes: [], edges: [] });

  const handleNodeSelect = (node) => {
    setSelectedNode(node);
  };

  const handleSearch = async (query, category) => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_API_URL}/search`, {
        params: { query, category }
      });
      const nodes = response.data.map(result => ({
        data: { id: result.id.toString(), label: result.name, category: result.category, ...result.properties }
      }));
      setGraphData({ nodes, edges: [] });
    } catch (error) {
      console.error('검색 중 오류 발생:', error);
    }
  };

  return (
    <div className="App">
      <SearchComponent onSearch={handleSearch} />
      <GraphVisualization data={graphData} onNodeSelect={handleNodeSelect} />
      <NodeDetails node={selectedNode} />
    </div>
  );
}

export default App;