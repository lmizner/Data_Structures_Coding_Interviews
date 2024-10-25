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
    




def find_bin(n):
    
    # Intialize empty list to store results
    result = []  

    # Create queue and start with '1' in the queue
    queue = MyQueue()
    queue.enqueue(1)

    # Loop to generate binary numbers up to 'n'
    for i in range(n):
        # Dequeue the front element of the queue
        result.append(str(queue.dequeue()))

        # Generate the next 2 binary numbers by appending '0' and '1' to the dequeued number
        s1 = result[i] + "0"
        s2 = result[i] + "1"

        # Enqueue the new binary numbers back into the queue
        queue.enqueue(s1)
        queue.enqueue(s2)

    return result





def main():
    inputs = [1, 3, 5, 9, 11]
    for i in range(len(inputs)):
        print(i+1, ".\tn: ", inputs[i], sep="")
        print("\n\tBinary numbers ", find_bin(inputs[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()