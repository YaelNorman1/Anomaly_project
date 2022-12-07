import { ListGroup } from "react-bootstrap";
import { Button } from "react-bootstrap";
import MoreAnomalyData from "../moreAnomalyData/MoreAnomalyData";


const CATEGORIES= {
    avgNumOfWithdraws: "Number Of Withdraws"
} 


export default function Anomaly (props){

    return (
        <ListGroup.Item>
            <div><strong>category:</strong> {CATEGORIES[props.anomaly.category]}</div>
            <div><strong>quantity: </strong>{props.anomaly.quantity}</div>
            <div><strong>start date: </strong>{props.anomaly.startDate.toString()}</div>
            <div><strong>end date: </strong>{props.anomaly.endDate.toString()}</div>
            <MoreAnomalyData userId= {props.userId} category= {props.anomaly.category} quantity= {props.anomaly.quantity} userStatistic= {props.userStatistic}/>
        </ListGroup.Item>
    )

}