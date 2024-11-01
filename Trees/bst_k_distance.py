from typing import List
from queue import Queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, nodes):
        self.root = self.createBinaryTree(nodes)

    def createBinaryTree(self, nodes):
        if len(nodes) == 0:
            return None

        # Create the root node of the binary tree
        root = TreeNode(nodes[0].data)

        # Create a queue and add the root node to it
        queue = Queue()
        queue.put(root)

        # Start iterating over the list of nodes starting from the second node
        i = 1
        while i < len(nodes):
            # Get the next node from the queue
            curr = queue.get()

            # If the node is not None, create a new TreeNode object for its left child,
            # set it as the left child of the current node, and add it to the queue
            if nodes[i] is not None:
                curr.left = TreeNode(nodes[i].data)
                queue.put(curr.left)

            i += 1

            # If there are more nodes in the list and the next node is not None,
            # create a new TreeNode object for its right child, set it as the right child
            # of the current node, and add it to the queue
            if i < len(nodes) and nodes[i] is not None:
                curr.right = TreeNode(nodes[i].data)
                queue.put(curr.right)

            i += 1

        # Return the root of the binary tree
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



def find_k_nodes(root, k):
    
    result = []
    find_k(root, k, result)
    return result

# Helper function
def find_k(root, k, result):

    # Check that root exists
    if root is None:
        return 
    
    # Append the kth node
    if k == 0:
        result.append(root.data)
        return
    
    # Check recursively in both subtrees for kth node
    else:
        find_k(root.left, k-1, result)
        find_k(root.right, k-1, result)


# Time Complexity = O(n)
# Space Complexity = O(h)



##############################################################


       
# Driver code
def main():
    list_of_trees = [ [TreeNode(2), TreeNode(1), TreeNode(4), TreeNode(3), TreeNode(5), TreeNode(6), TreeNode(7)],
                    [TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)],
                    [TreeNode(45), TreeNode(32), TreeNode(23), TreeNode(21), TreeNode(18), TreeNode(1)],
                    [TreeNode(8), TreeNode(5), TreeNode(9), TreeNode(4), TreeNode(6), None, TreeNode(10)],
                    [TreeNode(10), TreeNode(6), TreeNode(9), TreeNode(3), None, TreeNode(8), None, TreeNode(3)]
    ]

    k=[0, 1, 2, 1, 3]

    input_trees = []
    for list_of_nodes in list_of_trees:
        tree = BinaryTree(list_of_nodes)
        input_trees.append(tree)

    y = 1
    for i in range(len(input_trees)):
        print(y, ".\tInput Tree:", sep = "")
        display_tree(input_trees[i].root)
        print("\n\tk:", k[i],sep = "")
        print("\n\tResult: ", find_k_nodes(input_trees[i].root,k[i]), sep="")
        print("-"*100)
        y += 1

if __name__ == '__main__':
    main()