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



def union(head1, head2):

    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    visited_nodes = set()
    result = None

    while head1:
        visited_nodes.add(head1.data)
        head1 = head1.next

    # Traverse the second list to the end
    while head2:
        visited_nodes.add(head2.data)
        head2 = head2.next

    # Add elements of unqiue values to result
    for x in visited_nodes:
        result = insert_at_head(result, x)
    
    return result


def intersection(head1, head2):

    result = None
    visited_nodes = set()

    # Iterate over each node in the first list
    while head1:
        value = head1.data

        if value not in visited_nodes:
            visited_nodes.add(value)

        head1 = head1.next

    while head2:
        if head2.data in visited_nodes:

            result = insert_at_head(result, head2.data)
            visited_nodes.remove(head2.data)

        head2 = head2.next

    return result



def exists_in_results(data, head):

    current = head
    
    while current:
        if current.data == data:
            return True
        
        current = current.next

    return False


def insert_at_head(head, data):

    new_node = LinkedListNode(data)
    new_node.next = head
    return new_node



# Union
# Time Complexity = O(n+m+k)
# Space Complexity = O(min(n, m) + k)

# Intersection
# Time Complexity = O(n+m)
# Space Complexity = O(k)



#####################################################################



# Driver Code
def main():
    union_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 1, 2, 2, 3, 3, 4, 4, 5],
        [-45, 34, -54, 45, -65, 54],
        [12],
        [0, 1, 2],
    ]

    intersection_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 1, 2],
        [1, 1, 2, 2, 3, 3, 4, 4, 5],
        [-45, 34, -54, 45, -65, 54],
        [12],
    ]

    input_list2 = [
        [7, 8, 9, 10, 11, 12, 13, 14],
        [1, 3, 4, 1],
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1],
        [12],
    ]

    for i in range(len(union_list)):
        input_linked_list1 = LinkedList()
        input_linked_list2 = LinkedList()
        input_linked_list3 = LinkedList()

        input_linked_list1.create_linked_list(union_list[i])
        input_linked_list2.create_linked_list(intersection_list[i])
        input_linked_list3.create_linked_list(input_list2[i])
        
        print(i+1, ".\tInput linked list 1: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list1.head)
        
        print("\n\tInput linked list 2: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list3.head)
        
        print("\n\n\tUnion: ", end="")
        print_list_with_forward_arrow(union(input_linked_list1.head, input_linked_list3.head))

        print("\n\tIntersection: ", end="")
        print_list_with_forward_arrow(intersection(input_linked_list2.head, input_linked_list3.head))
        print("\n", "-"*100)


if __name__ == "__main__":
    main()

