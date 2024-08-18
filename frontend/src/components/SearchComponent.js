import React, { useState } from 'react';
import './SearchComponent.css';

const SearchComponent = ({ onSearch }) => {
  const [query, setQuery] = useState('');
  const [category, setCategory] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(query, category);
  };

  return (
    <form className="search-form" onSubmit={handleSubmit}>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="검색어 입력..."
        className="search-input"
      />
      <select
        value={category}
        onChange={(e) => setCategory(e.target.value)}
        className="search-category"
      >
        <option value="">모든 카테고리</option>
        <option value="Person">Person</option>
        <option value="Concept">Concept</option>
        <option value="Event">Event</option>
      </select>
      <button type="submit" className="search-button">검색</button>
    </form>
  );
};

export default SearchComponent;