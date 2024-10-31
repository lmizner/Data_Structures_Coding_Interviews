from queue import Queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, values):
        self.root = self.createBinaryTree(values)

    def createBinaryTree(self, values):
        if len(values) == 0:
            return None

        # Create the root node of the binary search tree
        root = TreeNode(values[0])

        # Start iterating over the list of values starting from the second value
        for value in values[1:]:
            node = TreeNode(value)
            curr = root
            while True:
                # If the value is less than the current node's value, move to the left child
                if node.data <= curr.data:
                    if curr.left is None:
                        # If the left child is empty, insert the new node here and break the loop
                        curr.left = node
                        break
                    else:
                        # If the left child is not empty, move to the left child and continue the search
                        curr = curr.left
                else:
                    # If the value is greater or equal to the current node's value, move to the right child
                    if curr.right is None:
                        # If the right child is empty, insert the new node here and break the loop
                        curr.right = node
                        break
                    else:
                        # If the right child is not empty, move to the right child and continue the search
                        curr = curr.right

        # Return the root of the binary search tree
        return root
    

def display_tree(node):
    if node is None:
        print("Tree is empty")
        return

    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)

def _display_aux(node):
    if node is None:
        return [], 0, 0, 0

    if node.left is None and node.right is None:
        line = str(node.data)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    if node.left is None:
        lines, n, p, x = _display_aux(node.right)
        s = str(node.data)
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    if node.right is None:
        lines, n, p, x = _display_aux(node.left)
        s = str(node.data)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    left, n, p, x = _display_aux(node.left)
    right, m, q, y = _display_aux(node.right)
    s = '%s' % node.data
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)

    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2



##############################################################



def find_min(root):
    # If the root is None (empty tree), return None as there's no minimum value.
    if root is None:  
        return None
    
    # Start from the root node.
    current = root
    
    # Traverse left until reaching the leftmost node (minimum value node).
    while current.left:  
        current = current.left
        
    # Return the data (value) of the leftmost node, which is the minimum value.
    return current.data



# Time Complexity = O(n)
# Space Complexity = O(1)



##############################################################



# Driver code
def main():

    inputs = [
        [18, 15, 13, 19, 5, 14],
        [1, 2, 3, 4, 5, 6],
        [100, 200, 50, 40, 30, 80, 90],
        [10],
        [1, 2],
        [-10, -20, -30, -40, -50, -60, -70]
    ]
    y = 1
    for i in range(len(inputs)):
        input_tree = BinarySearchTree(inputs[i])
        print(y, ".\tInput Tree:", sep = "")
        display_tree(input_tree.root)
        print("\n\tSmallest element: ",
              find_min(input_tree.root))
        print("-"*100, "\n")
        y+=1
if __name__ == "__main__":
    main()

