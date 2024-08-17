import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import NodeDetails from './NodeDetails';
import axios from 'axios';

jest.mock('axios');

describe('NodeDetails Component', () => {
  const mockNode = { id: '1', label: 'Test Node' };

  it('renders node details when node is provided', async () => {
    axios.get.mockResolvedValue({ data: { properties: {}, content: 'Test content' } });

    render(<NodeDetails node={mockNode} onExpandNode={() => {}} onUpdateNode={() => {}} />);

    await screen.findByText('Test Node');
    await screen.findByText('Test content');
  });

  it('allows editing node content', async () => {
    axios.get.mockResolvedValue({ data: { properties: {}, content: 'Initial content' } });
    axios.put.mockResolvedValue({});

    render(<NodeDetails node={mockNode} onExpandNode={() => {}} onUpdateNode={() => {}} />);

    await waitFor(() => {
      expect(screen.getByText('Initial content')).toBeInTheDocument();
    });

    fireEvent.click(screen.getByText('편집'));

    const textarea = screen.getByRole('textbox');
    fireEvent.change(textarea, { target: { value: 'Updated content' } });
    fireEvent.click(screen.getByText('저장'));

    await waitFor(() => {
      expect(axios.put).toHaveBeenCalledWith(`${process.env.REACT_APP_API_URL}/nodes/1`, {
        content: 'Updated content'
      });
    });
    
    expect(screen.getByText('Updated content')).toBeInTheDocument();
  });
});