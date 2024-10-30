class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency = {}
 
    def add_edge(self, u, v):
        if u in self.adjacency:
            self.adjacency[u].append(v)
        else:
            self.adjacency[u] = [v]

    def print_adjacency_list(self):
        for node, neighbors in self.adjacency.items():
            print(node, "->", neighbors)



######################################################################



def remove_edge(graph, source, destination):

    if source in graph.adjacency and destination in graph.adjacency[source]:

        # Remove destination node from adjancency list
        graph.adjacency[source].remove(destination)

    return graph


def count_vertices(edges):

    vertices = 0

    # Flatten the list of edges to count unique vertices
    flat = [num for sublist in edges for num in sublist]

    # Check for vertices in flattened list
    if len(flat) != 0:
        vertices = max(flat)

    return vertices + 1



# Time Complexity = O(V)
# Space Complexity = O(1)


######################################################################



# Driver code
import random

def main():
    edges = [[[0, 1], [1, 2]],
             [[0, 1], [0, 3], [1, 2]],
             [[0, 1], [1, 2], [1, 3], [1, 4], [3, 5]],
             [[0, 3], [1, 3], [2, 4], [3, 2]],
             [[0, 6], [1, 5], [1, 4], [2, 4], [2, 5], [2, 6], [3, 4], [3, 6], [4, 5], [5, 6]]]

    for i in range(len(edges)):
        vertices = count_vertices(edges[i])
        g = Graph(vertices)
        edge = random.choice(edges[i])
        for src, dest in edges[i]:
            g.add_edge(src, dest)
        print("Initial graph: \n")
        g.print_adjacency_list()
        print("\nSource: ",edge[0])
        print("Destination: ",edge[1])
        g = remove_edge(g,edge[0],edge[1])
        print("\nGraph after removing the edge: ") 
        g.print_adjacency_list()
        print("-"*100)


if __name__ == "__main__":
    main()

