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





def search(head, value):
  
    # If LinkedLIst is empty return False
    if head is None:
        return False
        
    # Set current value to head
    current = head
    
    # Check if the head of the list is equal to the value
    if current.data == value:
        return True
    
    # Check the remainder of the list for the value
    while current.next:
        if current.data == value:
            return True
        else:
            current = current.next
    
    # If value is not found, return False
    return False





# Driver code
def main():
    inputs = [
        [10, 20, 30, 40, 50],
        [-1, -2, -3, -4, -5, -6],
        [3, 2, 1],
        [],
        [12],
    ]
    value = [50, -7, 3, 55, 12]

    for i in range(len(inputs)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(inputs[i])
        if len(inputs[i]) == 0:
            print(i+1, ".\tInput linked list: null", sep="", end="")
        else:
            print(i+1, ".\tInput linked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tSearched value: ", value[i] )
        print("\n\tSingly linked list value found : ", search(input_linked_list.head, value[i]) )
        print("\n", "-"*100)


if __name__ == "__main__":
    main()



# Time Complexity = O()
# Space Complexity = O()