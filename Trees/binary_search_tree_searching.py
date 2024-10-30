import random

class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, val):
        if self is None:
            self = Node(val)
            return
        current = self

        while current:
            parent = current
            if val < current.val:
                current = current.leftChild
            else:
                current = current.rightChild

        if(val < parent.val):
            parent.leftChild = Node(val)
        else:
            parent.rightChild = Node(val)

    def search(self, val):
        current = self
        while current is not None:
            if val < current.val:
                current = current.leftChild
            elif val > current.val:
                current = current.rightChild
            else:
                return True
        return False



##############################################################



# Insert Implementation (Recursive)
class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True

    def search(self, val):
        if self.root:
            return self.root.search(val)
        else:
            return False



##############################################################



# Insert Implementation (Iterative)
def display(node):
    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)


def _display_aux(node):
    """
    Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # No child.
    if node.rightChild is None and node.leftChild is None:
        line = str(node.val)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.rightChild is None:
        lines, n, p, x = _display_aux(node.leftChild)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.leftChild is None:
        lines, n, p, x = _display_aux(node.rightChild)
        s = str(node.val)
        u = len(s)
        # first_line = s + x * '_' + (n - x) * ' '
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.leftChild)
    right, m, q, y = _display_aux(node.rightChild)
    s = '%s' % node.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * \
        '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + \
        (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + \
        [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


BST = BinarySearchTree(50)
for _ in range(15):
    ele = random.randint(0, 100)
    BST.insert(ele)
# We have hidden the code for this function but it is available for use!
display(BST.root)
print('\n')
print(BST.search(50))  # Will print True since 50 is the root
print(BST.search(11))  # May or may not be True. Check the tree!
