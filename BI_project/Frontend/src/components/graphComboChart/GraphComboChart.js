import { Card, CardContent, Typography } from "@mui/material";
import { Col } from "react-bootstrap";
import { ComboChart } from "../comboChart/ComboChart";
import { useState, useEffect } from 'react';

const anomalies = [
    {
       "anomalyId":1,
       "userId":"Px3ADejnL4",
       "category":"avgAmountDeposit",
       "quantity":60000,
       "startDate":"2022-12-11T15:34:52",
       "endDate":"2022-12-11T15:35:22"
    },
    {
       "anomalyId":2,
       "userId":"sjpui0UcGs",
       "category":"avgNumOfDeposits",
       "quantity":6,
       "startDate":"2022-12-11T15:35:53",
       "endDate":"2022-12-11T15:36:23"
    },
    {
       "anomalyId":3,
       "userId":"rkM2q8ZFo1",
       "category":"avgNumOfWithdraws",
       "quantity":10,
       "startDate":"2022-12-11T15:36:54",
       "endDate":"2022-12-11T15:37:24"
    },
    {
       "anomalyId":4,
       "userId":"vgqpYn8nEf",
       "category":"avgAmountWithdraw",
       "quantity":-6000,
       "startDate":"2022-12-11T15:38:25",
       "endDate":"2022-12-11T15:38:55"
    },
    {
       "anomalyId":5,
       "userId":"Px3ADejnL4",
       "category":"avgNumOfDeposits",
       "quantity":6,
       "startDate":"2022-12-11T15:42:59",
       "endDate":"2022-12-11T15:43:29"
    },
    {
       "anomalyId":6,
       "userId":"Px3ADejnL4",
       "category":"avgAmountWithdraw",
       "quantity":-15000,
       "startDate":"2022-12-11T15:44:00",
       "endDate":"2022-12-11T15:44:30"
    },
    {
       "anomalyId":7,
       "userId":"Px3ADejnL4",
       "category":"avgAmountDeposit",
       "quantity":60000,
       "startDate":"2022-11-11T15:34:52",
       "endDate":"2022-11-11T15:35:22"
    },
    {
       "anomalyId":8,
       "userId":"sjpui0UcGs",
       "category":"avgNumOfDeposits",
       "quantity":6,
       "startDate":"2022-11-11T15:35:53",
       "endDate":"2022-11-11T15:36:23"
    },
    {
       "anomalyId":9,
       "userId":"rkM2q8ZFo1",
       "category":"avgNumOfWithdraws",
       "quantity":10,
       "startDate":"2022-10-11T15:36:54",
       "endDate":"2022-10-11T15:37:24"
    },
    {
       "anomalyId":10,
       "userId":"vgqpYn8nEf",
       "category":"avgAmountWithdraw",
       "quantity":-6000,
       "startDate":"2022-09-11T15:38:25",
       "endDate":"2022-09-11T15:38:55"
    },
    {
       "anomalyId":11,
       "userId":"Px3ADejnL4",
       "category":"avgNumOfDeposits",
       "quantity":6,
       "startDate":"2022-12-11T15:42:59",
       "endDate":"2022-12-11T15:43:29"
    },
    {
       "anomalyId":12,
       "userId":"Px3ADejnL4",
       "category":"avgAmountWithdraw",
       "quantity":-15000,
       "startDate":"2022-11-11T15:44:00",
       "endDate":"2022-11-11T15:44:30"
    }
 ]

export default function GraphComboChart(props) {

    const [dateCategories, setDateCategories] = useState(getDateCategories())

    function getDateCategories(){
        const res = []

        const categories = getCategories(anomalies).sort()
        categories.push("average")
        res.push(["Month"].concat(categories))

        const AnomaliesGroupByMonthAndYear = getAnomaliesGroupByMonthAndYear(anomalies)

        for (const [key, value] of AnomaliesGroupByMonthAndYear) {

            const categoriesMap = getNumOfAnomaliesGroupByCategory(value)
            const sortedCategoriesMap = sortCategories(categoriesMap, getCategories(anomalies).sort())
            const sortedCategoriesArray = Array.from(sortedCategoriesMap.values())
            const average = sortedCategoriesArray.reduce((a, b) => a + b, 0) / sortedCategoriesArray.length;
            sortedCategoriesArray.push(average)
            const columnData = [key].concat(sortedCategoriesArray)
            res.push(columnData)
        }
        return res
    }

    function sortCategories(categoriesMap, categories){
        const res = new Map()
        for(const category of categories){
            res.set(category, categoriesMap.get(category) || 0)
        }
        return res
    }

    function getCategories(anomalies){
        let categoryNamesSet = new Set(anomalies.map(anomaly => anomaly.category));
        return Array.from(categoryNamesSet)
    }

    function getNumOfAnomaliesGroupByCategory(anomalies){
        const categoriesMap = new Map();
        for (let anomaly of anomalies) {
            let c = anomaly.category;
            categoriesMap.set(c, categoriesMap.get(c) + 1 || 1);
        }
        return categoriesMap
    }

    function getAnomaliesGroupByMonthAndYear(anomalies){
        const res = new Map()

        for(const anomaly of anomalies){
            const currentDate = new Date(anomaly.startDate)
            const year = currentDate.getFullYear()
            const month = currentDate.getMonth()
            const dateString = `${year}/${month}`
            if(res.get(dateString) == undefined){
                res.set(dateString, [anomaly])
            }
            else{
                res.get(dateString).push(anomaly)
            }
        }
        return res
    }


    const options = {
        title: "Anomalies graph",
        vAxis: "Number of anomalies",
        hAxis: "Month"
    }


    return(
    <Col>
        <Card  sx={{ height: '100%', mt: 3 }} >
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    <ComboChart data={dateCategories} options={options} />
                </Typography>
            </CardContent>
        </Card>
    </Col>
    )
}