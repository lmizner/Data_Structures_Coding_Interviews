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





def sort_stack(stack):
    
    # Initialize an empty temp_stack to store results
    temp_stack = MyStack()
    
    # Once an item is in the temp stack, loop through stack items until stack is empty
    while not stack.is_empty():
        current_value = stack.pop()
        # Check if current value is greater than temp_stack, if so add it 
        if temp_stack.peek() is not None and current_value <= temp_stack.peek():
            temp_stack.push(current_value)
        else:
            # Check if current value is less, if so, move larger temp stack values back to stack
            while not temp_stack.is_empty() and current_value > temp_stack.peek():
                stack.push(temp_stack.pop())
            # Then add current value to temp stack
            temp_stack.push(current_value)
        
    return temp_stack





def main():
    inputs = [
        [10, 30, 5, 20, 50],
        [-1, -2, -3, -4, -5, -6],
        [3, 2, -1],
        [12],
        [1, -2],
    ]

    for stack_values in inputs:
        stack = MyStack()
        for value in stack_values:
            stack.push(value)
        print("Original Stack:", stack_values)  # Print the original stack values from inputs array
        sorted_stack = sort_stack(stack)
        sorted_items = [sorted_stack.pop() for _ in range(sorted_stack.size())]
        print("Sorted Stack:", sorted_items)  # Print the sorted stack using pop()
        print("-" * 75)


if __name__ == "__main__":
    main()



# Time Complexity = O(n^2)
# Space Complexity = O(n)
