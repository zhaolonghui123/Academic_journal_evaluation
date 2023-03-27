import Chart2 from './component/chart2';
import Chart3 from './component/chart3';
import { Card, Select, Space } from 'antd';
import { useState,useEffect } from 'react';
import React from 'react';
import { journalURL } from '@/services/url';
import axios from "axios"
import Chart1 from './component/chart1';
const handleChange = (value: string) => {
  console.log(`selected ${value}`);
};
// const data1 = [
// ];
const Data: React.FC = () => {
  const [data1,SetData1] = useState([])
  useEffect(()=>{
    axios.get(journalURL.getOnePapercount+"?journalname="+"中学数学月刊")
    .then((res)=>{
      SetData1(res.data)
    })
  })
  
  return (<>
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
  </>)
}


export default Data;