def is_formation_possible(words_list, target):

    # Initialize an empty hash table
    hash_table = {}

    # Insert each word from the list into the hash table as a key
    for word in words_list:
        hash_table[word] = True

    # Iterate over each index of the word to check for possible formations
    for i in range(1, len(target)):
        prefix = target[:i]
        suffix = target[i:]

        # Check if both prefix and suffix exist as keys in the hash table
        if hash_table.get(prefix) and hash_table.get(suffix):
            return True
        
    return False



# Time Complexity = O(n+m)
# Space Complexity = O(n)



#####################################################################



# Driver Code
def main():
    words_list = [["flower", "moon", "plant", "sun", "star"],
                  ["sand", "water", "fly"],
                  ["paper", "pen", "book", "page", "note", "pencil"],
                  ["door", "light", "window", "balcony", "attic", "roof"],
                  ["bow", "rain"]]
    targets = ["sunflower", "waterfall", "notebook", "lighthouse", "rainbow"]

    for i in range(len(words_list)):
        print("Words in the table:", words_list[i])
        print("Target word:", targets[i])
        print("Found:", is_formation_possible(words_list[i], targets[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()