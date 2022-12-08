import React, { useState, useEffect } from "react";
import { Form , Row, Col , Container} from 'react-bootstrap';
import axios, * as others from 'axios';
import {CATEGORIES_URL} from '../../utils/consts';
import '../filter/Filter.css'
// import { Dayjs } from 'dayjs';
import TextField from '@mui/material/TextField';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import InputLabel from '@mui/material/InputLabel';
import { FormControl } from "@mui/material";
import Button from '@mui/material/Button';





function Filter(props) {
    const [filter, setFilter] = useState({
        userId: "",
        category: "",
        fromDate: null,
        toDate: null
      })
    const [categories, setCategories]  = useState([])
    const [value, setValue] = useState("");


    useEffect(() => {
      axios.get(CATEGORIES_URL)
      .then(function (response) {
        setCategories(response.data);
      })
      .catch(function (error) {
        console.log(error);
      })
    }, []);

    function handleChange(evt) {
      console.log(evt)
        const value = evt.target.value;
        setFilter({
          ...filter,
          [evt.target.name]: value
        });
    }

    function categoriesOptions(){
      return categories.map(category=><MenuItem  value={category}>{category}</MenuItem> )
    }

    return (
      <Container className="filter-row">
        <Row>
            <Col>
              <TextField
                id="outlined-number"
                label="User ID"
                type="number"
                onChange={handleChange}
                name= "userId"
                // InputLabelProps={{
                //   // shrink: true,
                // }}
              />
            </Col>

            <Col>
            <FormControl fullWidth>
              <InputLabel id="choose-category">Category</InputLabel>
              <Select
                labelId="choose-category"
                value={filter.category}
                label="Category"
                name= "category"
                onChange={handleChange}
              >
                {categoriesOptions()}
              </Select>
              </FormControl>
            </Col>

            <Col>
              <LocalizationProvider dateAdapter={AdapterDayjs}>
                <DatePicker
                  label="Start Date"
                  value={filter.fromDate}
                  onChange={(newValue) =>{
                    setFilter({
                      ...filter,
                      ["fromDate"]: JSON.stringify(newValue).slice(1,11)})
                  }}
                  renderInput={(params) => <TextField {...params} />}
                />
              </LocalizationProvider>
            </Col>

            <Col>
            <LocalizationProvider dateAdapter={AdapterDayjs}>
                <DatePicker
                  label="End Date"
                  value={filter.toDate}
                  onChange={(newValue) =>{
                    setFilter({
                      ...filter,
                      ["toDate"]: JSON.stringify(newValue).slice(1,11)})
                  }}
                  renderInput={(params) => <TextField {...params} />}
                />
              </LocalizationProvider>
            </Col>

            <Col>
                <Button type="submit" variant="contained" className="search-btn" onClick={()=>{props.filter(filter)}}>Search</Button>
            </Col>
        </Row>
      </Container>
    );
  }
  
  export default Filter;
  