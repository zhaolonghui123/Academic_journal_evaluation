import Chart2 from './component/chart2';
import Chart3 from './component/chart3';
import { Card, Select, Space } from 'antd';
import React from 'react';
import Chart1 from './component/chart1';
const handleChange = (value: string) => {
  console.log(`selected ${value}`);
};
const data1 = [
  { year: '2016', value: 3 },
  { year: '2017', value: 4 },
  { year: '2018', value: 3.5 },
  { year: '2019', value: 5 },
  { year: '2020', value: 4.9 },
  { year: '2021', value: 6 },
  { year: '2022', value: 7 },
  { year: '2023', value: 9 },
];
const Data: React.FC = () => (
  <>
    <Card title="折线" bordered={false} >
      <Chart2 data={data1} />
      
    </Card>
    <Card title="雷达" bordered={false} >
      <Chart3/>
      <div >
        <Space align="center">
          <Select
            defaultValue="中学数学月刊"
            style={{ width: 120 }}
            onChange={handleChange}
            options={[
              { value: '中学数学月刊', label: '中学数学月刊' },
              { value: '数学教育学报', label: '数学教育学报' },
              { value: '数学通报', label: '数学通报' },
            ]}
          />
          <Select
            defaultValue="中学数学月刊"
            style={{ width: 120 }}
            onChange={handleChange}
            options={[
              { value: '中学数学月刊', label: '中学数学月刊' },
              { value: '数学教育学报', label: '数学教育学报' },
              { value: '数学通报', label: '数学通报' },
            ]}
          />
        </Space> 
      </div>
    </Card>
    <Card title="饼图" bordered={false} >
      <Chart1/>
      <p>Card content</p>
    </Card>
  </>
);

export default Data;