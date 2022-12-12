import { Card, CardContent, Typography } from "@mui/material";
import { Col } from "react-bootstrap";
import ArrowUpwardIcon from '@mui/icons-material/ArrowUpward';
import ArrowDownwardIcon from '@mui/icons-material/ArrowDownward';
import BorderAllIcon from '@mui/icons-material/BorderAll';

export default function Amount(props) {
    let counter = props.counter
    let numOfDepositTransactions = filterCategory(props.filteredAnomalies,"avgNumOfDeposits")
    let numOfWithdrawTransactions =filterCategory(props.filteredAnomalies,"avgNumOfWithdraws")
    let depositAmount =filterCategory(props.filteredAnomalies,"avgAmountDeposit")
    let withdrawAmount =filterCategory(props.filteredAnomalies,"avgAmountWithdraw")

    function filterCategory(filteredAnomalies,category){
        return filteredAnomalies.filter(anomaly => anomaly["category"]==category).length
    }
    return(
    <Col>
        <Card  sx={{ height: '100%'}} >
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                {counter=="amount"? <p>
                     <h3>Amount Anomalies</h3>
                     <ArrowUpwardIcon color="success"/>
                     Deposit Amount :{depositAmount}
                     <div></div>
                     <ArrowDownwardIcon color="error" />
                     Withdraw Amount: {withdrawAmount}
                    </p> : counter=="num"? <p>
                     <h3>Quantity Anomalies</h3>
                        <ArrowUpwardIcon color="success"/>
                        Num of Deposit : {numOfDepositTransactions}
                        <div></div>
                        <ArrowDownwardIcon color="error" />
                        Num Of Withdraw: {numOfWithdrawTransactions}
                    </p> :
                    <p>
                        <h3>Total</h3>
                        <BorderAllIcon color="primary"/>
                        Total Anomalies: {props.filteredAnomalies.length}
                    </p>
                }
                </Typography>
            </CardContent>

        </Card>
    </Col>
    )

}
