import React, { useEffect, useRef } from 'react';
import CytoscapeComponent from 'react-cytoscapejs';

const GraphVisualization = ({ data, onNodeSelect }) => {
  const cyRef = useRef(null);

  useEffect(() => {
    if (cyRef.current && data && data.nodes && data.edges) {
      const cy = cyRef.current;
      
      // 기존 요소들 제거
      cy.elements().remove();
      
      // 노드 데이터 변환 및 추가
      const nodes = data.nodes.map(node => ({
        data: { 
          id: node.id.toString(),
          label: node.name,
          category: node.category
        }
      }));
      cy.add(nodes);
      
      // 엣지 데이터 변환 및 추가
      const edges = data.edges.map(edge => ({
        data: { 
          id: edge.id.toString(),
          source: edge.source.toString(),
          target: edge.target.toString(),
          label: edge.relationship_type
        }
      }));
      cy.add(edges);
      
      // 레이아웃 적용
      cy.layout({ 
        name: 'cose',
        animate: false,
        randomize: true,
        componentSpacing: 100,
        nodeOverlap: 20,
        refresh: 20,
        fit: true,
        padding: 30,
        boundingBox: undefined
      }).run();

      // 노드 선택 이벤트 핸들러
      cy.on('tap', 'node', (event) => {
        const node = event.target.data();
        onNodeSelect(node.id);
      });
    }
  }, [data, onNodeSelect]);

  return (
    <CytoscapeComponent
      elements={[]}
      style={{ width: '100%', height: '600px' }}
      cy={(cy) => { cyRef.current = cy; }}
      layout={{ name: 'preset' }}
      stylesheet={[
        {
          selector: 'node',
          style: {
            'background-color': (ele) => {
              switch(ele.data('category')) {
                case 'Person': return '#FF5733';
                case 'Concept': return '#33FF57';
                case 'Event': return '#3357FF';
                default: return '#666';
              }
            },
            'label': 'data(label)',
            'color': '#fff',
            'text-valign': 'center',
            'text-halign': 'center',
          }
        },
        {
          selector: 'edge',
          style: {
            'width': 3,
            'line-color': '#ccc',
            'target-arrow-color': '#ccc',
            'target-arrow-shape': 'triangle',
            'curve-style': 'bezier',
            'label': 'data(label)',
            'text-rotation': 'autorotate'
          }
        }
      ]}
    />
  );
};

export default GraphVisualization;