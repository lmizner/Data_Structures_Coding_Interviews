class MyQueue:
    def __init__(self):
        self.queue_list = []
        self.queue_size = 0

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def size(self):
        return self.queue_size
    
    def enqueue(self, value):
        self.queue_size += 1
        self.queue_list.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self.queue_list.remove(self.front())
        self.queue_size -= 1
        return front
    

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
    




def reverse_k_elements(queue, k):

    if k < 0 or k > queue.size() or queue.is_empty() is True:
        return queue

    # Initialize Stack to store first k elements
    stack = MyStack()
    results = MyQueue()

    # Loop through the first k elements in queue and add to stack
    for i in range(k):
        stack.push(queue.dequeue())

    # Then loop through stack, removing elements until empty
    while stack.is_empty() is False:
        results.enqueue(stack.pop())
    
    while queue.is_empty() is False:
        results.enqueue(queue.dequeue())

    return results


            


# Driver Code
def main():
    test_cases = [
        [1,2,3,4,5,6,7,8,9,10],
        [-2,1,-5,45,6,3,-9],
        [1,2,5,0,7,4,23],
        [7,3,5,6,8,12],
        [5,67,43,23,12,56,78,98,6,21,9]
    ]
    k_values = [4, 10, -7, 5, 2]
    for i in range(len(test_cases)):
        queue = MyQueue()
        for item in test_cases[i]:
            queue.enqueue(item)
        k = k_values[i]
        print(i+1, "\tOriginal Queue:", queue.queue_list)
        print("\tk value:", k)
        reversed_queue = reverse_k_elements(queue, k)
        print("\tQueue after reversal:" , reversed_queue.queue_list)
        print("-"*100)

if __name__ == '__main__':
    main()



# Time Complexity = O(n)
# Space Complexity = O(n)