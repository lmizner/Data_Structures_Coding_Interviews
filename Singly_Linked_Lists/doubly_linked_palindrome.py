class DoublyLinkedListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

# Template for the doubly linked list
class DoublyLinkedList:
    # __init__ will be used to make a DoublyLinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a DoublyLinkedListNode at the head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of insert_node_at_head method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = DoublyLinkedListNode(x)
            self.insert_node_at_head(new_node)
    
    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        return result
    

# Template for printing the linked list with forward arrows
def print_list_with_arrows(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # print node value
        
        temp = temp.next
        if temp:
            print("⟷", end=" ")
        else:
            # if this is the last node, print null at the end
            print("⟶ null", end=" ")
    




def is_palindrome(head):

    pointer_1 = head
    pointer_2 = get_tail_node(head)

    while pointer_1 != pointer_2:
        if pointer_1.data == pointer_2.data:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.prev
        else:
            return False
        
    return True



def get_tail_node(head):
    temp = head
    while temp.next is not None:
        temp = temp.next
    return temp





# Driver code
def main():
    input = (
                [2, 4, 6, 4, 2],
                [0, 3, 5, 5, 0],
                [9, 7, 4, 4, 7, 9],
                [5, 4, 7, 9, 4, 5],
                [5, 9, 8, 3, 8, 9, 5],
            )
    j = 1

    for i in range(len(input)):
        input_linked_list = DoublyLinkedList()
        input_linked_list.create_linked_list(input[i])
        head = input_linked_list.head
        print(j, ".\tDoubly Linked List:", end=" ", sep="")
        print_list_with_arrows(head)
        print("\n\n\tIs it a palindrome?", "Yes" if is_palindrome(head) else "No")
        j += 1
        print("-"*100, "\n")

if __name__ == "__main__":
    main()



# Time Complexity = O(n)
# Space Complexity = O(1)

