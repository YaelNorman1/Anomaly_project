import React, { useState, useEffect } from "react";
import { InputGroup , Form , DropdownButton , Dropdown , Row, Col , Button} from 'react-bootstrap';



function Filter() {
    const [state, setState] = useState({
        fromDate: "",
        toDate: ""
      })


    function handleChange(evt) {
        const value = evt.target.value;
        setState({
          ...state,
          [evt.target.name]: value
        });
    }

    return (
        <Row>
            <Col>
                <InputGroup className="mb-3">
                  <Form.Control
                    placeholder="Username"
                    aria-label="Username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
            </Col>

            <Col>
                <DropdownButton id="dropdown-basic-button" title="Category">
                  <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                  <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                  <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
                </DropdownButton>
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
                <Button type="submit">Button</Button>
            </Col>
        </Row>
    );
  }
  
  export default Filter;
  