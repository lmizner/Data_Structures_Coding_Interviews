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
    




def apply_operator(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 // num2  

def evaluate_post_fix(exp):

    # Initialize empty stack 
    stack = MyStack()

    for char in exp:
        if char.isdigit():
            # Push numbers in stack
            stack.push(int(char))
        else:
            # Pop top two numbers from stack
            right = stack.pop()
            left = stack.pop()
            # Apply operator to operands and push result back to stack
            result = apply_operator(char, left, right)
            stack.push(result)

    # Final result is at the top of the stack
    return stack.pop()





# Driver Code
def main():

    i = 1
    for case in test_cases:
        print(i, ".\tExpression: ", case, sep="")
        result = evaluate_post_fix(case)
        print("\tResult: ", result)
        print("-"*100)
        i+=1

if __name__ == "__main__" :
    test_cases = ["921*-8-4+", "53+62/*35*+", "543-3*+", "82/3-31*+", "92+31*-"]



# Time Complexity = O(n)
# Space Complexity = O(n)