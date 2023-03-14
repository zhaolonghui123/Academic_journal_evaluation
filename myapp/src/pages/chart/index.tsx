import React from 'react';
import { Pie } from '@ant-design/charts';

const chart: React.FC = () => {
  var data = [
    {
      type: '分类一',
      value: 27,
    },
    {
      type: '分类二',
      value: 25,
    },
    {
      type: '分类三',
      value: 18,
    },
    {
      type: '分类四',
      value: 15,
    },
    {
      type: '分类五',
      value: 10,
    },
    {
      type: '其他',
      value: 5,
    },
  ];
  var config = {
    appendPadding: 10, //在padding的基础上额外追加的padding,控制图表相对边距，格式为数字或数组
    data: data, //数据源
    angleField: 'value',
    colorField: 'type',
    radius: 0.8, //饼图的半径, 取值0到1
    label: { //hover时标签样式
      type: 'outer',
      content: '{name} {percentage}',
    },
    interactions: [{ type: 'pie-legend-active' }, { type: 'element-active' }], // 图表交互
  };
  return <Pie {...config} />;
};

export default chart;