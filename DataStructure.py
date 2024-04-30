class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        self.nodes.append(Node(value))

    def add_edge(self, value1, value2):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)
        if node1 and node2:
            node1.children.append(node2)
            node2.children.append(node1)

    def find_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None
    
    def depth_first_search(self, start_value):
        start_node = self.find_node(start_value)
        if not start_node:
            print(f"Node with value {start_value} not found.")
            return
        
        visited = set()
        self._dfs_helper(start_node, visited)

    def _dfs_helper(self, node, visited):
        if node not in visited:
            print(node.value)
            visited.add(node)
            for child in node.children:
                self._dfs_helper(child, visited)

    def breadth_first_search(self, start_value):
        start_node = self.find_node(start_value)
        if not start_node:
            print(f"Node with value {start_value} not found.")
            return
        
        visited = set()
        queue = [start_node]
        
        while queue:
            current_node = queue.pop(0)
            if current_node not in visited:
                print(current_node.value)
                visited.add(current_node)
                for child in current_node.children:
                    queue.append(child)
