#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for igraphplus"""

import unittest
import igraph

import igraphplus
from igraphplus import metrics

class IgraphPlusTestCase(unittest.TestCase):
    def setUp(self):
        self.undirected_graph = igraph.Graph.Full(100)
        self.directed_graph = igraph.Graph.Barabasi(1000)

    def test_efficiency(self):
        assert metrics.efficiency(self.undirected_graph) == 1.0

    def test_summary(self):
        metrics.summary(self.directed_graph)
        metrics.report(self.directed_graph)


if __name__ == '__main__':
    unittest.main()
