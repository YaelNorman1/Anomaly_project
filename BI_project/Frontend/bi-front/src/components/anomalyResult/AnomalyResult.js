// import { Container } from "react-bootstrap/lib/c";
import { Container } from "react-bootstrap";
import User from "../user/User";

function AnomalyResult(props) {

  function groupAnomaliesById(){
    const res = {}
    for(let anomaly of props.anomalies){
      if(res[anomaly.userId] === undefined){
        res[anomaly.userId] = 
        {
          userName: anomaly.userName,
          userId: anomaly.userId,
          anomalies: [],
        }
      }
      res[anomaly.userId]["anomalies"].push(anomaly);
    }
    return Object.values(res);
  }

  return (
    <Container className="AnomalyResult">
      {groupAnomaliesById().map(user => (<User user= {user}/>))}
    </Container>
  );
}

export default AnomalyResult;
