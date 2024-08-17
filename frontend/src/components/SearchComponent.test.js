import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import SearchComponent from './SearchComponent';

test('renders search input and category select', () => {
  render(<SearchComponent onSearch={() => {}} />);
  expect(screen.getByLabelText('검색어')).toBeInTheDocument();
  expect(screen.getByLabelText('카테고리')).toBeInTheDocument();
});

test('calls onSearch with correct parameters when search button is clicked', () => {
  const mockOnSearch = jest.fn();
  render(<SearchComponent onSearch={mockOnSearch} />);
  
  fireEvent.change(screen.getByLabelText('검색어'), { target: { value: 'test query' } });
  fireEvent.change(screen.getByLabelText('카테고리'), { target: { value: 'Person' } });
  fireEvent.click(screen.getByText('검색'));

  expect(mockOnSearch).toHaveBeenCalledWith('test query', 'Person');
});