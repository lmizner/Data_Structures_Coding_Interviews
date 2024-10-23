def find_minimum_sort(lst):
    lst.sort()  # Sort the list in ascending order
    return lst[0]  # Return the first element

# Time Complexity = O(n log n)
# Space Complexity = O(n)



def find_minimum(lst):
    # Set the minimum to the first value in the list
    minimum = lst[0]

    # Iterate through the rest of the list, replacing with new minimum as necessary
    for i in range(1, len(lst)):
        minimum = min(minimum, lst[i])

    return minimum

# Time Complexity = O(n)
# Space Complexity = O(1)



# Driver code
def main():

    inputs = [
        [9],
        [-1, -5, -10, -2, -4],
        [4, 3, 2, 1],
        [2, 3, 3, -1, -1],
        [100, 50, 75, 25, 400]
            
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tInput list: ", inputs[i], sep="")
        print("\n\tMinimum element: ", find_minimum(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()

