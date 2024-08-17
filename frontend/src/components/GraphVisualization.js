import React, { useEffect, useState } from 'react';
import CytoscapeComponent from 'react-cytoscapejs';
import axios from 'axios';

const GraphVisualization = ({ data, onNodeSelect }) => {
  const [elements, setElements] = useState([]);

  useEffect(() => {
    const nodes = data.nodes.map(node => ({
      data: { ...node.data, label: node.data.name }
    }));

    const fetchEdges = async () => {
      const edgePromises = nodes.map(node =>
        axios.get(`${process.env.REACT_APP_API_URL}/nodes/${node.data.id}/edges`)
      );
      const edgeResponses = await Promise.all(edgePromises);
      const edges = edgeResponses.flatMap(response =>
        response.data.map(edge => ({
          data: {
            id: `${edge.source_id}-${edge.target_id}`,
            source: edge.source_id.toString(),
            target: edge.target_id.toString(),
            label: edge.relationship_type
          }
        }))
      );

      setElements([...nodes, ...edges]);
    };

    fetchEdges();
  }, [data]);

  const layout = {
    name: 'cose',
    animate: false,
    nodeDimensionsIncludeLabels: true,
    randomize: false,
    componentSpacing: 100,
    nodeRepulsion: 400000,
    nodeOverlap: 10,
    idealEdgeLength: 10,
    edgeElasticity: 100,
    nestingFactor: 5,
    gravity: 80,
    numIter: 1000,
    initialTemp: 200,
    coolingFactor: 0.95,
    minTemp: 1.0
  };

  const stylesheet = [
    {
      selector: 'node',
      style: {
        'background-color': '#666',
        'label': 'data(label)',
        'width': 30,
        'height': 30,
        'font-size': 10,
        'text-valign': 'center',
        'text-halign': 'center',
        'text-outline-width': 2,
        'text-outline-color': '#fff',
        'color': '#000'
      }
    },
    {
      selector: 'edge',
      style: {
        'width': 1,
        'line-color': '#ccc',
        'target-arrow-color': '#ccc',
        'target-arrow-shape': 'triangle',
        'curve-style': 'bezier',
        'label': 'data(label)',
        'font-size': 8,
        'text-rotation': 'autorotate',
        'text-margin-y': -10
      }
    }
  ];

  const handleNodeClick = (event) => {
    const node = event.target.data();
    onNodeSelect(node);
  };

  return (
    <CytoscapeComponent
      elements={elements}
      layout={layout}
      stylesheet={stylesheet}
      style={{ width: '100%', height: '500px' }}
      cy={(cy) => {
        cy.on('tap', 'node', handleNodeClick);
        cy.center();
        cy.fit();
      }}
    />
  );
};

export default GraphVisualization;