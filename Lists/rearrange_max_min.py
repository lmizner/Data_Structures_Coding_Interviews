def rearrange_list(nums):
    
    # Initialize empty list to store results
    results = []
    
    # Determine the middle of the list
    middle = len(nums) // 2
    
    # Loop through the list appending to results
    for i in range(middle):
        # Append largest value to results list
        results.append(nums[-(i+1)])
        # Append smallest value to results list
        results.append(nums[i])
        
    # Add middle if length is an odd number
    if len(nums) % 2 != 0:
        results.append(nums[middle])
        
    return results





def main():
    input_list = [[1, 2, 3, 4, 5, 6, 7, 8],
				  [11, 22, 33, 44, 55, 66, 77, 88],
				  [1, 2, 4, 8, 16, 32, 64, 128, 512, 1024],
				  [3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13],
				  [100, 233, 544, 753, 864, 935, 1933, 2342]]

    for i in range(len(input_list)):
        print(i + 1, ".\tOriginal list: ", input_list[i], sep='')
        print("\tRearranged list: ", rearrange_list(input_list[i]), sep='')
        print("-" * 100)


if __name__ == '__main__':
    main()
    


# Time Complexity = O(n)
# Space Complexity = O(1)

