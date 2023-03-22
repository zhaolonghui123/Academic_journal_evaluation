import React from 'react';
import { Divider, Typography } from 'antd';

const { Title, Paragraph, Link } = Typography;


const Welcome: React.FC = () => (
  <Typography>
    <Title>
      介绍
    </Title>
    <Paragraph>
      Academic journal evaluation 是一款期刊评价指标数据中台
    </Paragraph>
    <Paragraph>
      由于核心期刊评选的数据报告每年只更新一次，为了更好的掌握期刊影响因子，引用量，下载量等评价指标的实时数据,
      Academic journal evaluation采用爬虫等技术对相应数据进行采集,并建立自己的数据库,对具体数据进行统一管理和
      数据可视化
    </Paragraph>
    <Divider />
    <Title>
      相关技术使用
    </Title>
    <Paragraph>
      Academic journal evaluation采用<Link href="https://beta-pro.ant.design/">ant design Pro</Link>与<Link href="https://fastapi.tiangolo.com/">fastapi</Link>进行搭建
    </Paragraph>
    <Paragraph>
      Ant Design Pro 是基于 Ant Design 和 umi 的封装的一整套企业级中后台前端/设计解决方案，致力于在设计规范和基础组件
      的基础上，继续向上构建，提炼出典型模板/业务组件/配套设计资源，进一步提升企业级中后台产品设计研发过程中的『用户』和
      设计者』的体验。
    </Paragraph>
    <Paragraph>
      FastAPI是一个用于构建API的现代、快速(高性能)的web框架,使用Python 3.6+并基于标准的Python类型提示. FastAPI鼓励使用Pydantic和OpenAPI进行文档编制，使用Docker进行快速开发和部署以及基于Starlette框架进行简单测试. FastAPI提供了许多好处，例如自动OpenAPI验证和文档编制，而无需添加不必要的膨胀.
      FastAPI具有以下特点:快速:可与NodeJS和Go比肩的极高性能(归功于Starlette和Pydantic),是最快的Python web框架之一;快速编码:减少代码量,增加代码可读性;少出错:减少人为错误;直观:更易于理解和学习
    </Paragraph>
  </Typography>
);

export default Welcome;