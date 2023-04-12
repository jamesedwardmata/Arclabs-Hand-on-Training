import React from "react";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

class mock_data extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        error: null,
        isLoaded: false,
        books: []
      };
    }
  
    componentDidMount() {
      fetch("http://127.0.0.1:8000/mockdata/")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              isLoaded: true,
              books: result
            });
          },
          // Note: it's important to handle errors here
          // instead of a catch() block so that we don't swallow
          // exceptions from actual bugs in components.
          (error) => {
            this.setState({
              isLoaded: true,
              error
            });
          }
        )
    }
  
    render() {
      const { error, isLoaded, books } = this.state;
      if (error) {
        return <div>Error: {error.message}</div>;
      } else if (!isLoaded) {
        return <div>Loading...</div>;
      } else {
        return (
            <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} size="small" aria-label="a dense table">
              <TableHead>
                <TableRow>
                  <TableCell>Title</TableCell>
                  <TableCell align="center">Author</TableCell>
                  <TableCell align="center">Date</TableCell>
                  <TableCell align="center">Content</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {books.map((books) => (
                  <TableRow
                    key={books.id}
                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                  >
                    <TableCell component="th" scope="row">
                      {books.Title}
                    </TableCell>
                    <TableCell align="center">{books.author}</TableCell>
                    <TableCell align="center">{books.Date}</TableCell>
                    <TableCell align="center">{books.Content}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
          
        );
      }
    }
  }

  export default mock_data