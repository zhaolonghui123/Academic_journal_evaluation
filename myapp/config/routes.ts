export default [
  {
    path: '/user',
    layout: false,
    routes: [
      {
        name: 'login',
        path: '/user/login',
        component: './user/Login',
      },
      {
        component: './404',
      },
    ],
  },
  {
    path: '/welcome',
    name: 'welcome',
    icon: 'smile',
    component: './Welcome',
  },
  {
    path: '/admin',
    name: 'admin',
    icon: 'crown',
    access: 'canAdmin',
    routes: [
      // {
      //   path: '/admin/UserManagemnt',
      //   name: 'UserManagemnt',
      //   icon: 'smile',
      //   component: './UserManagemnt',
      // },
      {
        path: '/admin/UserManagement',
        name: 'UserManagement',
        component: './UserManagement',
      },
      {
        path: '/admin/OperatingRecord',
        name: 'OperatingRecord',
        component: './OperatingRecord',
      },
      {
        component: './404',
      },
    ],
  },
  {
    name: 'Data',
    path: '/Data',
    icon: 'AreaChartOutlined',
    component: './Data',
  },
  // {
  //   name: 'DataManagement',
  //   path: '/DataManagement',
  //   //icon: 'FundTwoTone',
  //   rount:[
  //     {
  //       path: '/DataManagement/Data',
  //       name: 'Data',
  //       component: '/DataManagement/Data',
  //     },
  //     {
  //       component: '/404',
  //     },
  //   ]
  // },
  {
    name: 'list.table-list',
    icon: 'table',
    path: '/list',
    component: './TableList',
  },
  {
    path: '/',
    redirect: '/welcome',
  },
  {
    component: './404',
  },
];
