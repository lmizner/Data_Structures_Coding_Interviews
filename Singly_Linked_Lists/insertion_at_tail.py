# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList-type object
    def __init__(self):
        self.head = None

    # The insert_node_at_head method will insert a 
    # LinkedListNode at head of a linked list
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # The create_linked_list method will create the linked list using the
    # given integer array with the help of the insert_node_at_head method
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)
    
    # The __str__(self) method will display the elements of the linked list
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
    

# Template for LinkedListNode class
class LinkedListNode:
    # __init__ will be used to make a LinkedListNode-type object
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Template for printing the linked list with forward arrows
def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # print node value
        
        temp = temp.next
        if temp:
            print("→", end=" ")
        else:
            # If this is the last node, print null at the end
            print("→ null", end=" ")





def insert_at_tail(head, value):

    # Define a new node with given value
    new_node = LinkedListNode(value)

    # If LinkedList is empty, new node will become the head node
    if head is None:
        head = new_node
        return head

    # Otherwise, iterate over linked list until we find the end
    current = head

    while current.next:
        current = current.next
    
    # Once the end of the linked list is found
    current.next = new_node
    return head





def main():
    inputs = [
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4, -6],
        [3, 2, 1],
        [],
        [1, 2],
    ]

    values = [4, -5, 2, 0, -98]

    for i in range(len(inputs)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(inputs[i])
        
        print(i+1, ".\tInput linked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        
        print("\n\tNew node to be added: ", values[i], sep="", end="")
        
        print("\n\tUpdated linked list: ", end="")
        print_list_with_forward_arrow(insert_at_tail(input_linked_list.head, values[i]))
        print("\n", "-" * 100, sep='')


if __name__ == "__main__":
    main()



# Time Complexity = O(n)
# Space Complexity = O(1)