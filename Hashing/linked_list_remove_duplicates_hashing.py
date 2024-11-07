class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    # returns the number of nodes in the linked list
    def get_length(self, head):
        temp = head
        length = 0
        while(temp):
            length+=1
            temp = temp.next
        return length

    # returns the node at the specified position(index) of the linked list
    def get_node(self, head, pos):
        if pos != -1:
            p = 0
            ptr = head
            while p < pos:
                ptr = ptr.next
                p += 1
            return ptr
    
    # __str__(self) method will display the elements of linked list.
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


def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # print node value
        
        temp = temp.next
        if temp:
            print("→", end=" ")
        else:
            # if this is the last node, print null at the end
            print("→ null", end=" ")

def print_list_with_forward_arrow_loop(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # print node value
        
        temp = temp.next
        if temp:
            print("→", end=" ")



#####################################################################



def remove_duplicates(head):

    current_node = head
    prev_node = head

    # Initialize a set to store values of nodes which we already visited
    visited_nodes = set()

    if current_node and current_node.next:
        while current_node:
            value = current_node.data

            if value in visited_nodes:
                # Connect prev_node with current_node next element
                prev_node.next = current_node.next
                current_node = current_node.next

            else:   
                # Visit current_node for first time
                visited_nodes.add(current_node.data)
                prev_node = current_node
                current_node = current_node.next

    return head


# Time Complexity = O(n)
# Space Complexity = O(n)



#####################################################################



# Driver Code
def main():

    inputs = [
        [50, 10, 50, 10, 50],
        [-3, -4, 3, -3, -4, -7],
        [20, 20, 20, 20],
        [100, 100],
        [200],
    ]

    for i in range(len(inputs)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(inputs[i])
        print(i + 1, ".\tInput linked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tLinked list without duplicates: ", sep="", end="")
        print_list_with_forward_arrow(remove_duplicates(input_linked_list.head))

        print("\n", "-" * 100)


if __name__ == "__main__":
    main()