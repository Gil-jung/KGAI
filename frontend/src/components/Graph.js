import React, { useEffect, useRef } from 'react';
import cytoscape from 'cytoscape';
import CytoscapeComponent from 'react-cytoscapejs';
import cola from 'cytoscape-cola';
import popper from 'cytoscape-popper';
import tippy from 'tippy.js';
import 'tippy.js/dist/tippy.css';
import { IconButton, Tooltip } from '@mui/material';
import ZoomInIcon from '@mui/icons-material/ZoomIn';
import ZoomOutIcon from '@mui/icons-material/ZoomOut';
import CenterFocusStrongIcon from '@mui/icons-material/CenterFocusStrong';

cytoscape.use(cola);
cytoscape.use(popper);

const Graph = ({ data, onNodeSelect }) => {
  const cyRef = useRef(null);

  useEffect(() => {
    if (cyRef.current) {
      cyRef.current.layout({ name: 'cola', animate: false, maxSimulationTime: 2000 }).run();
      addTooltips(cyRef.current);
    }
  }, [data]);

  const addTooltips = (cy) => {
    cy.nodes().forEach((node) => {
      const ref = node.popperRef();
      const content = `
        <strong>${node.data('label')}</strong><br>
        ${Object.entries(node.data())
          .filter(([key]) => !['id', 'label'].includes(key))
          .map(([key, value]) => `${key}: ${value}`)
          .join('<br>')}
      `;
      
      tippy(ref, {
        content: content,
        trigger: 'manual',
        arrow: true,
        placement: 'bottom',
      });
    });

    cy.on('mouseover', 'node', (event) => {
      event.target.tippy.show();
    });

    cy.on('mouseout', 'node', (event) => {
      event.target.tippy.hide();
    });
  };

  const handleZoomIn = () => {
    if (cyRef.current) {
      cyRef.current.zoom(cyRef.current.zoom() * 1.2);
    }
  };

  const handleZoomOut = () => {
    if (cyRef.current) {
      cyRef.current.zoom(cyRef.current.zoom() / 1.2);
    }
  };

  const handleFit = () => {
    if (cyRef.current) {
      cyRef.current.fit();
    }
  };

  const stylesheet = [
    {
      selector: 'node',
      style: {
        'background-color': '#4CAF50',
        'label': 'data(label)',
        'color': '#fff',
        'text-valign': 'center',
        'text-halign': 'center',
        'font-size': '12px',
        'width': '60px',
        'height': '60px'
      }
    },
    {
      selector: 'edge',
      style: {
        'width': 2,
        'line-color': '#ccc',
        'target-arrow-color': '#ccc',
        'target-arrow-shape': 'triangle',
        'curve-style': 'bezier'
      }
    },
    {
      selector: ':selected',
      style: {
        'background-color': '#2196F3',
        'line-color': '#2196F3',
        'target-arrow-color': '#2196F3',
        'source-arrow-color': '#2196F3'
      }
    }
  ];

  const layout = {
    name: 'cola',
    animate: true,
    refresh: 1,
    maxSimulationTime: 4000,
    ungrabifyWhileSimulating: true,
    fit: true,
    padding: 30
  };

  return (
    <div style={{ position: 'relative', width: '100%', height: '100%' }}>
      <CytoscapeComponent
        elements={data.nodes.concat(data.edges)}
        stylesheet={stylesheet}
        layout={layout}
        style={{ width: '100%', height: '100%' }}
        cy={(cy) => {
          cyRef.current = cy;
          cy.on('tap', 'node', (event) => {
            const node = event.target;
            onNodeSelect(node.data());
          });
        }}
      />
      <div style={{ position: 'absolute', bottom: 10, right: 10 }}>
        <Tooltip title="확대">
          <IconButton onClick={handleZoomIn}>
            <ZoomInIcon />
          </IconButton>
        </Tooltip>
        <Tooltip title="축소">
          <IconButton onClick={handleZoomOut}>
            <ZoomOutIcon />
          </IconButton>
        </Tooltip>
        <Tooltip title="화면에 맞추기">
          <IconButton onClick={handleFit}>
            <CenterFocusStrongIcon />
          </IconButton>
        </Tooltip>
      </div>
    </div>
  );
};

export default Graph;