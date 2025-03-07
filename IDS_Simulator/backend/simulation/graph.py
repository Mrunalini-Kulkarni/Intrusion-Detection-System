class NetworkGraph:
    def __init__(self):
        self.graph = {}  # Adjacency list

    def add_device(self, device):
        """Add a device (node) to the network."""
        if device not in self.graph:
            self.graph[device] = []

    def add_connection(self, device1, device2):
        """Add a connection (edge) between two devices."""
        if device1 in self.graph and device2 in self.graph:
            self.graph[device1].append(device2)
            self.graph[device2].append(device1)

    def get_devices(self):
        """Return a list of all devices in the network."""
        return list(self.graph.keys())

    def get_connections(self, device):
        """Return a list of connections for a given device."""
        return self.graph.get(device, [])

    def bfs(self, start):
        """Perform BFS traversal to detect suspicious paths."""
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                queue.extend(self.graph[node])
        return visited
