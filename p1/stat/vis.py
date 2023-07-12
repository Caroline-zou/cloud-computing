import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Parallel
from pyecharts import options as opts
from pyecharts.charts import Page, Parallel
from pyecharts.globals import ThemeType
import random

repo_list = ['alibaba/canal', 'alibaba/druid', 'apache/pulsar', 'aliyun/terraform-provider-alicloud', 'alibaba/ice', 'alibaba/DataX', 'alibaba/easyexcel', 'midwayjs/midway', 'alibaba/Sentinel', 'alibaba/nacos', 'alibaba/spring-cloud-alibaba', 'labring/sealos', 'alibaba/arthas', 'hypertrons/hypertrons', 'openyurtio/openyurt', 'X-lab2017/X-lab2017.github.io', 'hypertrons/hypertrons-crx', 'X-lab2017/open-digger', 'alibaba/GraphScope', 'sealerio/sealer', 'hypertrons/hypertrons-crx-website', 'ApsaraDB/PolarDB-for-PostgreSQL', 'labring/laf', 'polardb/polardbx-sql', 'X-lab2017/open-galaxy', 'alibaba/lowcode-engine', 'X-lab2017/open-research', 'X-lab2017/open-leaderboard', 'X-lab2017/open-wonderland', 'X-lab2017/open-perf', 'alibaba/fastjson2', 'OpenEduTech/EduTechResearch', 'OpenEduTech/OpenEduKG', 'X-lab2017/open-certified', 'alibaba/havenask', 'modelscope/modelscope', 'redis/redis', 'seata/seata', 'opensergo/opensergo-specification', 'opensergo/opensergo-dashboard', 'opensergo/opensergo-java-sdk', 'opensergo/opensergo-control-plane', 'opensergo/opensergo-go-sdk', 'alibaba/lowcode-code-generator-demo', 'alibaba/lowcode-materials', 'alibaba/lowcode-plugins', 'alibaba/lowcode-tools', 'alibaba/lowcode-demo', 'alibaba/lowcode-engine-ext', 'alibaba/lowcode-datasource', 'kubevela/catalog', 'kubevela/kubevela', 'fluid-cloudnative/fluid', 'kubevela/velaux', 'kubevela/kubevela.io', 'kubevela/terraform-controller', 'kubevela/velad', 'kubevela/workflow', 'kubevela/kube-trigger', 'kubevela/pkg', 'X-lab2017/od-api', 'X-lab2017/oss101', 'nacos-group/nacos-spring-project', 'nacos-group/nacos-spring-boot-project', 'nacos-group/nacos-docker', 'nacos-group/nacos-k8s', 'nacos-group/nacos-sdk-go', 'nacos-group/nacos-sdk-python', 'nacos-group/nacos-sdk-csharp', 'nacos-group/nacos-sdk-cpp', 'nacos-group/nacos-plugin', 'nacos-group/nacos-sdk-rust', 'openyurtio/yurt-edgex-manager']
cnt=0
for repo in repo_list:

    # 读取CSV文件数据
    df = pd.read_csv('./statistics1.csv')
    selected_rows = df[df['repo_name'] == repo]
    # selected_rows = selected_rows[selected_rows['date'].isin(['2015-01', '2015-02', '2015-03', '2015-04', '2015-05', '2015-06', '2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12'])]

    # 获取要绘制的维度和数据
    dimensions = ['date','Contributor','Degree_Centrality', 'Closeness_Centrality', 'Betweenness_Centrality', 'Last_Openrank','Openrank']
    data = selected_rows[dimensions].values.tolist()
    user_ids = selected_rows['Contributor'].unique().tolist()
    parallel = Parallel(init_opts=opts.InitOpts(width="1700px",
                                    height="1000px"))
    for user_id in user_ids:
        # 根据用户ID筛选数据
        color1 = f'rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 0.7)'
        user_data = [d for d in data if d[1] == user_id]
        # 添加线条并指定颜色
        parallel.add(str(user_id), user_data, itemstyle_opts=opts.ItemStyleOpts(color=color1))
    # 设置图表的其他属性
    parallel.set_global_opts(
        title_opts=opts.TitleOpts(title="Parallel Coordinates Chart"),
        graphic_opts=[
            opts.GraphicGroup(
                graphic_item=opts.GraphicItem(
                    left="10000%",  # 左边距
                    top="5000%",  # 上边距
                    # right="50%",  # 右边距
                    # bottom="50%",  # 底边距
                )
            )
        ],
        legend_opts=opts.LegendOpts(
                is_show = True,
                type_ = 'scroll',
                selected_mode = True,
                pos_left = 'left',
                pos_right = None,
                pos_top = 'bottom',
                pos_bottom = None,
                orient = 'horizontal',
                align = None,
                padding = 5,
                item_gap = 10,
                item_width = 25,
                item_height = 14,        
                textstyle_opts = None,
                legend_icon ='roundRect',
                        
                )
                
    )
    parallel.add_schema(
            [opts.ParallelAxisOpts(
                    dim=0,
                    name="date",
                    type_="category",
                    data=[
                            '2015-01', '2015-02', '2015-03', '2015-04', '2015-05', '2015-06', '2015-07', '2015-08', '2015-09', '2015-10',
                            '2015-11', '2015-12',
                            '2016-01', '2016-02', '2016-03', '2016-04', '2016-05', '2016-06', '2016-07', '2016-08',
                            '2016-09', '2016-10', '2016-11', '2016-12', '2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06',
                            '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12', '2018-01', '2018-02', '2018-03', '2018-04',
                            '2018-05', '2018-06', '2018-07', '2018-08', '2018-09', '2018-10', '2018-11', '2018-12', '2019-01', '2019-02',
                            '2019-03', '2019-04', '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10', '2019-11', '2019-12',
                            '2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10',
                            '2020-11', '2020-12', '2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06', '2021-07', '2021-08',
                            '2021-09', '2021-10', '2021-11', '2021-12', '2022-01', '2022-02', '2022-03', '2022-04', '2022-05', '2022-06',
                            '2022-07', '2022-08', '2022-09', '2022-10', '2022-11', '2022-12', '2023-01', '2023-02', '2023-03', '2023-04',
                            '2023-05'
                        ]
                ),
                opts.ParallelAxisOpts(dim=1, name="Contributor"),
                opts.ParallelAxisOpts(dim=2, name="Degree_Centrality"),
                opts.ParallelAxisOpts(dim=3, name="Closeness_Centrality"),
                opts.ParallelAxisOpts(dim=4, name="Betweenness_Centrality"),
                opts.ParallelAxisOpts(dim=5, name="Last_Openrank"),
                opts.ParallelAxisOpts(dim=6, name="Openrank"),
                
            ]
        )

    # 渲染并保存图表
    name = repo.split("/")
    html_name = './parallel_html'+name[1]+'_parallel_coordinates.html'
    parallel.render(html_name)
    print(cnt)
    cnt+=1
