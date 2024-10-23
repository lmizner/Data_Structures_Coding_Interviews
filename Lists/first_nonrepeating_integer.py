def find_first_unique(nums):
  
  for pointer_1 in range(len(nums)):
    
    # Reset pointer_2 for each loop of pointer_1 value
    pointer_2 = 0
    
    while pointer_2 < len(nums):
      if nums[pointer_1] == nums[pointer_2] and pointer_1 != pointer_2:
        break
      pointer_2 += 1
      
    if pointer_2 == len(nums):
      return nums[pointer_1]
      
  return None   





# Driver code
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



# Time Complexity = O(n^2)
# Space Complexity = O(1)