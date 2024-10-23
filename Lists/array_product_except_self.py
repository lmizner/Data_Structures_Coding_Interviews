def find_product(nums):
  
  # Initialize empty list to store results
  results =[]  
  
  # Loop through the nums list
  for pointer in range(len(nums)):
      # Reset product for each index
      product = 1
      
      for i in range(len(nums)):
          if i != pointer:
              product *= nums[i]
      
      results.append(product)

  return results





def main():
    inputs = [
        [1, 2, 3, 4],   
        [5, -3, 1, 2],   
        [2, 2, 2, 0],      
        [0, 0, 0, 0],   
        [-1, -2, -4]     
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\n\tList of products: ", find_product(inputs[i]), sep="")
        print("-" * 100)

if __name__ == "__main__":
    main()



# Time Complexity = O(n^2)
# Space Complexity = O(1)