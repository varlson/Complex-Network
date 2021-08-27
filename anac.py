from randonCorres import*
# from graphBuilder import graphBuilder
# from metricExtractor import extractor


def main(g, folder):

    randon_main(g.copy(), folder+'/randon')    
    metrics  = extractor(g, 1)
    graphBuilder(g, metrics[1], metrics[0], 'GiantComponent', folder, 1)

    metrics  = extractor(g, 2)
    graphBuilder(g, metrics[1], metrics[0], 'Effienciy', folder, 2)

    metrics  = extractor(g, 3)
    graphBuilder(g, metrics[1], metrics[0], 'TotalFlow', folder, 3)


# g = Graph.Read_GraphML('rmsp.GraphML')

from netGenerator import _main
g = _main('pas2010')
main(g, 'ibge')