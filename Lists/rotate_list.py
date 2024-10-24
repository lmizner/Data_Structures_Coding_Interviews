def right_rotate(nums, k):
    # If the list is empty, no rotation is needed
    if len(nums) == 0:
        k = 0 
    # Calculate the rotation amount    
    else:
        k = k % len(nums)

    # Perform rotation by slicing the list
    rotated_list = nums[-k:] + nums[:-k]

    return rotated_list





def main():
    inputs = [
        ([10, 20, 30, 40, 50]),  
        ([1, -2, 3, 4, 5]),  
        ([-1, 90, -90, 4, 6]),      
        ([3, 6, 9, -12]),          
        ([-100, -200, -300])         
    ]
    k= [3, 2, 6, 2, 1]
    
    for i in range(len(inputs)):
        print(i + 1, ".\tnums: ", inputs[i], sep="")
        print("\tk: ", k[i], sep="")
        print("\n\tRotated list: ", right_rotate(inputs[i], k[i]), sep="")
        print("-" * 70)

if __name__ == "__main__":
    main()



# Time Complexity = O(n)
# Space Complexity = O(1)