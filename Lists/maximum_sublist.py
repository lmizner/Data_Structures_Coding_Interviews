def find_max_sum_sublist(nums):
  
  # If nums is empty
  if len(nums) < 1: 
    return 0
  
  current_max = nums[0]
  global_max = nums[0]

  for i in range(1, len(nums)):
    # If current_max is less than zero, then reset current max to nums[i]
    if current_max < 0:
      current_max = nums[i]
    # Otherwise add it to the current max
    else:
      current_max += nums[i]
    
    # Update global max whenever a new global max is found
    if current_max > global_max:
      global_max = current_max
    
  return global_max





# Driver code
def main():
    inputs = [[1, 2, 2, 3, 3, 1, 4], [2, 2, 1], [4, 1, 2, 1, 2], [-4, -1, -2, -1, -2],[-4, 2, -5, 1, 2, 3, 6, -5, 1], [25]]

    for i in range(len(inputs)):
        print(i + 1, ".\tList: ", inputs[i], sep="")
        print("\tMaximum Sum: ", find_max_sum_sublist(inputs[i]), sep="")
        print("-" * 75)


if __name__ == "__main__":
    main()



# Time Complexity = O(n)
# Space Complexity = O(1)