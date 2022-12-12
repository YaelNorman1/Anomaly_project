import React from "react";
import { Chart } from "react-google-charts";

export function ComboChart(props) {
    const data = props.data

      const options = {
        title: props.options.title,
        vAxis: { title: props.options.vAxis },
        hAxis: { title: props.options.hAxis },
        seriesType: "bars",
        series: { [data[0].length-2] : { type: "line" } },
      };

  return (
    <Chart
      chartType="ComboChart"
      width="100%"
      height="400px"
      data={data}
      options={options}
    />
  );
}
