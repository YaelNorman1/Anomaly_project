import logo from './logo.svg';
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

  // useEffect(() => {
  //   setFilteredAnomalies([



  //     {userId: 2, userName: 'yael', category: 'food',quantity: 10000, startDate: new Date(1995, 11, 17),endDate: new Date(1995, 11, 18)},
  //     {userId: 2, userName: 'yael', category: 'food',quantity: 1000000, startDate: new Date(1995, 11, 1) ,endDate: new Date(1995, 11, 20)},
  //     {userId: 2, userName: 'yael', category: 'shooping',quantity: 10000000, startDate: new Date(1995, 11, 22),endDate: new Date(1995, 10, 17)},
  //     {userId: 3, userName: 'ohad', category: 'food' ,quantity: 100, startDate: new Date(1995, 11, 17), endDate: new Date(1995, 11, 17) },
  //     {userId: 3, userName: 'ohad', category: 'food' ,quantity: 200, startDate: new Date(1995, 11, 17), endDate: new Date(1995, 11, 17) },
  //     {userId: 4, userName: 'tom', category: 'food' ,quantity: 300, startDate: new Date(1995, 11, 17), endDate: new Date(1995, 11, 17) },
  //     {userId: 5, userName: 'yagel', category: 'food' ,quantity: 400, startDate: new Date(1995, 11, 17), endDate: new Date(1995, 11, 17) },
  //   ])
  // },[])
  

  function fetchFilterAnomalies(filter){
    axios
    .get(ANOMALIES_URL, {
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
