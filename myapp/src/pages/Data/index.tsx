import Chart2 from './component/chart2';
import Chart3 from './component/chart3';
import { Card, Select, Space, Typography } from 'antd';
import { useState, useEffect, useCallback } from 'react';
import React from 'react';
import { citationURL, journalURL } from '@/services/url';
import axios from "axios"
import Chart1 from './component/chart1';
import { ProCard } from '@ant-design/pro-components';



// const data1 = [
// ];
const Data: React.FC = () => {
  
  const [avgCiteCount, setAvgCiteCount] = useState([]);
  const [twoYearsCitation, setTwoYearsCitation] = useState([]);
  const [citeCount, setCiteCount] = useState([]);
  const [impactFactor, setImpactFactor] = useState([]);
  const [data2, setData2] = useState([]);
  const [docCount, setDocCount] = useState([]);
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

  const getCiteCount = useCallback(()=>{
    axios.get(citationURL.getCiteCount)
    .then((res)=>{
      setCiteCount(res.data)
    });
  }, []);

  const getAvgCiteCount = useCallback(()=>{
    axios.get(citationURL.getAvgCiteCount)
    .then((res)=>{
      setAvgCiteCount(res.data)
    });
  }, []);

  const getTwoYearsCitation = useCallback(()=>{
    axios.get(citationURL.getTwoYearsCitation)
    .then((res)=>{
      setTwoYearsCitation(res.data)
    });
  }, []);

  const getIF = useCallback(()=>{
    axios.get(citationURL.getIF)
    .then((res)=>{
      setImpactFactor(res.data)
    });
  }, []);

  const getDocCount = useCallback(()=>{
    axios.get(citationURL.getDocCount)
    .then((res)=>{
      setDocCount(res.data)
    });
  }, []);
  
  const getData2 = useCallback(()=>{
    axios.post(journalURL.getjournalscore+`?journalname1=${journalname1}&journalname2=${journalname2}`)
    .then((res)=>{
      setData2(res.data)
    });
  }, [journalname1, journalname2]);

  useEffect(()=>{
    getAvgCiteCount();
    getTwoYearsCitation();
    getCiteCount();
    getData2();
    getOption();
    getDocCount();
    getIF();
  }, [getCiteCount, getData2, getOption, getDocCount, getIF, getTwoYearsCitation, getAvgCiteCount])
  
  return (<>
    <ProCard
      tabs={{
        type: 'card',
      }}
    >
      <ProCard.TabPane key="tab1" tab="被引量" style={{ padding: '20px',borderRadius: '5px',  border: '1px solid #ccc'}}>
          <Chart2 data={citeCount} />
      </ProCard.TabPane>
      <ProCard.TabPane key="tab2" tab="发文量" style={{ padding: '20px',borderRadius: '5px',  border: '1px solid #ccc'}}>
          <Chart2 data={docCount} />
      </ProCard.TabPane>
      <ProCard.TabPane key="tab3" tab="影响因子" style={{ padding: '20px',borderRadius: '5px',  border: '1px solid #ccc'}}>
          <Chart2 data={impactFactor} />
      </ProCard.TabPane>
      <ProCard.TabPane key="tab4" tab="平均被引量" style={{ padding: '20px',borderRadius: '5px',  border: '1px solid #ccc'}}>
          <Chart2 data={avgCiteCount} />
      </ProCard.TabPane>
      <ProCard.TabPane key="tab" tab="前两年发文在本年的引用量" style={{ padding: '20px',borderRadius: '5px',  border: '1px solid #ccc'}}>
          <Chart2 data={twoYearsCitation} />
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
