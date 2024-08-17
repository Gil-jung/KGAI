import React, { useState, useEffect } from 'react';
import { TextField, Button, Chip, Box, Autocomplete } from '@mui/material';
import axios from 'axios';

const Search = ({ onSearch }) => {
  const [query, setQuery] = useState('');
  const [labels, setLabels] = useState([]);
  const [availableLabels, setAvailableLabels] = useState([]);
  const [suggestions, setSuggestions] = useState([]);

  useEffect(() => {
    fetchLabels();
  }, []);

  const fetchLabels = async () => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_API_URL}/labels`);
      setAvailableLabels(response.data);
    } catch (error) {
      console.error('라벨 가져오기 오류:', error);
    }
  };

  const fetchSuggestions = async (input) => {
    if (input.length < 2) return;
    try {
      const response = await axios.get(`${process.env.REACT_APP_API_URL}/suggestions?query=${input}`);
      setSuggestions(response.data);
    } catch (error) {
      console.error('제안 가져오기 오류:', error);
    }
  };

  const handleSearch = async () => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_API_URL}/search`, {
        params: { query, labels: labels.join(',') }
      });
      onSearch(response.data);
    } catch (error) {
      console.error('검색 중 오류 발생:', error);
    }
  };

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
      <Autocomplete
        freeSolo
        options={suggestions}
        onInputChange={(event, newInputValue) => {
          setQuery(newInputValue);
          fetchSuggestions(newInputValue);
        }}
        renderInput={(params) => (
          <TextField
            {...params}
            label="검색어 입력"
            variant="outlined"
            fullWidth
          />
        )}
      />
      <Autocomplete
        multiple
        options={availableLabels}
        value={labels}
        onChange={(event, newValue) => {
          setLabels(newValue);
        }}
        renderInput={(params) => (
          <TextField
            {...params}
            variant="outlined"
            label="라벨 선택"
            placeholder="라벨"
          />
        )}
        renderTags={(value, getTagProps) =>
          value.map((option, index) => (
            <Chip variant="outlined" label={option} {...getTagProps({ index })} />
          ))
        }
      />
      <Button variant="contained" color="primary" onClick={handleSearch} fullWidth>
        검색
      </Button>
    </Box>
  );
};

export default Search;