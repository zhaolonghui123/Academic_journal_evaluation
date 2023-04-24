import React, { useState } from 'react';
import { PageContainer } from '@ant-design/pro-layout';
import { Card, Button, Modal, Form, Input } from 'antd';

interface JournalData {
  id: number;
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
    },
    {
      "id": 2,
      "主办单位": "天津师范大学 中国教育学会",
      "主编": "王梓坤",
      "出版周期": "双月刊",
      "国际刊号": "1004-9894",
      "国内刊号": "12-1194/G4",
      "影响因子": "3.39",
      "文献量": "2865",
      "被引量": "69312",
      "下载量": "321514",
      "基金论文量": "1807",
      "电话": "022-23766679",
      "地址": "天津市西青区宾水西道393号天津师大129信箱"
    },
    {
      "id": 3,
      "主办单位": "中国数学会 北京师范大学",
      "主编": "保继光",
      "出版周期": "月刊",
      "国际刊号": "0583-1458",
      "国内刊号": "11-2254/O1",
      "影响因子": "1.23",
      "文献量": "5275",
      "被引量": "29410",
      "下载量": "410866",
      "基金论文量": "631",
      "电话": "010-58807753",
      "地址": "北京市师范大学"
    },
    {
      "id": 4,
      "主办单位": "陕西师范大学",
      "主编": "石生民",
      "出版周期": "旬刊",
      "国际刊号": "1002-2171",
      "国内刊号": "61-1032/G4",
      "影响因子": "1.14",
      "文献量": "2980",
      "被引量": "3052",
      "下载量": "986",
      "基金论文量": "651",
      "电话": "029-85308154",
      "地址": "陕西师范大学校内"
    }
  ]);

  // 控制表单的可见性
  const [visible, setVisible] = useState(false);

  // 存储表单数据的状态值
  const [formData, setFormData] = useState<JournalData>({
    id: data.length + 1,
    主办单位: '',
    主编: '',
    出版周期: '',
    国际刊号: '',
    国内刊号: '',
    影响因子: '',
    文献量: '',
    被引量: '',
    下载量: '',
    基金论文量: '',
    电话: '',
    地址: '',
  });

  // 处理表单提交事件
  const handleOk = () => {
    setData([...data, formData]);
    setVisible(false);
  };

  // 渲染列表项
  const renderItem = (item: JournalData) => {
    return (
      <Card key={item.id} style={{ marginBottom: '16px' }}>
        <Card.Meta title={item['主办单位']} description={item['主编']} />
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
          <Form.Item label="主办单位" name="主办单位" rules={[{ required: true }]}>
            <Input onChange={(e) => setFormData({ ...formData, 主办单位: e.target.value })} />
          </Form.Item>
          <Form.Item label="主编" name="主编" rules={[{ required: true }]}>
            <Input onChange={(e) => setFormData({ ...formData, 主编: e.target.value })} />
          </Form.Item>
          <Form.Item label="出版周期" name="出版周期" rules={[{ required: true }]}>
            <Input onChange={(e) => setFormData({ ...formData, 出版周期: e.target.value })} />
          </Form.Item>
          <Form.Item label="国际刊号" name="国际刊号" rules={[{ required: true }]}>
            <Input onChange={(e) => setFormData({ ...formData, 国际刊号: e.target.value })} />
          </Form.Item>
          <Form.Item label="国内刊号" name="国内刊号" rules={[{ required: true }]}>
            <Input onChange={(e) => setFormData({ ...formData, 国内刊号: e.target.value })} />
          </Form.Item>
          <Form.Item label="影响因子" name="影响因子" rules={[{ required: true }]}>
            <Input onChange={(e) => setFormData({ ...formData, 影响因子: e.target.value })} />
          </Form.Item>
          <Form.Item label="文献量" name="文献量" rules={[{ required: true }]}>
            <Input onChange={(e) => setFormData({ ...formData, 文献量: e.target.value })} />
          </Form.Item>
          <Form.Item label="被引量" name="被引量" rules={[{ required: true }]}>
            <Input onChange={(e) => setFormData({ ...formData, 被引量: e.target.value })} />
          </Form.Item>
          <Form.Item label="下载量" name="下载量" rules={[{ required: true }]}>
            <Input onChange={(e) => setFormData({ ...formData, 下载量: e.target.value })} />
          </Form.Item>
          <Form.Item label="基金论文量" name="基金论文量" rules={[{ required: true }]}>
            <Input onChange={(e) => setFormData({ ...formData, 基金论文量: e.target.value })} />
          </Form.Item>
          <Form.Item label="电话" name="电话">
            <Input onChange={(e) => setFormData({ ...formData, 电话: e.target.value })} />
          </Form.Item>
          <Form.Item label="地址" name="地址">
            <Input onChange={(e) => setFormData({ ...formData, 地址: e.target.value })} />
          </Form.Item>
        </Form>
      </Modal>
    </PageContainer>
  );
};

export default JournalList;