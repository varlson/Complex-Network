from graphBuilder import graphBuilder
from metricExtractor import extractor
from igraph import *

def main(g):
    metrics  = extractor(g, 1)
    graphBuilder(g, metrics[1], metrics[0], 'net', 'anac/terrestrial/GiantComponent', 1)

    metrics  = extractor(g, 2)
    graphBuilder(g, metrics[1], metrics[0], 'net1', 'anac/terrestrial/Effienciy', 2)

    metrics  = extractor(g, 3)
    graphBuilder(g, metrics[1], metrics[0], 'net2', 'anac/terrestrial/TotalFlow', 3)


g = Graph.Read_GraphML('anac/terrestrial.GraphML')

main(g)