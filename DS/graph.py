"""The Graph data structure, implemented as a dict via Nick Hunt-Walker."""
from stack import Stack
from que import Queue
from collections import OrderedDict
from math import inf


class Graph(object):
    """The Graph data structure.

    g.nodes(): return a list of all nodes in the graph
    g.edges(): return a list of all edges in the graph
    g.add_node(n): adds a new node 'n' to the graph
    g.add_edge(n1, n2): adds a new edge to the graph connecting 'n1' and 'n2',
        if either n1 or n2 are not already present in the graph,
        they should be added.
    g.del_node(n): deletes the node 'n' from the graph, raises an error if no
        such node exists
    g.del_edge(n1, n2): deletes the edge connecting 'n1' and 'n2' from the
        graph, raises an error if no such edge exists
    g.has_node(n): True if node 'n' is contained in the graph, False if not.
    g.neighbors(n): returns the list of all nodes connected to 'n' by edges,
        raises an error if n is not in g
    g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2,
        False if not, raises an error if either of the supplied nodes are not
        in g
    """

    def __init__(self):
        """Initialize a graph."""
        self._container = {}

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return list(self._container.keys())

    def add_node(self, node):
        """Add a node to the graph."""
        self._container.setdefault(node, OrderedDict())

    def add_edge(self, node1, node2, weight=1):
        """Add a connection between two nodes to the graph."""
        self.add_node(node1)
        self.add_node(node2)
        if node2 not in self._container[node1]:
            self._container[node1][node2] = weight

    def has_node(self, node):
        """Boolean value of whether or not the node exists in the graph."""
        return node in self._container

    def edges(self):
        """Return a list of all edges in the graph."""
        edge_list = []
        for node in self.nodes():
            for neighbor in self.neighbors(node):
                edge_list.append((node,
                                  neighbor,
                                  self._container[node][neighbor]))
        return edge_list

    def del_node(self, node):
        """Remove the node from the graph."""
        if self.has_node(node):
            self._container.pop(node)
            for n in self.nodes():
                if self.adjacent(n, node):
                    self._container[n].pop(node)
        else:
            raise KeyError("Node not in graph.")

    def del_edge(self, node1, node2):
        """Remove the connection between two nodes, if one exists."""
        if self.adjacent(node1, node2):
            self._container[node1].pop(node2)
        else:
            raise KeyError("Edge doesn't exist")

    def neighbors(self, node):
        """Return a list of neighbors for a given node."""
        try:
            return self._container[node]
        except KeyError:
            raise KeyError("This node is not in the graph.")

    def adjacent(self, node1, node2):
        """Return a boolean of whether or not node2 is a neighbor of node1."""
        return node2 in self.neighbors(node1)

    def depth_first_traversal(self, start_node):
        """Go wide first."""
        path = []

        if self.has_node(start_node):
            path.append(start_node)
            to_visit = Stack(self._container[start_node][::-1])

            while len(to_visit):
                next_node = to_visit.pop()
                if next_node not in path:
                    path.append(next_node)
                for neighbor in self.neighbors(next_node):
                    to_visit.push(neighbor)

        return path

    def breadth_first_traversal(self, start_node):
        """Go wide first."""
        path = []
        if self.has_node(start_node):
            path.append(start_node)
            to_visit = Queue(self._container[start_node])

            while len(to_visit):
                next_node = to_visit.dequeue().data
                if next_node not in path:
                    path.append(next_node)
                for neighbor in self.neighbors(next_node):
                    to_visit.enqueue(neighbor)

        return path

    def dijkstras_shortest_path(self, start, end):
        """Dijkstra algorithm for the shortest path between two points."""
        dist_dict = {node: inf for node in self.nodes()}
        dist_dict[start] = 0
        path = {}
        to_visit = self.nodes()

        while to_visit:
            min_item = sorted([(item, dist_dict[item]) for item in dist_dict if item in to_visit], key=lambda x: x[1])[0][0]
            to_visit.remove(min_item)

            for neighbor in self.neighbors(min_item):
                alt = dist_dict[min_item] + self._container[min_item][neighbor]
                if alt < dist_dict[neighbor]:
                    dist_dict[neighbor] = alt
                    path[neighbor] = min_item

        return self._reverse_path(path, end)

    def _reverse_path(self, path, end):
        """Take the path dict and find the start from the end."""
        pathway = []
        curr = end
        try:
            while curr:
                pathway.append(curr)
                curr = path[curr]

        except KeyError:
            pass

        return pathway[::-1]

    def bellman_ford_shortest_path(self, start, end):
        """The Bellman-Ford algorithm for shortest path between two points."""
        dist_dict = {node: inf for node in self.nodes()}
        dist_dict[start] = 0
        path = {}

        for item in self.nodes():
            for edge in self.edges():
                if dist_dict[edge[0]] + edge[2] < dist_dict[edge[1]]:
                    dist_dict[edge[1]] = dist_dict[edge[0]] + edge[2]
                    path[edge[1]] = edge[0]

        for edge in self.edges():
            if dist_dict[edge[0]] + edge[2] < dist_dict[edge[1]]:
                raise ValueError("Graph contains a negative-weight cycle")
        return self._reverse_path(path, end)

    def floyd_shortest_path(self, start, end):
        """."""
        dist_dict = {}
        path = {}
        for node1 in self.nodes():
            dist_dict[node1] = {}
            path[node1] = {}
            for node2 in self.nodes():
                dist_dict[node1][node2] = inf if node1 != node2 else 0
                path[node1][node2] = None

        for edge in self.edges():
            dist_dict[edge[0]][edge[1]] = edge[2]
            path[edge[0]][edge[1]] = edge[1]

        for k in self.nodes():
            for i in self.nodes():
                for j in self.nodes():
                    if dist_dict[i][j] > dist_dict[i][k] + dist_dict[k][j]:
                        dist_dict[i][j] = dist_dict[i][k] + dist_dict[k][j]
                        path[i][j] = path[i][k]

        return self._reverse_floyd_path(path, start, end)

    def _reverse_floyd_path(self, path, start, end):
        if not path[start][end]:
            return None
        final = [start]
        curr = start
        while curr != end:
            curr = path[curr][end]
            final.append(curr)

        return final
