"""This module contains SortedDict data structure."""
from sortedcontainers import SortedDict


class Ring:
    """This class provides Ring class implementation."""

    def __init__(self):
        """This method inits the sorted dict data structure"""
        self.__nodes = SortedDict()

    def add_node(self, node):
        """This method adds new nodes to sorted dict."""
        self.__nodes[node.key] = node

    def remove_node(self, node):
        """This method removes nodes from sorted dict."""
        del self.__nodes[node.key]

    def get_node(self, key):
        """This method retrives nodes from sorted dict by their keys."""
        return self.__nodes[key]

    def get_nodes(self):
        """This method retrives all nodes from sorted dict."""
        return self.__nodes

    def find_route(self, key, count):
        """This method finds the best destination for specefic key."""
        bisect_index = self.__nodes.bisect(key)
        return [self.__nodes[self.__nodes.iloc[bisect_index+i]] for i in range(count)]

    def __len__(self):
        """This method returns class length."""
        return len(self.__nodes)

    def __get_item__(self, key):
        """This method returns class item by the key."""
        return self.__nodes[key]
