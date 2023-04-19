import Chart2 from './component/chart2';
import Chart3 from './component/chart3';
import { Card, Select, Space, Typography } from 'antd';
import { useState,useEffect } from 'react';
import React from 'react';
import { journalURL } from '@/services/url';
import axios from "axios"
import Chart1 from './component/chart1';
import { ProCard } from '@ant-design/pro-components';
const handleChange = (value: string) => {
  console.log(`selected ${value}`);
};
// const data1 = [
// ];
const Data: React.FC = () => {
  
  const [data1,SetData1] = useState([])
  const [data2,SetData2] = useState([])
  useEffect(()=>{
    axios.get(journalURL.getPapercount)
    .then((res)=>{
      SetData1(res.data)
    });
    axios.get(journalURL.gettest)
    .then((res)=>{
      SetData2(res.data)
    });
  },[])
  
  return (<>
    <ProCard
      tabs={{
        type: 'card',
      }}
    >
      <ProCard.TabPane key="tab1" tab="引用量" style={{ padding: '20px',borderRadius: '5px',  border: '1px solid #ccc'}}>
          <Chart2 data={data1} />
      </ProCard.TabPane>
      <ProCard.TabPane key="tab2" tab="被摘量" style={{ padding: '20px',borderRadius: '5px',  border: '1px solid #ccc'}}>
          <Chart2 data={data1} />
      </ProCard.TabPane>
      <ProCard.TabPane key="tab3" tab="影响因子" style={{ padding: '20px',borderRadius: '5px',  border: '1px solid #ccc'}}>
          <Chart2 data={data1} />
      </ProCard.TabPane>
      <ProCard.TabPane key="tab4" tab="H指数" style={{ padding: '20px',borderRadius: '5px',  border: '1px solid #ccc'}}>
          <Chart2 data={data1} />
      </ProCard.TabPane>
    </ProCard>
    
    <Card title="雷达" bordered={false} >
      <Chart3 data={data2}/>
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
    <Card>
      <Typography.Link href="http://127.0.0.1:8080/api/journal/pdf/影响因子年报2021" target="_blank">原文</Typography.Link>
    </Card>
  </>)
}


export default Data;