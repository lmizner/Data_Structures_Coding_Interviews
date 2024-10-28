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





def next_greater_element(lst):
    stack = MyStack()
    res = [-1] * len(lst)

    # Loop through elements, starting at last index and moving backwards to the first index
    for i in range(len(lst) - 1, -1, -1):
        # While stack has elements and the current element is greater 
        # than top element, pop all elements
        while not stack.is_empty() and stack.peek() <= lst[i]:
            stack.pop()

        # If the stack has an element, the top element will be 
        # greater than ith element
        if not stack.is_empty():
            res[i] = stack.peek()
        stack.push(lst[i])
        
    return res





def main():
    inputs = [[4, 6, 3, 2, 8, 1, 9, 9, 9],
              [33, 20, 105, 88],
              [12, 5, 44, 56, 46, 78],
              [1, 2, 3, 4, 5],
              [150, 125, 100, 75, 50, 25, 0]]

    for i in range(len(inputs)):
        print(i + 1, ".\tList: ", inputs[i], sep="")
        print("\n\tResult: ", next_greater_element(inputs[i]))
        print("-" * 100)

if __name__ == "__main__":
    main()



# Time Complexity = O(n)
# Space Complexity = O(n)

