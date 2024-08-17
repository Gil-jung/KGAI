import React, { useState } from 'react';
import { TextField, Button, Select, MenuItem, FormControl, InputLabel } from '@mui/material';

const SearchComponent = ({ onSearch }) => {
  const [query, setQuery] = useState('');
  const [category, setCategory] = useState('');

  const handleSearch = () => {
    onSearch(query, category);
  };

  return (
    <div>
      <TextField
        label="검색어"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <FormControl sx={{ m: 1, minWidth: 120 }}>
        <InputLabel>카테고리</InputLabel>
        <Select
          value={category}
          onChange={(e) => setCategory(e.target.value)}
        >
          <MenuItem value="">전체</MenuItem>
          <MenuItem value="Person">인물</MenuItem>
          <MenuItem value="Concept">개념</MenuItem>
          <MenuItem value="Event">사건</MenuItem>
        </Select>
      </FormControl>
      <Button variant="contained" onClick={handleSearch}>검색</Button>
    </div>
  );
};

export default SearchComponent;