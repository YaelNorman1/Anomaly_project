import { Button } from "react-bootstrap/lib/InputGroup";

export default function Anomaly (props){
    // popUpDetails(){

    // }

    return (
        <ListGroup.Item>
            {props.anomaly}
            <Button onClick={popUpDetails}>Details</Button>
        </ListGroup.Item>
    )

}