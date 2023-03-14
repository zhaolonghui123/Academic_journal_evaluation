import { DefaultFooter } from '@ant-design/pro-components';

const Footer: React.FC = () => {

  return (
    <DefaultFooter
      copyright={'苏州大学数学科学学院'}
      links={[
        {
          key: 'lhzhao',
          title: 'zhaolonghui',
          href: 'https://zhaolonghui123.github.io/',
          blankTarget: true,
        },
        {
          key: '苏州大学数学科学学院',
          title: '苏州大学数学科学学院',
          href: 'https://ant.design',
          blankTarget: true,
        },
      ]}
    />
  );
};

export default Footer;
