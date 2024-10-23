def find_second_maximum(nums):
  
  # Initialize first and second max variables
  first_max, second_max = float('-inf'), float('-inf')
  
  # Loop through list of nums
  for i in range(len(nums)):
    # First, check if value is the new first_max
    if nums[i] > first_max:
      second_max = first_max
      first_max = nums[i]
    # Next, check if value is the new second_max and doesn't equal first_max
    elif nums[i] > second_max and nums[i] != first_max:
      second_max = nums[i]
      
  return second_max





# Driver code
def main():
    inputs = [[9, 2, 3, 6],
            [1, 2],
            [-2, 2],
            [-4, -1, -9, 1, -7],
            [25, 50, 75, 100, 100]]

    for i in range(len(inputs)):
        print(i + 1, ".\tList: ", inputs[i], sep="")
        print("\n\tSecond maximum value: ", find_second_maximum(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()



# Time Complexity = O(n)
# Space Complexity = O(1)