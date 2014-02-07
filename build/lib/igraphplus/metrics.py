# -*- coding: utf-8 -*-

"""
igraphplus.metrics
~~~~~~~~~~~~~~~~~

This module contains the metrics for graphs.
"""


def efficiency(g, initial=0, removed=0):
    """Efficiency calculation"""
    result = 0.0
    paths = g.shortest_paths()
    if g.is_directed():
        for path in paths:
            for distance in path:
                if 0 < distance < float('Inf'):
                    result += float(1) / distance
    else:
        for index, path in enumerate(paths):
            for distance in path[index + 1:]:
                if 0 < distance < float('Inf'):
                    result += float(2) / distance

    n = g.vcount()
    if initial:
        n = initial
    if removed:
        n -= removed

    result /= n * (n - 1)
    return result


def degree_distribution(g):
    """ bin = [min_i, max_i, amount)"""
    distribution = {}
    for b in g.degree_distribution().bins():
        if b[2]:
            distribution[b[0]] = b[2]
    return distribution


def degree_distribution_plot(g, filename='degree_distribution', loglog=True, marker='.'):
    import pylab

    f = degree_distribution(g)
    if loglog:
        pylab.xscale('log')
        pylab.yscale('log')
    pylab.xlabel('k')
    pylab.ylabel('N')
    pylab.title('Degree distribution')
    pylab.plot(f.keys(), f.values(), marker)
    pylab.savefig(filename + '.png')


def degree_properties(g):
    """ Response with min, max, average degree and it's std"""
    import numpy

    degrees = numpy.array(g.degree())
    min_degree = degrees.min()
    max_degree = degrees.max()
    mean_degree = degrees.mean()
    std_degree = degrees.std()
    return min_degree, max_degree, mean_degree, std_degree


def summary(g):
    degree_stats = degree_properties(g)
    connected = 'connected' if (g.is_connected()) else 'unconnected'
    directed = 'directed' if (g.is_directed()) else 'undirected'
    deg = '(%d, %0.2f ± %0.2f, %d)' % (degree_stats[0], degree_stats[2], degree_stats[3], degree_stats[1])
    return 'N:%d E:%d %s %s Components:%d Degree:%s' % (
        g.vcount(), g.ecount(), connected, directed, len(g.components()), deg)


def report(g):
    degree_stats = degree_properties(g)
    print 'Graph is: %s, %s' % \
          ('Connected' if (g.is_connected()) else 'Disconnected', 'Directed' if (g.is_directed()) else 'Undirected')
    print 'Number of nodes: %d' % g.vcount()
    print 'Number of edges: %d' % g.ecount()
    print 'Number of components: %d' % len(g.components())
    print 'Degree: min = %d, max = %d, mean = %0.2f, std = %0.2f' % (
        degree_stats[0], degree_stats[1], degree_stats[2], degree_stats[3])
