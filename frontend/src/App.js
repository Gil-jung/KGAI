import React, { useState } from 'react';
import { Container, Grid, Paper, ThemeProvider, createTheme, CssBaseline, CircularProgress } from '@mui/material';
import { styled } from '@mui/material/styles';
import Graph from './components/Graph';
import Search from './components/Search';
import NodeDetails from './components/NodeDetails';
import axios from 'axios';
import './App.css';
import ErrorBoundary from './components/ErrorBoundary';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(2),
  height: '100%',
}));

function App() {
  const [selectedNode, setSelectedNode] = useState(null);
  const [graphData, setGraphData] = useState({ nodes: [], edges: [] });
  const [loading, setLoading] = useState(false);

  const handleNodeSelect = (node) => {
    setSelectedNode(node);
  };

  const handleSearch = async (query, labels) => {
    setLoading(true);
    try {
      const response = await axios.get(`${process.env.REACT_APP_API_URL}/search`, {
        params: { query, labels: labels.join(',') }
      });
      const nodes = response.data.map(result => ({
        data: { id: result.node_id.toString(), label: result.label, ...result.properties }
      }));
      setGraphData({ nodes, edges: [] });
    } catch (error) {
      console.error('검색 중 오류 발생:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleExpandNode = async (nodeId) => {
    setLoading(true);
    try {
      const response = await axios.post(`${process.env.REACT_APP_API_URL}/expand-node/${nodeId}`);
      const newNodes = response.data.expanded_nodes.map(node => ({
        data: { id: node.id.toString(), label: node.label, ...node.properties }
      }));
      const newEdges = response.data.expanded_nodes.map(node => ({
        data: { source: nodeId.toString(), target: node.id.toString(), label: 'related' }
      }));

      setGraphData(prevData => ({
        nodes: [...prevData.nodes, ...newNodes],
        edges: [...prevData.edges, ...newEdges]
      }));
    } catch (error) {
      console.error('노드 확장 중 오류 발생:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <ErrorBoundary>
        <Container maxWidth="lg">
          <Grid container spacing={3}>
            <Grid item xs={12}>
              <StyledPaper>
                <Search onSearch={handleSearch} />
              </StyledPaper>
            </Grid>
            <Grid item xs={8}>
              <StyledPaper sx={{ height: '600px', position: 'relative' }}>
                {loading && (
                  <CircularProgress
                    sx={{
                      position: 'absolute',
                      top: '50%',
                      left: '50%',
                      marginTop: '-20px',
                      marginLeft: '-20px',
                    }}
                  />
                )}
                <Graph data={graphData} onNodeSelect={handleNodeSelect} />
              </StyledPaper>
            </Grid>
            <Grid item xs={4}>
              <StyledPaper>
                <NodeDetails node={selectedNode} onExpandNode={handleExpandNode} />
              </StyledPaper>
            </Grid>
          </Grid>
        </Container>
      </ErrorBoundary>
    </ThemeProvider>
  );
}

export default App;