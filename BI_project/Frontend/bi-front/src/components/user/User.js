import Anomaly from "../anomaly/Anomaly"
import '../user/User.css'
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';

export default function User (props) {
    return (
    <Card>
      <Card.Header>{props.user.userName} {props.user.userId}</Card.Header>
      <ListGroup variant="flush">
        {props.user.anomalies.map(anomaly => {
            return <Anomaly anomaly= {anomaly}/>
        })} 
      </ListGroup>
    </Card>
  );
}
