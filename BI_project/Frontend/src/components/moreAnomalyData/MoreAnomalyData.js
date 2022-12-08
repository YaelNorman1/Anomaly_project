import React, { useState, useRef } from 'react';
import Button from 'react-bootstrap/Button';
import Overlay from 'react-bootstrap/Overlay';
import Popover from 'react-bootstrap/Popover';
import ApiCalls from '../../apiModel/apiCalls';
import {CATEGORIES_ENUM} from '../../utils/consts';
import '../moreAnomalyData/popover.css'

const api= new ApiCalls();

const CATEGORIES= {
  avgNumOfWithdraws: "Number Of Withdraws"
} 

export default function MoreAnomalyData(props) {
  const [show, setShow] = useState(false);
  const [target, setTarget] = useState(null);
  const ref = useRef(null);
  const [userStatistic, setUserStatistic]= useState({});
  
  const saveUserStatistic= () => {
    api.callGetUserStatistic(props.userId)    
    .then(function (response) {
      setUserStatistic(response.data);
    })
    .catch(function (error) {
      console.log(error);
    })
  }

  const getRenderCategory = () => {
      return CATEGORIES_ENUM[props.category];

  }

  const setCategoryDataToRender= () => {
      const category= getRenderCategory();
      // console.log(category)
      return (
        <Popover.Body>
          <strong>Anomaly: </strong> {category} <br/>
          <strong>Average Behavior: </strong> {userStatistic[props.category]}<br/>
          <strong>Description: </strong> Please notice to this unusual {category}!<br/>
          The average of {category} is <strong>{userStatistic[props.category]}</strong> and now we found an anomaly behavior of <strong style={{color: "red"}}>{props.quantity}</strong> {category}.
        </Popover.Body>
      );
  }

  const handleClick = (event) => {
    setShow(!show);
    setTarget(event.target);
    if (!show){
      saveUserStatistic();
      console.log(props.userStatistic)
    }
    
  };

  return (
    <div ref={ref}>
      <Button onClick={handleClick}>More Info</Button>

      <Overlay
        show={show}
        target={target}
        placement="bottom"
        container={ref}
        containerPadding={20}
      >
        <Popover id="popover-contained">
          <Popover.Header as="h3">{userStatistic.userName} - {userStatistic.userId}</Popover.Header>
          {/* <Popover.Body> */}
            {setCategoryDataToRender()}
          {/* </Popover.Body> */}
        </Popover>
      </Overlay>
    </div>
  );
}
