import Chart2 from './component/chart2';
import Chart3 from './component/chart3';
import { Card } from 'antd';
import React from 'react';
import Chart1 from './component/chart1';

const Data: React.FC = () => (
  <>
    <Card title="折线" bordered={false} >
      <Chart2/>
      <p>Card content</p>
    </Card>
    <Card title="雷达" bordered={false} >
      <Chart3/>
      <p>Card content</p>
    </Card>
    <Card title="饼图" bordered={false} >
      <Chart1/>
      <p>Card content</p>
    </Card>
  </>
);

export default Data;