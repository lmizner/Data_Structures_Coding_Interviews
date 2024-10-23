def remove_even(lst):
  result = []  
  for i in range(len(lst)):
    if lst[i] % 2 != 0:
      result.append(lst[i])
  return result


def main():

    inputs = [
            [3, 2, 41, 3, 34],
            [-5, -4, -3, -2, -1],
            [-1, 2, 3, -4, -10],
            [1, 2, 3, 7],
            [2, 4, 6, 8, 10],

    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tInput list: ", inputs[i], sep="")
        print("\n\tFinal list: ", remove_even(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()



# Time Complexity = O(n)
# Space Complexity = O(1)