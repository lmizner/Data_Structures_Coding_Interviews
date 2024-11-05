def find_symmetric(nums):
    
    # Create an empty set
    lookup = set()
    result = []
    
    # Traverse through the given list
    for pair in nums:
        
        # Make a tuple and a reverse tuple out of the pair
        current_pair = tuple(pair)
        pair.reverse()
        reverse_pair = tuple(pair)
        
        # Check if the reverse tuple exists in the set
        if(reverse_pair in lookup):
            
            # Symmetric pair found
            result.append(list(current_pair))
            result.append(list(reverse_pair))
        
        else:
            
            # Insert the current tuple into the set
            lookup.add(current_pair)
    
    return result



# Time Complexity = O(n)
# Space Complexity = O(n)



#####################################################################



# Driver Code
def main():
    test_cases = [
        [[1, 2], [4, 6], [4, 3], [6, 4], [5, 9], [3, 4], [9, 5]],
        [[1, 2], [2, 1], [3, 4], [5, 5], [6, 7]],
        [[1, 9], [9, 1]],
        [[1, 2], [3, 4], [5, 6]],
        [[-8, -4], [7, 7], [1, 1], [2, 2], [-4, -8]]
    ]
    i = 1
    for case in test_cases:
        print(i, ".\tInput list: ", case, sep="")
        symmetric = find_symmetric(case)
        print("\n\tSymmetric pairs: ", symmetric)
        print("-"*100)
        i+=1

if __name__ == "__main__":
    main()