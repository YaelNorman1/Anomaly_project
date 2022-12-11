import { ListGroup } from "react-bootstrap";
import MoreAnomalyData from "../moreAnomalyData/MoreAnomalyData";
import '../anomaly/Anomaly.css'

const CATEGORIES= {
    avgNumOfWithdraws: "Number Of Withdraws"
} 


export default function Anomaly (props){

    return (
        <ListGroup.Item >
            <div className="anomaly-details"><strong>category:</strong> {CATEGORIES[props.anomaly.category]}</div>
            <div className="anomaly-details"><strong>quantity: </strong>{props.anomaly.quantity}</div>
            <div className="anomaly-details"><strong>start date: </strong>{props.anomaly.startDate.toString()}</div>
            <div className="anomaly-details"><strong>end date: </strong>{props.anomaly.endDate.toString()}</div>
            <MoreAnomalyData userId= {props.userId} category= {props.anomaly.category} quantity= {props.anomaly.quantity} userStatistic= {props.userStatistic}/>
        </ListGroup.Item>
    )

}