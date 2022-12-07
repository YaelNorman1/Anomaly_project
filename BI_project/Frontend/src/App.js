import 'bootstrap/dist/css/bootstrap.min.css'
import './App.css';
import Header from './components/header/Header';
import Filter from './components/filter/Filter';
import { Container } from 'react-bootstrap';
import { useState, useEffect } from 'react';
import AnomalyResult from './components/anomalyResult/AnomalyResult';
import axios, * as others from 'axios';
import {ANOMALIES_URL} from '../src/utils/consts'

function App() {
  const [filteredAnomalies, setFilteredAnomalies] = useState([])

  useEffect(() => {
    axios.get(ANOMALIES_URL)
    .then(function (response) {
      setFilteredAnomalies(response.data)
    })
    .catch(function (error) {
        console.error(error);
    });
  },[])
  

  function fetchFilterAnomalies(filter){
    axios.get(ANOMALIES_URL, {
        params: { userId: filter.userId, category: filter.category, fromDate: filter.fromDate, toDate: filter.toDate},
    })
    .then(function (response) {
        setFilteredAnomalies(response.data)
    })
    .catch(function (error) {
        console.error(error);
    });
  }

  return (
    <Container className="App">
      <Header />
      <Filter filter={fetchFilterAnomalies}/>
      <AnomalyResult anomalies={filteredAnomalies}/>
    </Container>
  );
}

export default App;
