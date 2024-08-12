class Graph:
    def __init__(self, nodes, graph_type, adj, max_edges):
        self.nodes = nodes
        self.graph_type = graph_type
        self.adj = adj
        self.max_edges = max_edges
        self.create_graph()

    def create_graph(self):
        edge_count = 0
        while True:
            # add edges based on user input
            u, v = map(int, input(f"Enter graph edges within the range of 0-{self.nodes-1}: ").split())
            if 0 <= u < self.nodes and 0 <= v < self.nodes:
                if self.graph_type == 0:
                    self.addUndirectedEdges(u, v)
                else:
                    self.addDirectedEdges(u, v)
                edge_count += 1

                if edge_count < self.max_edges:
                    prompt = input("Would you like to enter another edge? (y/n): ")
                    if prompt != 'y':
                        break
                    else:
                        continue
                else:
                    break
            else:
                print(f"Node(s) out of bounds. Please enter in the range of 0-{self.nodes-1}\n")
                continue
    
    def addUndirectedEdges(self, v1, v2):
        self.adj[v1].append(v2)
        self.adj[v2].append(v1)

    def addDirectedEdges(self, v1, v2):
        self.adj[v1].append(v2)

    def isConnected(self):
        # init all visits to 0 before traversal
        visited = [False for _ in range(self.nodes)]
        self.DFS(self.adj, 0, visited)

        for i in range(self.nodes):
            if not visited[i]:
                return False
        return True

    def isStronglyConnected(self):
        return True

    def DFS(self, adj, v, visited):
        visited[v] = True
        # check neighboring nodes of each vertex -- deep as possible before backtracking
        for n in adj[v]:
            if not visited[n]:
                self.DFS(self.adj, n, visited)

def main():
    directed = int(input("Is this a directed (1) or undirected graph (0)?: "))
    nodes = int(input("How many vertices?: "))
    result = 0
    max_edges = 0
    if directed:
        max_edges = nodes*(nodes - 1)
    else:
        max_edges = (nodes*(nodes - 1))/2

    # generate adjacency list
    adj = [[] for _ in range(nodes)]

    graph = Graph(nodes, directed, adj, max_edges)
    # print(f"result: {graph.isConnected()}\n\n")
    if not directed:
        result = graph.isConnected()
    else:
        result = graph.isStronglyConnected()

    if result:
        if directed:
            print("\nThis directed graph is strongly connected.\n")
        else:
            print("\nThis undirected graph is connected.\n")
    else:
        if directed:
            print("\nThis directed graph is not strongly connected.\n")
        else:
            print("\nThis undirected graph is not connected.\n")

if __name__ == "__main__":
    main()
