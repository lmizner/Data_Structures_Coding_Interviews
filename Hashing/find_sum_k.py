def find_sum(nums, k):

    found_values = {}

    for num in nums:

        # Calculate the complement needed to reach the target sum k
        complement = k - num

        # Check if the complement is in found_values dictionary
        if complement in found_values:

            # If found, return pair
            return [complement, num]

        # Add current number to found_values dictionary
        found_values[num] = 0

    return []



# Time Complexity = O(n)
# Space Complexity = O(n)



#####################################################################



# Driver code
def main():
    inputs = [[1, 2, 3, 4],
            [1, 2],
            [2, 2],
            [-4, -1, -9, 1, -7],
            [25, 50, 75, 100, 400]]

    k = [5, 3, 4, -3, 425]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\tk: ", k[i], sep="")
        print("\n\tResult: ", find_sum(inputs[i], k[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
