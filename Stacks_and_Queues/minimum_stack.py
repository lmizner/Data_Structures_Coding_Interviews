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
    




class MinStack:
    # Initialize min and main stack here
    def __init__(self):

        # Initialize two empty stacks
        self.min_stack = MyStack()
        self.main_stack = MyStack()


    # Remove and returns value from the stack
    def pop(self):

        # Pop from both stacks, and return value from main_stack
        self.min_stack.pop()
        return self.main_stack.pop()


    # Pushes values into the stack
    def push(self, value):

        # Push new value onto main stack
        self.main_stack.push(value)

        if self.min_stack.is_empty() or self.min_stack.peek() > value:
            # Push new value onto min stack
            self.min_stack.push(value)
        else:
            # Push top value onto min stack
            self.min_stack.push(self.min_stack.peek())


    # Returns minimum value from stack
    def min(self):
        return self.min_stack.peek()
        





# Driver code
def main():
    calls = [["MinStack","push()","push()","min()","pop()"],
             ["MinStack","push()","pop()","push()","min()"],
             ["MinStack","push()","push()","push()","push()", "pop()","min()"],
             ["MinStack","push()","min()","push()"],
             ["MinStack","push()","push()","min()","push()","min()"]
    
    ]

    inputs = [[None, 3, 7, None, 7],
              [None, -1, None, -4, None],
              [None, 100, 300, -200, -140, None, None],
              [None, 100000, None, -100000],
              [None, 54, 89, None, 45, None]
    ]

    for i in range(len(calls)):
        stack_obj = MinStack()

        print(i + 1, ".\t Starting operations:", sep="")

        # initialize a queue
        # loop over all the commands
        for j in range(len(calls[i])):
            if calls[i][j] == "push()":
                inputstr = "push" + \
                    "("+str(inputs[i][j])+")"
                print("\t\t", inputstr, sep="")
                stack_obj.push(inputs[i][j])
            elif calls[i][j] == "pop()":
                inputstr = "pop" + \
                    "("+")"
                print("\t\t", inputstr, "   returns ",
                      stack_obj.pop(), sep="")
            elif calls[i][j] == "min()":
                inputstr = "min" + \
                    "("+")"
                print("\t\t", inputstr, "   returns ",
                      stack_obj.min(), sep="")

        print("-" * 100)


if __name__ == "__main__":
    main()
    


# Time Complexity = O(1)
# Space Complexity = O(n)