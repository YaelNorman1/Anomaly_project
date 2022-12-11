import { Card, CardContent, Typography } from "@mui/material";
import { Col } from "react-bootstrap";

export default function Amount() {

    return(
    <Col>
        <Card  sx={{ height: '100%'}} >
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                Anomaly Appearance
                </Typography>
            </CardContent>

        </Card>
    </Col>
    )

}
