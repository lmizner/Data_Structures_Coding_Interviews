# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next_element = self.head
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
            temp = temp.next_element
        return length

    # returns the node at the specified position(index) of the linked list
    def get_node(self, head, pos):
        if pos != -1:
            p = 0
            ptr = head
            while p < pos:
                ptr = ptr.next_element
                p += 1
            return ptr
    
    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next_element
            if temp:
                result += ", "
        result += ""
        return result
    

# Template for linked list node class
class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next_element=None):
        self.data = data
        self.next_element = next_element


# Template for printing the linked list with forward arrows
def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # print node value
        
        temp = temp.next_element
        if temp:
            print("→", end=" ")
        else:
            # if this is the last node, print null at the end
            print("→ null", end=" ")

def print_list_with_forward_arrow_cycle(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # print node value
        
        temp = temp.next_element
        if temp:
            print("→", end=" ")





def detect_cycle(head):

    # Initialize slow and fast pointers
    slow = head
    fast = head

    # If LinkedList is empty, there is no cycle
    if head is None:
        return False

    # Traverse linked list
    while slow and fast and fast.next_element:
        # Move pointers forward
        slow = slow.next_element
        fast = fast.next_element.next_element

        # If pointers meet, there is a cycle
        if slow == fast:
            return True
    
    # If None is reached, there is no cycle
    return False





# Driver code
def main():

    input = (
             [2, 4, 6, 8, 10, 12],
             [1, 3, 5, 7, 9, 11],
             [0, 1, 2, 3, 4, 6],
             [3, 4, 7, 9, 11, 17],
             [5, 1, 4, 9, 2, 3],
            )
    pos = [0, -1, 1, -1, 2]
    j = 1

    for i in range(len(input)):

        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(f"{j}.\tInput: ", sep="", end="")
        if pos[i] == -1:
            print_list_with_forward_arrow(input_linked_list.head)
        else:
            print_list_with_forward_arrow_cycle(input_linked_list.head)
        print("\n\tPosition:", pos[i])
        if pos[i] != -1:
            length = input_linked_list.get_length(input_linked_list.head)
            last_node = input_linked_list.get_node(input_linked_list.head, length - 1)
            last_node.next_element = input_linked_list.get_node(input_linked_list.head, pos[i])

        print(f"\n\tDetected cycle = {detect_cycle(input_linked_list.head)}")
        j += 1
        print("-"*100, "\n")


if __name__ == "__main__":
    main()



# Time Complexity = O(n)
# Space Complexity = O(1)