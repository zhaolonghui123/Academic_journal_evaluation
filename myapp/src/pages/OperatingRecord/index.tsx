import React, { useState, useEffect } from 'react';
import { PageContainer } from '@ant-design/pro-layout';
import { Card, Button, Modal, Form, Input } from 'antd';
import { journalURL } from '@/services/url';
import axios from 'axios';

interface JournalData {
  id: number;
  期刊名称: string;
  主办单位: string;
  主编: string;
  出版周期: string;
  国际刊号: string;
  国内刊号: string;
  影响因子: string;
  文献量: string;
  被引量: string;
  下载量: string;
  基金论文量: string;
  电话: string;
  地址: string;
}

const JournalList: React.FC = () => {
  // 初始化数据
  const [data, setData] = useState<JournalData[]>([
    {
      "id": 1,
      "期刊名称": "中学数学月刊",
      "主办单位": "苏州大学",
      "主编": "徐稼红",
      "出版周期": "月刊",
      "国际刊号": "1004-1176",
      "国内刊号": "32-1444/O1",
      "影响因子": "0.37",
      "文献量": "6070",
      "被引量": "7085",
      "下载量": "183966",
      "基金论文量": "596",
      "电话": "0512-65112618",
      "地址": "江苏省苏州市十梓街1号苏州大学"
    }
  ]);

  // 控制表单的可见性
  const [visible, setVisible] = useState(false);

  // 存储表单数据的状态值
  const [formData, setFormData] = useState({
    journalname:''
  });

  // 处理表单提交事件
  const handleOk = () => {
    console.log(formData);
    axios.post(journalURL.createjournal+`?journalname=${formData.journalname}`)
    .then((res)=>{
      console.log(res.data)
    })
    setVisible(false);
  };


  useEffect(()=>{
    axios.get(journalURL.getjournal)
    .then((res)=>{
      setData(res.data)
    })
  },[])
  // 渲染列表项
  const renderItem = (item: JournalData) => {
    return (
      <Card key={item.id} style={{ marginBottom: '16px'  }}>
        <Card.Meta title={item['期刊名称']} style={{ padding: '10px'}}/>
        <div>主办单位：{item['主办单位']}</div>
        <div>主编：{item['主编']}</div>
        <div>出版周期：{item['出版周期']}</div>
        <div>国际刊号：{item['国际刊号']}</div>
        <div>国内刊号：{item['国内刊号']}</div>
        <div>影响因子：{item['影响因子']}</div>
        <div>文献量：{item['文献量']}</div>
        <div>被引量：{item['被引量']}</div>
        <div>下载量：{item['下载量']}</div>
        <div>基金论文量：{item['基金论文量']}</div>
        <div>电话：{item['电话']}</div>
        <div>地址：{item['地址']}</div>
      </Card>
    );
  };

  return (
    <PageContainer>
      <div style={{ marginBottom: '24px' }}>
        <Button type="primary" onClick={() => setVisible(true)}>创建新 Card</Button>
      </div>

      {data.map(renderItem)}

      <Modal
        title="创建新 Card"
        visible={visible}
        onCancel={() => setVisible(false)}
        onOk={handleOk}
      >
        <Form
          labelCol={{ span: 6 }}
          wrapperCol={{ span: 18 }}
          initialValues={{ remember: true }}
          onFinish={handleOk}
        >
          <Form.Item label="期刊名称" name="期刊名称" rules={[{ required: true }]}>
            <Input onChange={(e) => setFormData({ ...formData, journalname:e.target.value })} />
          </Form.Item>
        </Form>
      </Modal>
    </PageContainer>
  );
};

export default JournalList;