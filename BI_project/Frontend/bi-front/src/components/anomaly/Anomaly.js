import { ListGroup } from "react-bootstrap";
import { Button } from "react-bootstrap";
import MoreAnomalyData from "../moreAnomalyData/MoreAnomalyData";

export default function Anomaly (props){
    function popUpDetails(){
        console.log("fo")
    }
    
    return (
        <ListGroup.Item>
            <div>category: {props.anomaly.category}</div>
            <div>quantity: {props.anomaly.quantity}</div>
            <div>start date: {props.anomaly.startDate.toString()}</div>
            <div>end date: {props.anomaly.endDate.toString()}</div>
            <MoreAnomalyData />
        </ListGroup.Item>
    )

}