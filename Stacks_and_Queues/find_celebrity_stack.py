class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return self.stack_size
    
    def push(self, value):
        self.stack_size += 1
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -= 1
        return self.stack_list.pop()





def knows(matrix, x, y):
    # Returns True if x knows y, else returns False
    return matrix[x][y] == 1

def find_celebrity(matrix, n):

    # Initialize Stack
    stack = MyStack()
    celebrity = -1

    # Loop through all n individuals, adding them to the stack
    for i in range(n):
        stack.push(i)

    while not stack.is_empty():
        x = stack.pop()
        
        if stack.is_empty():
            celebrity = x
            break

        y = stack.pop()

        if knows(matrix, x, y):
            # x knows y, discard x and push y back in stack
            stack.push(y)
        else:
            # y is discarded, x is pushed back
            stack.push(x)

    # Verify the potential celebrity
    for j in range(n):
        # A celebrity knows no one, and everyone knows the celebrity
        if celebrity != j and (knows(matrix, celebrity, j) or not knows(matrix, j, celebrity)):
            return -1
    
    return celebrity





def main():
    matrixes = [
        [ # matrix 1
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [0, 0, 0, 0],
            [0, 1, 1, 0]
        ],
        [ # matrix 2
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [0, 0, 0, 1],
            [0, 1, 1, 0]
        ],
        [ # matrix 3
            [0, 0, 0, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 0]
        ],

        [ # matrix 4
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0]
        ],

        [ # matrix 5
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]

        ]        

    ]

    n = [4, 4, 4, 4, 5]

    for i in range(5):
        print(i+1, ".\tInput matrix:", matrixes[i])
        print("\tCelebrity:", find_celebrity(matrixes[i], n[i]))
        print("-"*100)

if __name__ == "__main__":
    main()



# Time Complexity = O(n)
# Space Complexity = O(n)