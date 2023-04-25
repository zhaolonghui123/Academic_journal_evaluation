import Chart2 from './component/chart2';
import Chart3 from './component/chart3';
import { Card, Select, Space, Typography } from 'antd';
import { useState, useEffect, useCallback } from 'react';
import React from 'react';
import { journalURL } from '@/services/url';
import axios from "axios"
import Chart1 from './component/chart1';
import { ProCard } from '@ant-design/pro-components';



// const data1 = [
// ];
const Data: React.FC = () => {
  
  const [data1, setData1] = useState([]);
  const [data2, setData2] = useState([]);
  const [journalname1, setName1] = useState('中学数学月刊');
  const [journalname2, setName2] = useState('数学通报');
  const [options,SetOption] = useState([])

  const handleChange1 = (value: string) => {
    //console.log(`selected ${value}`);
    setName1(value);
  };
  const handleChange2 = (value: string) => {
    //console.log(`selected ${value}`);
    setName2(value);
  };
  

  const getOption = useCallback(()=>{
    axios.get(journalURL.getjournalnamelist)
    .then((res)=>{
      SetOption(res.data)
    });
  }, []);

  const getData1 = useCallback(()=>{
    axios.get(journalURL.getPapercount)
    .then((res)=>{
      setData1(res.data)
    });
  }, []);
  
  const getData2 = useCallback(()=>{
    axios.post(journalURL.getjournalscore+`?journalname1=${journalname1}&journalname2=${journalname2}`)
    .then((res)=>{
      setData2(res.data)
    });
  }, [journalname1, journalname2]);

  useEffect(()=>{
    getData1();
    getData2();
    getOption();
  }, [getData1, getData2, getOption])
  
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
            onChange={handleChange1}
            options={options}
          />
          <Select
            defaultValue="数学通报"
            style={{ width: 120 }}
            onChange={handleChange2}
            options={options}
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
