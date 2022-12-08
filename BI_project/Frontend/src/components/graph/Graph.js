import { Card, CardContent, Typography } from "@mui/material";
import { Col } from "react-bootstrap";

export default function Graph() {

    return(
    <Col>
        <Card  sx={{ height: '100%', mt: 3 }} >
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                Graph 
                </Typography>
            </CardContent>

        </Card>
    </Col>
    )

}