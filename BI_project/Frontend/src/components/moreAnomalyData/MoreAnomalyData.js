import React, { useState, useRef } from 'react';
// import Button from 'react-bootstrap/Button';
import Overlay from 'react-bootstrap/Overlay';
import Popover from 'react-bootstrap/Popover';
import {CATEGORIES_ENUM} from '../../utils/consts';
import '../moreAnomalyData/popover.css';
import Button from '@mui/material/Button';


export default function MoreAnomalyData(props) {
  const [show, setShow] = useState(false);
  const [target, setTarget] = useState(null);
  const ref = useRef(null);


  const getRenderCategory = () => {
      return CATEGORIES_ENUM[props.category];

  }

  const setCategoryDataToRender= () => {
      const category= getRenderCategory();
      return (
        <Popover.Body>
          <strong>Anomaly: </strong> {category} <br/>
          <strong>Average Behavior: </strong> {props.userStatistic[props.category]}<br/>
          <strong>Description: </strong> Please notice to this unusual {category}!<br/>
          The average of {category} is <strong>{props.userStatistic[props.category]}</strong> and now we found an anomaly behavior of <strong style={{color: "red"}}>{props.quantity}</strong> {category}.
        </Popover.Body>
      );
  }

  const handleClick = (event) => {
    setShow(!show);
    setTarget(event.target);    
  };

  return (
    <div ref={ref}>
      <Button type="submit" variant="contained" className='info-btn' onClick={handleClick}>More Info</Button>

      <Overlay
        show={show}
        target={target}
        placement="bottom"
        container={ref}
        containerPadding={20}
      >
        <Popover id="popover-contained">
          <Popover.Header as="h3">{props.userStatistic.userName} - {props.userStatistic.userId}</Popover.Header>
            {setCategoryDataToRender()}
        </Popover>
      </Overlay>
    </div>
  );
}
