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





def find_nth(head, n):

    # Set current to the head
    current = head

    # Calculate how many steps the pointer has to take from the head to nth node
    pointer = (length(head) - n)

    # Iterate through the linked list, deincrementing the pointer steps
    while pointer > 0:
        current = current.next
        pointer -= 1

    # Return the final position
    return current



def length(head):

    # Define a counter
    count = 0

    # If LinkedList is empty, return count = 0
    if head is None:
        return count
    else:
        count += 1

    # Otherwise, iterate over linked list until we find the end
    current = head

    while current.next:
        count += 1
        current = current.next
    
    # Once the end of the linked list is found
    return count





# Driver code
def main():
    input_data = (
        [7, 10, 14, 21, 22],
        [3, 6, 9, 12],
        [23, 19, 15, 22, 34, 76, 12],
        [5],
        [1, 3, 5, 7, 9, 11, 6],
    )
    n = [4, 2, 6, 1, 3]
    for i in range(len(input_data)):
        index = n[i]
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input_data[i])
        print("{0}.\tInput linked list: ".format(i+1), end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tn: ", index)
        print("\n\tNode returned:", find_nth(input_linked_list.head, index).data)
        print("-" * 100)

if __name__ == "__main__":
    main()



# Time Complexity = O(n)
# Space Complexity = O(1)