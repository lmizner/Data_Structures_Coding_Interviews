def find_sub_zero(lst):

    ht = dict()
    total_sum = 0

    for elem in lst:
        total_sum += elem
        if elem == 0 or total_sum == 0 or ht.get(total_sum) != None:
            return True
        ht[total_sum] = elem

    return False



# Time Complexity = O(n)
# Space Complexity = O(n)



#####################################################################



# Driver Code
def main():
    inputs = [[10, 4, 10, -56, 23, 7, 2, -2, 9],
              [-3, 3],
              [2, -5, -4, 43, 2],
              [-7, 1, 2, 5, -6 , 1, -3, 3, -17],
              [25, 50, 75, 100, 400]]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\n\tResult: ", find_sub_zero(inputs[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()

