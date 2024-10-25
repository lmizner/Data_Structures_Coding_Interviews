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





def remove_duplicates(head):

    # Check if LinkedList is empty
    if head is None:
        return None
    
    # Check is LinkedList contains only one node
    if head.next is None: 
        return head
    
    # Initialize pointer
    outer = head
    
    # Traverse LinkedList searching for duplicate values
    while outer:
        inner = outer

        while inner:
            if inner.next:
                # Check if duplicate is found, and if so, remove it
                if outer.data == inner.next.data:
                    new_next = inner.next.next
                    inner.next = new_next
                # Otherwise move to the next node
                else:
                    inner = inner.next
            
            else:
                inner = inner.next
        
        outer = outer.next

    return head





def main():

    inputs = [
        [30, 20, 30, 10, 50],
        [-7, -7, -22, -1, -5, -5],
        [1, 1, 1],
        [9, -9, 9],
        [1, -2, -2],
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
    


# Time Complexity = O(n^2)
# Space Complexity = O(1)