class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        if self.head is None:  # Check whether the head is None
            return True
        else:
            return False

    def insert_at_head(self, dt):
        temp_node = LinkedListNode(dt)
        if self.is_empty():
            self.head = temp_node
            return self.head
        temp_node.next = self.head
        self.head = temp_node
        return self.head

    # Inserts a value at the end of the list
    def insert_at_tail(self, value):
        # Creating a new node
        new_node = LinkedListNode(value)
        # Check if the list is empty, if it is simply point head to new node
        if self.get_head() is None:
            self.head = new_node
            return
        # if list not empty, traverse the list to the last node
        temp = self.get_head()
        while temp.next is not None:
            temp = temp.next
        # Set the nextElement of the previous node to new node
        temp.next = new_node
        return


class Graph:
    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # definining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        self.array = []
        # Creating a new Linked List for each vertex/index of the list
        for i in range(vertices):
            self.array.append(LinkedList())

    # Function to add an edge from source to destination
    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
        # As we are implementing a directed graph, (1,0) is not equal to (0,1)
            self.array[source].insert_at_head(destination)
            # Uncomment the following line for undirected graph 
            self.array[destination].insert_at_head(source)

        # If we were to implement an Undirected Graph i.e (1,0) == (0,1)
        # We would create an edge from destination towards source as well
        # i.e self.list[destination].insertAtHead(source)

    def print_graph(self):
        print("\t>>Undirected Graph<<")
        for i in range(self.vertices):
            print("\t|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next
            print("None")



######################################################################



def is_tree(graph):

    visited = [False] * graph.vertices

    # Check cycle by recursively visiting adjacent nodes
    if check_cycle(graph, 0, visited, -1):
        return False
    
    # CHeck if all node were visited from the source
    for i in range(len(visited)):
        if not visited[i]:
            return False

    return True



def check_cycle(graph, node, visited, parent):

    visited[node] = True

    # Pick an adjacent node and run recursive depth first search
    adjacent = graph.array[node].head

    while adjacent:
        if not visited[adjacent.data]:
            if check_cycle(graph, adjacent.data, visited, node):
                return True
            
        elif adjacent.data is not parent:
            return True
        
        adjacent = adjacent.next

    return False



# Time Complexity = O(V+E)
# Space Complexity = O(V)


######################################################################



def main():
    n = [3, 4, 5, 5, 6, 1]
    edges = [[[0, 1], [0, 2], [1, 2]], 
             [[0, 1], [0, 2], [0, 3]], 
             [[0, 1], [0, 2], [0, 3], [0, 4], [3, 4]], 
             [[0, 1], [0, 2], [0, 3], [3, 4]], 
             [[0, 1], [0, 2], [1, 3], [2, 4], [0, 5]],
             []]

    for i in range(len(n)):
        print(i + 1, ".\t n = ", n[i], sep="")
        print("\t Edges = ", edges[i], sep="")
        g = Graph(n[i])
        for j in range(len(edges[i])):
            g.add_edge(edges[i][j][0], edges[i][j][1])
        print("\n")
        g.print_graph()
        print("\n\t Is the given graph a valid tree:", is_tree(g))
        print("-" * 100)

main()




