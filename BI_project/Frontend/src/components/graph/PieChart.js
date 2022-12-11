import React from "react";
import { Chart } from "react-google-charts";
import { Card, CardContent, Typography } from "@mui/material";
import { Col } from "react-bootstrap";

export default function App(props) {
  return (
    <Col>
      <Card sx={{ height: "100%", mt: 3 }}>
        <CardContent>
          <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
            <Chart
              chartType="PieChart"
              data={props.data}
              width={"100%"}
              height={"400px"}
            />
          </Typography>
        </CardContent>
      </Card>
    </Col>
  );
}
