def min_heapify(max_heap, index):

    # Calculate the left and right child indices
    left = (index * 2) + 1
    right = (index * 2) + 2
    smallest = index

    # Check if left child is within heap bounds and smaller than current
    if len(max_heap) > left and max_heap[smallest] > max_heap[left]:
        smallest = left

    # Check if the right child is within heap bounds and smaller than current
    if len(max_heap) > right and max_heap[smallest] > max_heap[right]:
        smallest = right

    # Swap smallest element with current index (if needed) and recursively call min_heapify
    if smallest != index:
        temp = max_heap[smallest]
        max_heap[smallest] = max_heap[index]
        max_heap[index] = temp
        min_heapify(max_heap, smallest)

    return max_heap


# Convert max heap to min heap
def convert_max(max_heap):

    for i in range((len(max_heap)) // 2, -1, -1):
        max_heap = min_heapify(max_heap, i)

    return max_heap



# Time Complexity = O(n)
# Space Complexity = O(1)



########################################################################


# Driver code
def main():
    max_heaps = [[9, 4, 7, 1, -2, 6, 5],
                [468, 397, 361, 336, 324, 318],
                [1000, 800, 500, -900, -1000],
                [5, 4, 3, 2, 1],
                [[10, 9, 6, 2, -3, -12, -14]]]

    for i in range(len(max_heaps)):
        print(i+1,".", "\tGiven Max heap: ", max_heaps[i])
        print("\tConverted Min heap: ", convert_max(max_heaps[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()
