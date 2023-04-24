import React, { useState,useEffect } from 'react';
import { Space, Table, Tag } from 'antd';
import axios from "axios";
import { userURL } from '@/services/url';
import type { ColumnsType } from 'antd/es/table';

interface DataType {
  username: string;
  password: string;
  isAdmin: number;
  phone: string;
  email: string; 
}

const columns: ColumnsType<DataType> = [
  {
    title: 'username',
    dataIndex: 'username',
    key: 'username',
    render: (text) => <a>{text}</a>,
  },
  {
    title: 'password',
    dataIndex: 'password',
    key: 'password',
  },
  {
    title: 'isAdmin',
    dataIndex: 'isAdmin',
    key: 'isAdmin',
  },
  {
    title: 'phone',
    dataIndex: 'phone',
    key: 'phone',
  },
  {
    title: 'email',
    dataIndex: 'email',
    key: 'email',
  },
];

const initdata: DataType[] = []

const UserManagement: React.FC = () =>{
  const [data,setData] = useState(initdata)
  useEffect(()=>{
    axios.get(userURL.getAllUser)
    .then((res)=>{
      setData(res.data)
    })
  },[])
  return  <Table columns={columns} dataSource={data} />;
}

export default UserManagement;