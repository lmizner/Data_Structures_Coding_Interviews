# Template for LinkedListNode class
class LinkedListNode:
    # __init__ will be used to make a LinkedListNode-type object
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList-type object
    def __init__(self):
        self.head = None

    # The insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # The create_linked_list method will create the linked list using the
    # given integer array with the help of the InsertAthead method
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)


# Template for printing the linked list with forward arrows
def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # Print node value
        
        temp = temp.next
        if temp:
            print("→", end=" ")
        else:
            # If this is the last node, print NULL at the end
            print("→ null", end=" ")





def union(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    current = head1
    while current.next:
        current = current.next
    current.next = head2
    remove_duplicates(head1)

    return head1

# Helper function to remove duplicate nodes from a list
def remove_duplicates(head1):
    if head1 is None:
        return

    # Iterate over each node in the list
    outer_node = head1
    while outer_node:
        # Use another pointer to compare the current node with the rest of the list
        inner_node = outer_node
        while inner_node.next:
            # If a duplicate is found, remove it by skipping the node
            if outer_node.data == inner_node.next.data:
                inner_node.next = inner_node.next.next
            else:
                inner_node = inner_node.next
        outer_node = outer_node.next

def intersection(head1, head2):
    result = None
    current1 = head1

    # Iterate over each node in the first list
    while current1:
        current2 = head2
        # Compare each node in the first list with each node in the second list
        while current2:
            # If a common element is found and it's not already in the result list, add it
            if current1.data == current2.data and not exists_in_result(current1.data, result):
                result = insert_at_head(result, current1.data)
            current2 = current2.next
        current1 = current1.next

    return result

# Function to check if a data value exists in the result list
def exists_in_result(data, head):
    current = head
    while current:
        if current.data == data:
            return True
        current = current.next
    return False

# Helper function to insert a new node at the head of a list
def insert_at_head(head, data):
    new_node = LinkedListNode(data)
    new_node.next = head
    return new_node





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
        [1, 1, 2, 2, 3, 3, 4, 4, 5],
        [-45, 34, -54, 45, -65, 54],
        [12],
        [0, 1, 2],
    ]

    input_list2 = [
        [7, 8, 9, 10, 11, 12, 13, 14],
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1],
        [12],
        [3, 4, 5],
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


# Union
# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Intersection
# Time Complexity = O(n * m * k)
# Space Complexity = O(k)