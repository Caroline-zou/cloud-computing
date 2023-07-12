#!/usr/bin/env python
import csv
import igraph
import pandas as pd

g = igraph.Graph()

df = pd.read_csv('repo-attributes.csv')
print(len(df))
# with open('repo-attributes.csv', 'rb') as repofile:
#     reader = csv.DictReader(repofile)
for i in range(len(df)):
    # repo=df.iloc(i)
    print(type(df['repository_language'][i]))
    g.add_vertex(name=df['repository_url'][i],
        label=df['repository_url'][i][19:],
        language='(unknown)' if df['repository_language'][i] == 'null'
            else str(df['repository_language'][i]),
        # label=str(df['repository_language'][i]),
        watchers=int(df['repository_watchers'][i]))
    # break

df1 = pd.read_csv('repo_weights.csv')
# with open('repo_weights.csv', 'rb') as edgefile:
#     reader = csv.DictReader(edgefile)
for i in range(len(df1)):
    g.add_edge(df1['repository1'][i], df1['repository2'][i],
        weight=float(df1['weight'][i]))

# print g.summary()
g.write('repositories.gml')