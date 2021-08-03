#-*-coding:utf-8 -*-

label_dict = {}
fin = open('user_label','r')
for line in fin:
    k = line.strip().split(' ')
    lable = 1 if k[1].startswith('over') else 0
    label_dict[k[0]] = lable
fin.close()
user_color_dict = {}
user_relation_list = []
fin = open('user_relation','r')
for line in fin:
    k = line.strip().split(' ')
    user_relation_list.append((k[0], k[1]))
    if k[0] in label_dict:
        if label_dict[k[0]]:
            color = 'red'
        else:
            color = 'blue'
    else:
        color = 'black'
    user_color_dict[k[0]] = color
    if k[1] in label_dict:
        if label_dict[k[1]]:
            color = 'red'
        else:
            color = 'blue'
    else:
        color = 'black'
    user_color_dict[k[1]] = color
fin.close()
user_list = []
colors = []
for k,v in user_color_dict.items():
    user_list.append(k)
    colors.append(v)
from matplotlib import pyplot as plt
import networkx as nx

plt.rcParams.update({
    'figure.figsize':(10,8)
})
G=nx.Graph()
G.add_nodes_from(user_list)
G.add_edges_from(user_relation_list)
nx.draw_networkx(G,node_color=colors,node_size=80)
plt.show()

