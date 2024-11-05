def is_disjoint(list1, list2):

    # Initializing a set with list1 elements
    lookup = set(list1) 

    # Checking if list2 elements are in the set
    for elem in list2:
        if elem in lookup:
            # Return false if there is an element in list2 that is also in list1
            return False
    return True



# Time Complexity = O(m+n)
# Space Complexity = O(n)



#####################################################################



# Driver code
def main():

    inputs_list1 = [
            [2, 5, 10, 30, 45],
            [-5, -42, -31, -21, -10],
            [10, 20, -30, -40, 50],
            [100, 300],
            [500],

    ]

    inputs_list2 = [
            [3, 6, 13, 20, 23],
            [-1, -3, -5, -22, -15],
            [60, 70, 80, 90, 100],
            [300, 100],
            [200],

    ]

    for i in range(len(inputs_list1)):
        print(i + 1, ".\tList1: ", inputs_list1[i], sep="")
        print("\tList2: ", inputs_list2[i], sep="")
        print("\n\tResult: ", is_disjoint(inputs_list1[i], inputs_list2[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()


