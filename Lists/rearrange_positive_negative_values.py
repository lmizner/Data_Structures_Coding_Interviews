def rearrange(lst):
  
  # Initialize a list for negative values and positive values
  negative = []
  positive = []

  for i in range(len(lst)):
    if lst[i] < 0:
      negative.append(lst[i])
    else:
      positive.append(lst[i])
        
  return negative + positive





def main():
    inputs = [[10, 4, 6, 23, 7],
              [-3, 20, -1, 8],
              [2, -5, -4, 43, 2],
              [-3, -10, -19, 21, -17],
              [25, 50, 75, -100, 400]]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\n\tResult: ", rearrange(inputs[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()



# Time Complexity = O(n)
# Space Complexity = O(n)