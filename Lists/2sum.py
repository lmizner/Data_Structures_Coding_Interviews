def find_sum(nums, k):
  
    # Sort nums in ascending order
    nums.sort()
    
    # Initialize empty list to store results
    results = []
    
    # Initialize two pointers, one for start and one for end 
    start = 0
    end = len(nums) - 1
    
    # While no solution
    while nums[start] + nums[end] != k:
      # If sum is less than k, increment the start pointer 1
      if nums[start] + nums[end] < k:
        start += 1
      # If sum is greater than k, increment the end pointer -1
      else:
        end -= 1
    
    # Once solution is found, append start and end values to results
    results.append(nums[start])
    results.append(nums[end])
    
    return results





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



# Time Complexity = O(n)
# Space Complexity = O(1)