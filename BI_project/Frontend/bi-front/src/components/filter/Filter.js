import React, { useState, useEffect } from "react";
import { Form , Row, Col , Button} from 'react-bootstrap';
import axios, * as others from 'axios';



function Filter() {
    const [state, setState] = useState({
        userName: "",
        category: [],
        fromDate: "",
        toDate: ""
      })

      useEffect(() => {
        axios.get('http://localhost:8000/categories')
        .then(function (response) {
          console.log(response.data)
          setState({
            ...state,
            ['category']: response.data
          });
        })
        .catch(function (error) {
          console.log(error);
        })
      }, []);

    function handleChange(evt) {
        const value = evt.target.value;
        setState({
          ...state,
          [evt.target.name]: value
        });
        console.log(state)
    }

    function categoriesOptions(){
      return state.category.map(category=>{
         return (<option value="{category}">{category}</option>)
        })
    }

    function printData(){
      console.log("user name: " + state.userName)
      console.log("category: " + state.category)
      console.log("from date: " + state.fromDate)
      console.log("to date:" + state.toDate)
    }

    return (
        <Row>
            <Col>
              <Form.Control type="email" placeholder="Enter user name" name="userName" onChange={handleChange}/>
            </Col>

            <Col>
              <Form.Select aria-label="Floating label select example" name="category" onChange={handleChange} value={state.category}>
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
                  value={state.fromDate}
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
                  min={state.fromDate}
                  id="enddate"
                  value={state.toDate}
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
  