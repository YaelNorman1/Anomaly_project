import Anomaly from "../anomaly/Anomaly"
import '../user/User.css'
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import ApiCalls from '../../apiModel/apiCalls';
import { useEffect, useState } from "react";

const api= new ApiCalls();

export default function User (props) {

  const [userStatistic, setUserStatistic]= useState({});
  
  useEffect(() => {
    api.callGetUserStatistic(props.user.userId)    
    .then(function (response) {
      setUserStatistic(response.data);
    })
    .catch(function (error) {
      console.log(error);
    })
  }, [userStatistic]);


  return (
    <Card>
      <Card.Header className="user-header">{userStatistic.userName}- {userStatistic.userId}</Card.Header>
      <ListGroup variant="flush">
        {props.user.anomalies.map(anomaly => {
            return <Anomaly key={anomaly.anomalyId} anomaly= {anomaly} userId= {userStatistic.userId} userStatistic= {userStatistic}/> 
        })} 
      </ListGroup>
    </Card>
  );
}
