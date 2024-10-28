# Template for the EduLinkedList
class LinkedList:
    # __init__ will be used to make a EduLinkedList-type object
    def __init__(self):
        self.head = None

    # The insert_node_at_head method will insert a EduEduLinkedListNode at head
    # of a EduLinkedList
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # The create_linked_list method will create the EduLinkedList using the
    # given integer array with the help of the InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    # Returns the number of nodes in the EduLinkedList
    def get_length(self, head):
        temp = head
        length = 0
        while(temp):
            length+=1
            temp = temp.next
        return length

    # Returns the node at the specified position (index) of the EduLinkedList
    def get_node(self, head, pos):
        if pos != -1:
            p = 0
            ptr = head
            while p < pos:
                ptr = ptr.next
                p += 1
            return ptr
    
    # The __str__(self) method will display the elements of the EduLinkedList.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result


class LinkedListNode:
    # __init__ will be used to make a LinkedListNode-type object
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MyQueue:
    def __init__(self):
        self.queue_list = []
        self.queue_size = 0

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def size(self):
        return self.queue_size
    
    def enqueue(self, value):
        self.queue_size += 1
        self.queue_list.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self.queue_list.remove(self.front())
        self.queue_size -= 1
        return front
    

class Graph:
    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # Definining a list that can hold multiple LinkedLists
        # Equal to the number of vertices in the graph
        self.array = []
        # Creating a new LinkedList for each vertex/index of the list
        for i in range(vertices):
            self.array.append(LinkedList())

    # Function to add an edge from source to destination
    def add_edge(self, source, destinations):
        if source < self.vertices:
            for dest in destinations:
                if dest < self.vertices:
                    dest_node = LinkedListNode(dest)
                    self.array[source].insert_node_at_head(dest_node)
        
        # As we are implementing a directed graph, (1,0) is not equal to (0,1)
            # dest_node = LinkedListNode(destination)
            # self.array[source].insert_node_at_head(dest_node)

        # If we were to implement an Undirected Graph, i.e., (1,0) == (0,1),
        # we would create an edge from destination toward source as well
        # i.e., self.list[destination].insertAtHead(source)

    def print_graph(self):
        for i in range(self.vertices):
            print("\t|", i, end=" | => ")
            temp = self.array[i].head
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next
            print("None")



######################################################################



def bfs_traversal(graph, source):

    # Initialize an empty array to store results
    results = []
    num_vertices = graph.vertices
    visited = [False] * num_vertices 

    # Create a queue for BFS
    queue = MyQueue()

    # Enqueue the source vertex and mark it as visited
    queue.enqueue(source)
    visited[source] = True

    # Cycle through remaining graph vertices, until none are left
    while not queue.is_empty():

        # Dequeue vertex from queue and add it to results
        current_vertex = queue.dequeue()
        results.append(current_vertex) 

        # Enqueue all neighbors of current vertex 
        temp = graph.array[current_vertex].head

        while temp is not None:
            # Cycle through neighbor list (temp), add to queue, and mark as visited
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True
            temp = temp.next
    
    return results



# Time Complexity = O(V+E)
# Space Complexity = O(V)

######################################################################



# Driver code
def main():
    # Vertices for each graph
    graph_vertices = [5, 4, 6]  
    # Edges for each graph
    graph_edges = [[[[0, [1, 2]], [2, [0, 3, 4]]]], [[[0, [1, 2]], [2, [0, 3]]]], [[[0, [1, 4]], [1, [2, 5]], [4, [3]], [3, [2]]]]]  
    sources = [2, 0, 0]
    
    for i in range(len(graph_vertices)):
        graph = Graph(graph_vertices[i])
        for j in range(len(graph_edges[i][0])):
            source, destinations = graph_edges[i][0][j]
            graph.add_edge(source, destinations)
        
        print(str(i+1)+".\t>>Adjacency List of the Graph<<\n")
        graph.print_graph()
        print("\n\tBFS Traversal starting from vertex "+ str(sources[i])+ ":", bfs_traversal(graph, sources[i]))
        print("-"*100, "\n")
if __name__ == "__main__":
    main()

