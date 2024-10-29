class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:  # Check whether the head is None
            return True
        else:
            return False

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        if self.is_empty():
            self.head_node = temp_node
            return self.head_node
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    # Inserts a value at the end of the list
    def insert_at_tail(self, value):
        # Creating a new node
        new_node = Node(value)
        # Check if the list is empty, if it is simply point head to new node
        if self.get_head() is None:
            self.head_node = new_node
            return
        # if list not empty, traverse the list to the last node
        temp = self.get_head()
        while temp.next_element is not None:
            temp = temp.next_element
        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return

    def length(self):
        # start from the first element
        curr = self.get_head()
        length = 0

        # Traverse the list and count the number of nodes
        while curr is not None:
            length += 1
            curr = curr.next_element
        return length

    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def delete_at_head(self):
        # Get Head and firstElement of List
        first_element = self.get_head()
        # If List is not empty then link head to the
        # nextElement of firstElement.
        if first_element is not None:
            self.head_node = first_element.next_element
            first_element.next_element = None
        return

    def delete(self, value):
        deleted = False
        if self.is_empty():  # Check if list is empty -> Return False
            print("List is Empty")
            return deleted
        current_node = self.get_head()  # Get current node
        previous_node = None  # Get previous node
        if current_node.data is value:
            self.delete_at_head()  # Use the previous function
            deleted = True
            return deleted

        # Traversing/Searching for Node to Delete
        while current_node is not None:
            # Node to delete is found
            if value is current_node.data:
                # previous node now points to next node
                previous_node.next_element = current_node.next_element
                current_node.next_element = None
                deleted = True
                break
            previous_node = current_node
            current_node = current_node.next_element
        return deleted

    def search(self, dt):
        if self.is_empty():
            print("List is Empty")
            return None
        temp = self.head_node
        while temp is not None :
            if temp.data is dt:
                return temp
            temp = temp.next_element
        print(dt, " is not in List!")
        return None

    def remove_duplicates(self):
        if self.is_empty():
            return

        # If list only has one node, leave it unchanged
        if self.get_head().next_element is None:
            return

        outer_node = self.get_head()
        while outer_node:
            inner_node = outer_node  # Iterator for the inner loop
            while inner_node:
                if inner_node.next_element:
                    if outer_node.data == inner_node.next_element.data:
                        # Duplicate found, so now removing it
                        new_next_element = inner_node.next_element.next_element
                        inner_node.next_element = new_next_element
                    else:
                        # Otherwise simply iterate ahead
                        inner_node = inner_node.next_element
                else:
                    # Otherwise simply iterate ahead
                    inner_node = inner_node.next_element
            outer_node = outer_node.next_element
        return
    

class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return self.stack_size
    
    def push(self, value):
        self.stack_size += 1
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -= 1
        return self.stack_list.pop()


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
        if (source < self.vertices and destination < self.vertices):
        # As we are implementing a directed graph, (1,0) is not equal to (0,1)
            self.array[source].insert_at_head(destination)
            # Uncomment the following line for undirected graph 
            # self.array[destination].insert_at_head(source)

        # If we were to implement an Undirected Graph i.e (1,0) == (0,1)
        # We would create an edge from destination towards source as well
        # i.e self.list[destination].insertAtHead(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")



######################################################################


# Kosaraju's strongly connected component algorithm
def find_mother_vertex(g):
    
    visited = [False] * g.vertices
    last_vertex = 0

    for i in range(g.vertices):

        if not visited[i]:

            perform_DFS(g, i , visited)
            last_vertex = i

    visited = [False] * g.vertices

    # Verify if last_vertex is a mother vertex by performing DFS
    perform_DFS(g, last_vertex, visited)

    # If any vertex is not visited in second pass
    if any(not i for i in visited):
        # last vertex is not a mother vertex
        return -1
    else:
        # last vertex is a mother vertex
        return last_vertex


    
def perform_DFS(g, node, visited):
    
    visited[node] = True
    temp = g.array[node].head_node

    # Traverse all adjacent vertices
    while temp:

        if not visited[temp.data]:

            # Perform DFS from adjacent vertex
            perform_DFS(g, temp.data, visited)

        temp = temp.next_element


# Time Complexity = O(V+E)
# Space Complexity = O(V)


######################################################################



def main():
    n = [3, 4, 5, 4, 3]
    edges = [[[0, 1], [0, 2], [1, 2]],
            [[2, 3], [3, 2, 1], [3, 0, 2], [2, 1]],
            [[0, 1], [0, 2], [0, 3], [0, 4], [3, 4]],
            [[0, 2, 1], [3, 2, 1], [2, 1, 0]],
            [[2, 0, 1], [1, 2]]]

    for i in range(len(n)):
        print(i + 1, ".\t n = ", n[i], sep="")
        print("\t Edges = ", edges[i], sep="")
        g = Graph(n[i])
        for j in range(len(edges[i])):
            g.add_edge(edges[i][j][0], edges[i][j][1])
        print("\n")
        g.print_graph()
        print("\n\t The mother vertex in this graph is:", find_mother_vertex(g))
        print("-" * 100)

main()




