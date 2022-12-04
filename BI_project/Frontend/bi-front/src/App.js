import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css'
import './App.css';
import Header from './components/header/Header';
import Filter from './components/filter/Filter';
import { Container } from 'react-bootstrap';
import { useState } from 'react';

function App() {


  return (
    <Container className="App">
      <Header />
      <Filter />
      
    </Container>
  );
}

export default App;
