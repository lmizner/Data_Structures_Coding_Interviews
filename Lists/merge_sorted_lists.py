def merge_lists(nums1, nums2):
  
  # Check if nums1 list is empty
  if not nums1:
    return nums2
  
  # Check if nums2 list is empty
  if not nums2:
    return nums1

  # Initialze emtpy list for storing results
  results = []
  
  # Initialize two pointers
  nums1_pointer = 0
  nums2_pointer = 0
  
  # Traverse both lists until the end of either list is reached
  while nums1_pointer < len(nums1) and nums2_pointer < len(nums2):
    if nums1[nums1_pointer] < nums2[nums2_pointer]:
      results.append(nums1[nums1_pointer])
      nums1_pointer += 1 
    else:
      results.append(nums2[nums2_pointer])
      nums2_pointer += 1
      
  # Append any remaining elements from nums1
  while nums1_pointer < len(nums1):
    results.append(nums1[nums1_pointer])
    nums1_pointer += 1

  # Append any remaining elements from nums2
  while nums2_pointer < len(nums2):
    results.append(nums2[nums2_pointer])
    nums2_pointer += 1
  
  return results





# Driver code
def main():
    nums1 = [[23, 33, 35, 41, 44, 47, 56, 91, 105], [1, 2], [1, 1, 1], [6], [12, 34, 45, 56, 67, 78, 89, 99]]
    nums2 = [[32, 49, 50, 51, 61, 99], [7], [1, 2, 3, 4], [-99, -45], [100]]

    for i in range(len(nums1)):
        print(i+1,".\tFirst list: ", nums1[i])
        print("\tSecond list: ", nums2[i])
        print("\tMerged list: ", merge_lists(nums1[i], nums2[i]))
        print("-"*100)


if __name__ == "__main__":
    main()



# Time Complexity = O(m + n)
# Space Complexity = O(m + n)