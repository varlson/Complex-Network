from itertools import count
from igraph import *
from utility import effGlobal, legend, pairBuilder

import numpy as np

g =0
pair = 0

def main():
    g = Graph.GRG(10, 0.5)
    g.vs['code'] = g.degree()

    return g

def pair(g):

    pair = pairBuilder(g, g.degree())
    return pair

def efficiencyRemovalFuncion(g, pair):
    effTotal = np.zeros(g.vcount()+1)
    E = effGlobal(g)
    effTotal[0] = 1.0

    # visual_style = {}
    # visual_style['vertex_color'] = 'LightBlue'#DarkCyan
    # visual_style['edge_color'] = 'Black'
    
    g.vs['label'] = [x for x in range(g.vcount())]
    gcp = g.copy()

    count =1
    
    gcp.vs['color'] = 'LightBlue'
    gcp.vs['edge_color'] = 'Black'
    
    while gcp.vcount() > 1:

        index = gcp.vs.find(code = pair[count-1][1]).index
        gcp.vs[index]['size'] = 50
        gcp.vs[index]['color'] = 'Red'
        # layout = 
        plot(gcp ,"evid/"+str(count)+'.png')
        gcp.delete_vertices(index)
        effTotal[count] = effGlobal(gcp)/E
        count+=1
    return effTotal


# efficiencyRemovalFuncion(g, pair)


import matplotlib.pylab as plt

def graphBuilder(g, removalTypes, metrics, network, folder, option=1):
    N = float(g.vcount())
    nodes = [x/N for x in range(0, g.vcount()+1)]
    plt.xlabel("nodes")
    
    removalTypes = [removalTypes] if not isinstance(removalTypes, list) else removalTypes
    metrics = [metrics] if not isinstance(metrics, list) else metrics

    for metric, removalType in zip(metrics, removalTypes):
    	R = sum(metric[1:])/len(metric)
    	R = str(R)[:5]
    	plt.plot(nodes, metric, label = removalType)
    
    plt.title("Rede de "+network)
    # plt.title("Rede de Passageiros de "+network[3:])
    plt.xlabel(r'$f$', fontsize=14)
    if option == 1:
        plt.ylabel(r'$P_\infty(f) / P_\infty(0)$', fontsize=14)
    elif option ==3:
        plt.ylabel(r'$ \parallel W \parallel(f) / \parallel W \parallel(0)$', fontsize=16)
    else:
        plt.ylabel(r'$ E (f) / E (0)$', fontsize=16)
    plt.legend()
    plt.margins(x = 0.02, y = 0.02)
    # plt.set_aspect('equal')
    makeFolder(folder)
    
    return 
    plt.savefig(folder+'/'+network+".png")
    plt.clf()


    # plt.title("Rede de "+network)
    # # plt.title("Rede de Passageiros de "+network[3:])
    # plt.xlabel(r'$f$', fontsize=14)
    # if option == 1:
    #     plt.ylabel(r'$P_\infty(f) / P_\infty(0)$', fontsize=14)
    # elif option ==3:
    #     plt.ylabel(r'$ \parallel W \parallel(f) / \parallel W \parallel(0)$', fontsize=16)
    # else:
    #     plt.ylabel(r'$ E (f) / E (0)$', fontsize=16)
    # plt.legend()
    # plt.margins(x = 0.02, y = 0.02)
    # # plt.set_aspect('equal')
    # makeFolder(folder)
    
    fig.savefig(folder+'/'+network+".png")
    # plt.clf()