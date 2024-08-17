import React from 'react';
import { render, screen } from '@testing-library/react';
import NodeDetails from './NodeDetails';

test('renders "노드를 선택해주세요" when no node is selected', () => {
  render(<NodeDetails node={null} />);
  expect(screen.getByText('노드를 선택해주세요.')).toBeInTheDocument();
});

test('renders node details when a node is selected', () => {
  const mockNode = {
    id: '1',
    label: 'Test Node',
    category: 'Test',
    properties: { key: 'value' },
    markdown_content: '# Test Content'
  };
  render(<NodeDetails node={mockNode} />);
  expect(screen.getByText('Test Node')).toBeInTheDocument();
  expect(screen.getByText('카테고리: Test')).toBeInTheDocument();
  expect(screen.getByText('key: value')).toBeInTheDocument();
  expect(screen.getByText('Test Content')).toBeInTheDocument();
});