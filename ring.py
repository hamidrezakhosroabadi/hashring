from sortedcontainers import sorteddict


class Ring:
    def __init__(self):
        self.nodes = sorteddict()

    def add_node(self, node):
        self.nodes[node.key] = node

    def remove_node(self, node):
        del self.nodes[node.key]

    def get_node(self, key):
        return self.nodes[key]

    def find_route(self, key):
        return self.nodes[self.nodes.iloc[self.nodes.bisect(key)]]
