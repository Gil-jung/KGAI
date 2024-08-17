import React from 'react';
import { Typography, Button, Box } from '@mui/material';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught by ErrorBoundary:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <Box sx={{ p: 3, textAlign: 'center' }}>
          <Typography variant="h5" gutterBottom>
            오류가 발생했습니다.
          </Typography>
          <Button
            variant="contained"
            color="primary"
            onClick={() => this.setState({ hasError: false })}
          >
            다시 시도
          </Button>
        </Box>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;