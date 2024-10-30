class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


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



def find_min(g, src, dest):

    if src == dest:
        return 0
    
    results = 0
    num_vertices = g.vertices

    visited = [False] * num_vertices
    distance = [0] * num_vertices

    # Initialize queue for breadth first search
    queue = MyQueue()

    # Enqueue the source vertex and mark it as visited
    queue.enqueue(src)
    visited[src] = True

    # Cycle through remaining graph vertices, until none are left
    while not queue.is_empty():

        # Dequeue vertex from queue and add it to results
        current_node = queue.dequeue()

        # Enqueue all neighbors of current vertex 
        temp = g.array[current_node].head_node

        while temp is not None:
            # Cycle through neighbor list (temp), add to queue, and mark as visited
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True
                distance[temp.data] = distance[current_node] + 1

                # Return the distance when destination node is found
                if temp.data == dest:
                    return distance[dest]
            
            temp = temp.next_element
    
    return -1



# Time Complexity = O(V+E)
# Space Complexity = O(V)


######################################################################



# Driver code
def main():
    inputs = [ [[0, 1],[1, 2]],
               [[1, 2],[2, 4],[1, 4],[4, 3]],
               [[0, 1],[1, 2],[2, 3],[3, 4],[2, 4]],
               [[0, 1],[1, 2],[2, 3],[3, 4],[4, 5],[5, 6]],
               [[0, 1],[1, 2], [2, 3],[0, 3]]
    ]

    src =  [0, 1, 0, 0, 1]
    dest = [2, 3, 4, 6, 3]

    for i in range(len(inputs)):
        g=Graph(7)
        for j in range(len(inputs[i])):
            g.add_edge(inputs[i][j][0],inputs[i][j][1])
        print("\tGraph:")
        g.print_graph()
        print("\n\tsrc: ", src[i], sep="")
        print("\tdest: ", dest[i], sep="")
        print("\n\tResult: ", find_min(g, src[i],dest[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()

