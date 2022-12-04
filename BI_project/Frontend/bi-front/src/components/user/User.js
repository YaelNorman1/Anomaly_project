import Anomaly from "../anomaly/Anomaly"
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import '../user/User.css'

export default function User (props) {

    return (
        <Card style={{ width: '18rem' }}>
            <Card.Body>
                <Card.Title>{props.userName}</Card.Title>
                <ListGroup variant="flush">
                    {props.anomalies.map(anomaly => {
                    return <Anomaly anomaly= {anomaly}/>
                    })} 
                </ListGroup>
            </Card.Body> 
        </Card >
    )
}