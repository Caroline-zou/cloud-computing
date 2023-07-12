import json
import networkx as nx
import requests
import matplotlib.pyplot as plt
import csv
import os

repo_list = ['alibaba/canal', 'alibaba/druid', 'apache/pulsar', 'aliyun/terraform-provider-alicloud', 'alibaba/ice', 'alibaba/DataX', 'alibaba/easyexcel', 'midwayjs/midway', 'alibaba/Sentinel', 'alibaba/nacos', 'alibaba/spring-cloud-alibaba', 'labring/sealos', 'alibaba/arthas', 'hypertrons/hypertrons', 'openyurtio/openyurt', 'X-lab2017/X-lab2017.github.io', 'hypertrons/hypertrons-crx', 'X-lab2017/open-digger', 'alibaba/GraphScope', 'sealerio/sealer', 'hypertrons/hypertrons-crx-website', 'ApsaraDB/PolarDB-for-PostgreSQL', 'labring/laf', 'polardb/polardbx-sql', 'X-lab2017/open-galaxy', 'alibaba/lowcode-engine', 'X-lab2017/open-research', 'X-lab2017/open-leaderboard', 'X-lab2017/open-wonderland', 'X-lab2017/open-perf', 'alibaba/fastjson2', 'OpenEduTech/EduTechResearch', 'OpenEduTech/OpenEduKG', 'X-lab2017/open-certified', 'alibaba/havenask', 'modelscope/modelscope', 'redis/redis', 'seata/seata', 'opensergo/opensergo-specification', 'opensergo/opensergo-dashboard', 'opensergo/opensergo-java-sdk', 'opensergo/opensergo-control-plane', 'opensergo/opensergo-go-sdk', 'alibaba/lowcode-code-generator-demo', 'alibaba/lowcode-materials', 'alibaba/lowcode-plugins', 'alibaba/lowcode-tools', 'alibaba/lowcode-demo', 'alibaba/lowcode-engine-ext', 'alibaba/lowcode-datasource', 'kubevela/catalog', 'kubevela/kubevela', 'fluid-cloudnative/fluid', 'kubevela/velaux', 'kubevela/kubevela.io', 'kubevela/terraform-controller', 'kubevela/velad', 'kubevela/workflow', 'kubevela/kube-trigger', 'kubevela/pkg', 'X-lab2017/od-api', 'X-lab2017/oss101', 'nacos-group/nacos-spring-project', 'nacos-group/nacos-spring-boot-project', 'nacos-group/nacos-docker', 'nacos-group/nacos-k8s', 'nacos-group/nacos-sdk-go', 'nacos-group/nacos-sdk-python', 'nacos-group/nacos-sdk-csharp', 'nacos-group/nacos-sdk-cpp', 'nacos-group/nacos-plugin', 'nacos-group/nacos-sdk-rust', 'openyurtio/yurt-edgex-manager']
print(len(repo_list))
date_list=[
  '2015-01', '2015-02', '2015-03', '2015-04', '2015-05', '2015-06', '2015-07', '2015-08', '2015-09', '2015-10',
  '2015-11', '2015-12', '2016-01', '2016-02', '2016-03', '2016-04', '2016-05', '2016-06', '2016-07', '2016-08',
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
cnt=0
for repo in repo_list:
    for date in date_list:
        print(cnt)
        cnt+=1
        G=nx.DiGraph()

        url = f'https://oss.x-lab.info/open_digger/github/{repo}/project_openrank_detail/{date}.json'
        print(url)
        try:
            response=requests.get(url)
            data=response.json()
        except:
            continue
        repo_id=None
        # print(data['nodes'])
        contributors=[]
        for node in data['nodes']:
            if node['c']=='u':
                contributors.append(node)
            elif node['c']=='r':
                repo_id=node['id']
        # print(len(contributors))
        # print(contributors)
        # print(repo_id)
        interactions=[]
        for edge in data['links']:
            if edge['s']!=repo_id and edge['t']!=repo_id:
                interactions.append(edge)
        # print(interactions)

        for contributor in contributors:
            G.add_node(contributor['id'])
        for interaction in interactions:
            G.add_edge(interaction['s'], interaction['t'])

        # 计算度中心性
        degree_centrality = nx.degree_centrality(G)

        # 计算接近中心性
        closeness_centrality = nx.closeness_centrality(G)

        # 计算介数中心性
        betweenness_centrality = nx.betweenness_centrality(G)
        data=[]
        # 打印每个贡献者的中心性指标值
        for contributor in contributors:
            # print("Contributor:", contributor['id'])
            # print("Degree Centrality:", degree_centrality[contributor['id']])
            # print("Closeness Centrality:", closeness_centrality[contributor['id']])
            # print("Betweenness Centrality:", betweenness_centrality[contributor['id']])
            # print()
            temp=[]
            temp.append(repo)
            temp.append(repo_id)
            temp.append(date)
            temp.append(contributor['id'])
            temp.append(degree_centrality[contributor['id']])
            temp.append(closeness_centrality[contributor['id']])
            temp.append(betweenness_centrality[contributor['id']])
            temp.append(contributor['i'])
            temp.append(contributor['v'])
            data.append(temp)

        # 绘制合作网络图
        # plt.figure(figsize=(10, 6))
        # pos = nx.spring_layout(G)  # 选择布局算法
        # nx.draw_networkx(G, pos, with_labels=True, node_size=200, node_color='lightblue')
        # plt.title("Collaboration Network")
        # plt.savefig("./a.png")
        # plt.show()


        csv_file = 'statistics1.csv'
        file_exists = os.path.isfile(csv_file)

        with open('./statistics1.csv','a',newline='') as file:
            writer=csv.writer(file)
            if not file_exists:
                header = ['repo_name','repo_id','date','Contributor', 'Degree_Centrality', 'Closeness_Centrality','Betweenness_Centrality','Last_Openrank','Openrank']
                writer.writerow(header)
            writer.writerows(data)
            