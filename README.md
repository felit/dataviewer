
install
---
pip install flask pymongo elasticsearch

dataviewer
依赖的技术要点

d3 highcharts react or angularjs nodejs

可实现后端存储

elasticsearch mongodb jdbc(postgresql、kylin、hive)

支持页面形式

各种图表

简介

专注于BI的数据可视化

TODO
---
实现postgresql可视化
实现多表关联
实现elasticsearch的可视化处理
每格图表添加汇总信息
添加搜索条件
日报表汇总页面添加日期
周后表汇总页面添加周的日期选项
添加布局拖拽功能
全局日期选择：日、周、月、年
表格下载按钮、汇总信息与图表的下载按钮与汇总信息放置位置不同


扩展形式
---
插件 回调

不支持内容
---
权限

概念
---
查询
配置分为三部分：数据源、适配、页面
数据源的三层抽象，增加灵活性：environment、group、datasource、query
数据模型与展现模型进行适配


TODO 特性
---
跨数据源关联 主辅数据型式
元数据可导入导出
元数据可以存储在 rdbms、es、mongodb、文件等数据源
元数据迁移
查询执行时间日志
页面直接配置数据源
其他配置选项：应用、用户、
邮件发送功能
数据导出后发送到相应的邮箱
配置信息的可视化、测试、监控
字段映射(value->title)，可配置，可导入，可查询，定期导入
多个图表

+图表与图表之间相互通信
排序，分页

roadmap
---
通过添加插件来增加数据源的支持
添加测试、验证方便开发与测试

其他非功能特性
---
数据源配置导入导出
给权限留出扩展点
灰度发布
权限与组织结构适配

License

MIT