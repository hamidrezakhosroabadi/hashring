"""This module contains SortedDict data structure."""
from sortedcontainers import SortedDict


class Ring:
    """This class provides Ring class implementation."""

    def __init__(self):
        """This method inits the sorted dict data structure"""
        self.nodes = SortedDict()

    def add_node(self, node):
        """This method adds new nodes to sorted dict."""
        self.nodes[node.key] = node

    def remove_node(self, node):
        """This method removes nodes from sorted dict."""
        del self.nodes[node.key]

    def get_node(self, key):
        """This method retrives nodes from sorted dict by their keys."""
        return self.nodes[key]

    def find_route(self, key):
        """This method finds the best destination for specefic key."""
        return self.nodes[self.nodes.iloc[self.nodes.bisect(key)]]
