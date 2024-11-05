def is_subset(list1, list2):

    set_list1  = set(list1) 

    # Traverse list2 elements and return True if all elements of list2 are found in set set_list1
    for elem in list2:
        if elem not in set_list1 :
            return False

    return True



# Time Complexity = O(m+n)
# Space Complexity = O(n)



#####################################################################



if __name__ == "__main__":
    list1 = [
        [9, 4, 7, 1, -2, 6, 5],
        [34, 19],
        [1, 2, 5, 0, 7, 4, 23],
        [-4, 6, 8, 1, 3, 14, 5, 7, 29],
        [52, 57, 23, -6, 22, -16, 78, 98, 46, 24, 19]
    ]
    list2 = [
        [7, 1, -2],
        [34],
        [],
        [14, -4, 29],
        [7, -6, 8, -4]
    ]
    for i in range(len(list1)):
        print(i+1, "\tList1:: ", list1[i])
        print("\tList2:: ", list2[i])
        result = is_subset(list1[i], list2[i])
        print("\tOutput:" , result)
        print("-" * 100)
