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
    




class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        self.temp_stack = MyStack()


    # Inserts the element in the queue
    def enqueue(self, value):
        # Push the value into main_stack in O(1)
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            self.main_stack.push(value)
        else:
            while not self.main_stack.is_empty():
                self.temp_stack.push(self.main_stack.pop())
            # Inserting the value in the queue
            self.main_stack.push(value)
            while not self.temp_stack.is_empty():
                self.main_stack.push(self.temp_stack.pop())


    # Removes the element from the queue
    def dequeue(self):
        # If stack is empty return None
        if self.main_stack.is_empty():
            return None
        # Otherwise continue removing values from stack, until empty
        value = self.main_stack.pop()
        return value





# Driver code
def main():
    calls = [["NewQueue","enqueue()","enqueue()","enqueue()","dequeue()"],
             ["NewQueue","enqueue()","dequeue()","enqueue()","dequeue()"],
             ["NewQueue","enqueue()","enqueue()","dequeue()","dequeue()"],
             ["NewQueue","enqueue()","enqueue()","dequeue()","enqueue()"],
             ["NewQueue","enqueue()","dequeue()","enqueue()","enqueue()"]
    
    ]

    inputs = [[None, 3, 4, 5, None],
              [None, -1, None, -4, None],
              [None, 200, 700, None, None],
              [None, -100, -100, None, -100],
              [None, 100000, None, -100000, 4000]
    ]

    for i in range(len(calls)):
        queue_obj = NewQueue()

        print(i + 1, ".\t Starting operations:", sep="")

        # Initialize a queue
        # Loop over all the commands
        for j in range(len(calls[i])):
            if calls[i][j] == "enqueue()":
                inputstr = "enqueue" + \
                    "("+str(inputs[i][j])+")"
                print("\t\t", inputstr, sep="")
                queue_obj.enqueue(inputs[i][j])
            if calls[i][j] == "dequeue()":
                inputstr = "dequeue" + \
                    "("+")"
                print("\t\t", inputstr, "   returns ",
                      queue_obj.dequeue(), sep="")

        print("-" * 100)


if __name__ == "__main__":
    main()


# Enqueue
# Time Complexity = O(n)
# Space Complexity = O(1)

# Dequeue
# Time Complexity = O(n)
# Space Complexity = O(1)