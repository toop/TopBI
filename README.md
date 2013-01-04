项目名称：TopBI
----------------

项目简介：
---------
商业智能分析系统：动态报表、固定报表、个性化报表、多维报表、仪表盘、业务分析、KPI、数据挖掘、营销决策。

前期只做展示部分（不考虑数据仓库和ETL部分），以平台+模块的模式开发，模块即插即用。

功能描述：OLAP部分通过配置数据源，从数据仓库读取表结构保存到postgresql数据库，然后在线设置cubes、维度、度量值、粒度和聚合，通过pyparser解析MDX查询cubes生成数据，数据由highcharts进行互动式展示，数据可以导出为：png，pdf，execl，csv

后期：业务分析、KPI、数据挖掘、营销决策及机器学习

QQ群：285504816

模块说明：
---------
Olap模块：联机分析，（定义数据源、定义schema、定义维度、定义度量值、定义粒度）通过用户自配置cubes满足分析需要
业务分析：经营分析
KPI：
DM：数据挖掘
营销决策：通过分析，提供营销决策支持
机器学习：根据历史数据进行机器学习训练

应用说明：
---------
1、假设已经建立数据仓库
2、对企业数据按照需要进行汇总（比如按照分公司、时间、地区、产品线），并以数字或者图表展示，同时能看到明细
3、对企业数据进行同比（去年同时间段的数据对比）
4、让用户根据需要自己增加分析模型：毛利、产品线、库存、滞销、库存占用、坪效、资金.......
5、数据结果可以导出为：png，pdf，execl，csv格式
6、支持 RDBMS 连接



架构：
------
python web framework（讨论后选型）+sqlalchemy+postgresql+mako+jquery+highcharts+gevent或者asyncoro+Bootstrap
 * -env:python 2.7.3
 * -server：gevent或者asyncoro
 * -charts：highcharts
 * -ORM：sqlalchemy
 * -template：mako、wheezy.templates、pytenjin、jinja2
 * -database：postgresql
 * -python web framework：wheezy.web（推荐），tornado，werkzeug
 * -ui：jquery + Bootstrap


文件夹：
---------
 * -静态文件: static
 * -模版: templates
 * -模块: models
 * -视图: views


 
