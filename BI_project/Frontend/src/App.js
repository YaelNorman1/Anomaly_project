import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import Header from "./components/header/Header";
import Filter from "./components/filter/Filter";
import { Container, Row } from "react-bootstrap";
import { useState, useEffect } from "react";
import AnomalyResult from "./components/anomalyResult/AnomalyResult";
import axios, * as others from "axios";
import { ANOMALIES_URL, CATEGORIES_ENUM } from "../src/utils/consts";
import Amount from "./components/amount/Amount";
import PieChart from "./components/graph/PieChart";
import GraphComboChart from './components/graphComboChart/GraphComboChart';

function App() {
  const [filteredAnomalies, setFilteredAnomalies] = useState([])
  
  useEffect(() => {
    axios
      .get(ANOMALIES_URL)
      .then(function (response) {
        setFilteredAnomalies(response.data);
      })
      .catch(function (error) {
        console.error(error);
      });
  }, []);

  function fetchFilterAnomalies(filter) {
    axios
      .get(ANOMALIES_URL, {
        params: {
          userId: filter.userId,
          category: filter.category,
          fromDate: filter.fromDate,
          toDate: filter.toDate,
        },
      })
      .then(function (response) {
        setFilteredAnomalies(response.data);
      })
      .catch(function (error) {
        console.error(error);
      });
  }

  function parseDataForPie() {
    const categoriesMap = new Map();
    for (let anomaly of filteredAnomalies) {
      let c = anomaly.category;
      categoriesMap.set(c, categoriesMap.get(c) + 1 || 1);
    }
    let categoriesMapAsArr = Array.from(
      categoriesMap,
      ([category, counter]) => [CATEGORIES_ENUM[category], counter]
    );

    return [["Category", "counter"], ...categoriesMapAsArr];
  }

  return (
    <Container className="App">
      <Header />
      <Row className='mt-2'>
        <Amount filteredAnomalies={filteredAnomalies} counter="amount"/>
        <Amount filteredAnomalies={filteredAnomalies} counter="num"/>
        <Amount filteredAnomalies={filteredAnomalies} counter="total"/>
      </Row>
      <Row className="mt-2">
        <PieChart data={parseDataForPie()} />
        <GraphComboChart/>
      </Row>
      <Filter filter={fetchFilterAnomalies} />
      <AnomalyResult anomalies={filteredAnomalies} />
    </Container>
  );
}

export default App;
