import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import Search from './Search';
import axios from 'axios';

jest.mock('axios');

describe('Search Component', () => {
  it('renders search input and button', () => {
    render(<Search onSearch={() => {}} />);
    expect(screen.getByLabelText(/검색어 입력/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /검색/i })).toBeInTheDocument();
  });

  it('calls onSearch with correct parameters when search button is clicked', async () => {
    const mockOnSearch = jest.fn();
    axios.get.mockResolvedValue({ data: [] });

    render(<Search onSearch={mockOnSearch} />);

    fireEvent.change(screen.getByLabelText(/검색어 입력/i), { target: { value: 'test query' } });
    fireEvent.click(screen.getByRole('button', { name: /검색/i }));

    await waitFor(() => {
      expect(axios.get).toHaveBeenCalledWith(`${process.env.REACT_APP_API_URL}/search`, {
        params: { query: 'test query', labels: '' }
      });
    });

    expect(mockOnSearch).toHaveBeenCalled();
  });
});