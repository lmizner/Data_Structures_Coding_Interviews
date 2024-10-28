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




def is_balanced(exp):
    
    # Define Closing parentheses
    closing = ['}', ')', ']']

    # Initialize stack
    stack = MyStack()

    # Loop through the string of characters
    for character in exp:
        if character in closing:
            # If the stack is empty, return False
            if stack.is_empty():
                return False
            
            # Otherwise, check if it matches the open parenthesis from the stack
            top_element = stack.pop()

            if character == '}' and top_element != '{':
                return False
            elif character == ')' and top_element != '(':
                return False
            elif character ==']' and top_element != '[':
                return False

        else:
            # If the character is an open parantheses, add it to the stack
            stack.push(character)

    # Check if stack is empty or not after checking full string
    if not stack.is_empty():
        return False
    
    return True



def main():
    parentheses = ["(){}[]",
                   "[{()}]",
                   "]}){{()}({[",
                   "[[{{((}])}])",
                   ")))))"]

    for i in range(len(parentheses)):
        print(i + 1, ".\tCheck balanced parentheses: '" + "".join(parentheses[i]), "'", sep='')
        result = is_balanced(parentheses[i])

        print("\tIs the string balanced?", result)
        print("-" * 100)


if __name__ == '__main__':
    main()



# Time Complexity = O(n)
# Space Complexity = O(n) 