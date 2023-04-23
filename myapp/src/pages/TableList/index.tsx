import { Table, Input, Typography } from 'antd';
import { SearchOutlined } from '@ant-design/icons';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { journalURL } from '@/services/url';

interface RowData {
  id: number;
  paperName: string;
  authors: string[];
  journalname: string;
  publishTime: string;
  downloads: number;
}

const datatest: RowData[] = [
  {
    id: 1,
    paperName: '影响因子年报2021',
    authors: ['作者1', '作者2'],
    journalname: '中学数学月刊',
    publishTime: '2022-01-01',
    downloads: 100,
  }
];

const TableList: React.FC = () => {
  const [searchText, setSearchText] = useState('');
  const [data,setdata] = useState(datatest)
  const handleSearch = (value: string) => {
    setSearchText(value);
  };

  const columns = [
    {
      title: '论文名',
      dataIndex: 'paperName',
      key: 'paperName',
      filterDropdown: ({
        setSelectedKeys,
        selectedKeys,
        confirm,
        clearFilters,
      }: {
        setSelectedKeys: any;
        selectedKeys: any;
        confirm: any;
        clearFilters: any;
      }) => (
        <div style={{ padding: 8 }}>
          <Input
            placeholder="搜索论文名"
            value={selectedKeys[0]}
            onChange={(e) =>
              setSelectedKeys(e.target.value ? [e.target.value] : [])
            }
            onPressEnter={() => confirm()}
            style={{ marginBottom: 8, display: 'block' }}
          />
          <button onClick={() => clearFilters()}>重置</button>
          <button onClick={() => confirm()}>搜索</button>
        </div>
      ),
      onFilter: (value: string | number | boolean | undefined, record: RowData) =>
        record.paperName.toLowerCase().includes(String(value).toLowerCase()),
    },
    {
      title: '作者',
      dataIndex: 'authors',
      key: 'authors',
      filterDropdown: ({
        setSelectedKeys,
        selectedKeys,
        confirm,
        clearFilters,
      }: {
        setSelectedKeys: any;
        selectedKeys: any;
        confirm: any;
        clearFilters: any;
      }) => (
        <div style={{ padding: 8 }}>
          <Input
            placeholder="搜索作者"
            value={selectedKeys[0]}
            onChange={(e) =>
              setSelectedKeys(e.target.value ? [e.target.value] : [])
            }
            onPressEnter={() => confirm()}
            style={{ marginBottom: 8, display: 'block' }}
          />
          <button onClick={() => clearFilters()}>重置</button>
          <button onClick={() => confirm()}>搜索</button>
        </div>
      ),
      onFilter: (value: string | number | boolean | undefined, record: RowData) =>
        record.authors.some((author) =>
          author.toLowerCase().includes(String(value).toLowerCase())
        ),
    },
    {
      title: '发表时间',
      dataIndex: 'publishTime',
      key: 'publishTime',
      sorter: (a: RowData, b: RowData) =>
      Date.parse(a.publishTime.replace('年', '/').replace('期', '/1')) - Date.parse(b.publishTime.replace('年', '/').replace('期', '/1')),
    },
    {
      title: '发表期刊',
      dataIndex: 'journalname',
      key: 'journalname',
      filterDropdown: ({
        setSelectedKeys,
        selectedKeys,
        confirm,
        clearFilters,
      }: {
        setSelectedKeys: any;
        selectedKeys: any;
        confirm: any;
        clearFilters: any;
      }) => (
        <div style={{ padding: 8 }}>
          <Input
            placeholder="搜索期刊名"
            value={selectedKeys[0]}
            onChange={(e) =>
              setSelectedKeys(e.target.value ? [e.target.value] : [])
            }
            onPressEnter={() => confirm()}
            style={{ marginBottom: 8, display: 'block' }}
          />
          <button onClick={() => clearFilters()}>重置</button>
          <button onClick={() => confirm()}>搜索</button>
        </div>
      ),
      onFilter: (value: string | number | boolean | undefined, record: RowData) =>
        record.paperName.toLowerCase().includes(String(value).toLowerCase()),
    },
    {
      title: '下载量',
      dataIndex: 'downloads',
      key: 'downloads',
    },
    {
      title: '操作',
      key: 'action',
      render: (text: string, record: RowData) => (
        <Typography.Link href={`http://127.0.0.1:8080/api/journal/pdf/${record.paperName}`} target="_blank">原文</Typography.Link>
      ),
    },
  ];

  const onSearchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    handleSearch(e.target.value);
  };
  useEffect(()=>{
    axios.get(journalURL.getjournalInfo)
    .then((res)=>{
      setdata(res.data)
    });
  },[])
  const filteredData = data.filter(
    (record) =>
      searchText === '' ||
      record.paperName.toLowerCase().includes(searchText.toLowerCase()) ||
      record.authors.some((author) =>
        author.toLowerCase().includes(searchText.toLowerCase())
      )
  );

  return (
    <div>
      <Input
        placeholder="搜索论文名或作者"
        onChange={onSearchChange}
        prefix={<SearchOutlined />}
        style={{ width: 200, marginBottom: 20 }}
      />
      <Table dataSource={filteredData} columns={columns} />
    </div>
  );
};

export default TableList;
