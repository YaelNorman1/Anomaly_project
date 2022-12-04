import React, { useState, useEffect } from "react";
import { Form , Row, Col , Button} from 'react-bootstrap';
import axios, * as others from 'axios';



function Filter() {
    const [filter, setFilter] = useState({
        userName: "",
        category: "",
        fromDate: "",
        toDate: ""
      })
    const [categories, setCategories]  = useState([])

      useEffect(() => {
        axios.get('http://localhost:8000/categories')
        .then(function (response) {
          setCategories(response.data);
        })
        .catch(function (error) {
          console.log(error);
        })
      }, []);

    function handleChange(evt) {
        const value = evt.target.value;
        setFilter({
          ...filter,
          [evt.target.name]: value
        });
    }

    function categoriesOptions(){
      return categories.map(category=>{
         return (<option value={category} key={category}>{category}</option>)
        })
    }

    function printData(){
      console.log("user name: " + filter.userName)
      console.log("category: " + filter.category)
      console.log("from date: " + filter.fromDate)
      console.log("to date:" + filter.toDate)
    }

    return (
        <Row>
            <Col>
              <Form.Control type="email" placeholder="Enter user name" name="userName" onChange={handleChange}/>
            </Col>

            <Col>
              <Form.Select aria-label="Floating label select example" name="category" onChange={handleChange} value={filter.category}>
                <option>Open this select menu</option>
                {categoriesOptions()}
              </Form.Select>
            </Col>

            <Col>
              <Form>
                <span style={{ opacity: "0.6", fontSize: "13px" }}>from</span>
                <input
                  type="date"
                  name="fromDate"
                  id="startdate"
                  value={filter.fromDate}
                  onChange={handleChange}
                  className="form-control datepicker"
                  style={{ width: "150px" }}
                />
              </Form>
            </Col>

            <Col>
              <Form>
                <span style={{ opacity: "0.6", fontSize: "13px" }}>to</span>
                <input
                  type="date"
                  name="toDate"
                  min={filter.fromDate}
                  id="enddate"
                  value={filter.toDate}
                  placeholder="Select Date"
                  onChange={handleChange}
                  className="form-control datepicker"
                  style={{ width: "150px" }}
                />
              </Form>
            </Col>

            <Col>
                <Button type="submit" onClick={printData}>Button</Button>
            </Col>
        </Row>
    );
  }
  
  export default Filter;
  