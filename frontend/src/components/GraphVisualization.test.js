import React from 'react';
import { render, screen } from '@testing-library/react';
import GraphVisualization from './GraphVisualization';

// CytoscapeComponent를 모의(mock)합니다.
jest.mock('react-cytoscapejs', () => {
  return function DummyCytoscape(props) {
    return <div data-testid="cytoscape-mock" />;
  };
});

describe('GraphVisualization', () => {
  const mockData = {
    nodes: [
      { data: { id: '1', name: 'Node 1', label: 'Node 1' } },
      { data: { id: '2', name: 'Node 2', label: 'Node 2' } },
    ],
    edges: [
      { data: { source: '1', target: '2', label: 'relates to' } },
    ],
  };

  const mockOnNodeSelect = jest.fn();

  it('renders without crashing', () => {
    render(<GraphVisualization data={mockData} onNodeSelect={mockOnNodeSelect} />);
    expect(screen.getByTestId('cytoscape-mock')).toBeInTheDocument();
  });

  it('passes correct props to CytoscapeComponent', () => {
    render(<GraphVisualization data={mockData} onNodeSelect={mockOnNodeSelect} />);
    const cytoscapeElement = screen.getByTestId('cytoscape-mock');
    
    expect(cytoscapeElement).toHaveStyle('width: 100%');
    expect(cytoscapeElement).toHaveStyle('height: 500px');
  });
});