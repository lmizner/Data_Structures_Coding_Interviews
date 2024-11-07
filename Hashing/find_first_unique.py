def find_first_unique(nums):

    counts = {}

    # Count the occruences of each number in the input list
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    result = None

    # Find the first unique number in the input list
    for num in nums:

        # If the count of the number is 1, it's unqiue
        if counts[num] == 1:
            result = num
            return result



# Time Complexity = O(n)
# Space Complexity = O(n)



#####################################################################



# Driver Code
def main():

    inputs = [
            [9, 2, 3, 2, 6, 6],
            [-5, -4, -4, 6, -1],
            [-1, 2, -1, -4, -10],
            [1, 1, 2, 9],
            [-2, 2, -2, 2, 5]
            ]

    for i in range(len(inputs)):
        print(i + 1, ".\tInput list: ", inputs[i], sep="")
        print("\n\tfirst unique number: ", find_first_unique(inputs[i]), sep="")
        print("-" * 100)

if __name__ == "__main__":
    main()
