import collections

def check_path(n, edges, source, destination):

    # Create an adjacency list using the graph edges
    adjacency = collections.defaultdict(list)

    for a, b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)

    # Initialize a queue to store nodes needing to be exlored and set to store visited nodes
    visited = set()
    queue = [source]

    visited.add(source)

    # Perform breadth first search to find path
    while queue:
        current_vertex = queue.pop(0)

        # Check if the dequeued vertex in the destination
        if current_vertex == destination:
            return True
        
        # Check neighbors of current vertex
        for neighbor in adjacency[current_vertex]:
            
            # If neighbor has not been visited yet, enqueue, and mark visited
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    # If destination vertex is not reached
    return False



# Time Complexity = O(V+E)
# Space Complexity = O(V+E)


######################################################################


# Driver code
def main():
    n = [3, 4, 6, 5, 7]
    edges = [[[0, 1], [1, 2]],
             [[0, 1], [0, 3]],
             [[0, 1], [1, 2], [1, 3], [1, 4], [3, 5]],
             [[0, 3], [1, 3], [2, 4]],
             [[0, 6], [1, 5], [1, 4], [2, 4], [2, 5], [2, 6], [3, 4], [3, 6], [4, 5], [5, 6]]]
    sources = [2, 0, 0, 3, 5]
    destinations = [0, 2, 5, 4, 3]

    for i in range(len(edges)):
        print(i+1,".\tn: ", n[i])
        print("\tEdges: ", edges[i])
        print("\tSource:", sources[i])
        print("\tDestination: ", destinations[i])
        print("\tPath exists: ", check_path(n[i], edges[i], sources[i], destinations[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()