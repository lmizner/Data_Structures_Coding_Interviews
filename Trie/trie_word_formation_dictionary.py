class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26  # This will store pointers to the children
        self.is_end_word = False  # true if the node represents the end of word
        self.char = char  # To store the value of a particular key


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node

    # Function to get the index of character 't'
    def get_index(self, t):
        return ord(t) - ord('a')

    # Function to insert a key in the Trie
    def insert(self, key):
        if key is None:
            return False  # None key

        key = key.lower()  # Keys are stored in lowercase
        current = self.root

        # Iterate over each letter in the key
        # If the letter exists, go down a level
        # Else simply create a TrieNode and go down a level
        for letter in key:
            index = self.get_index(letter)

            if current.children[index] is None:
                current.children[index] = TrieNode(letter)

            current = current.children[index]

        current.is_end_word = True

    # Function to search a given key in Trie
    def search(self, key):
        if key is None:
            return False  # None key

        key = key.lower()
        current = self.root

        # Iterate over each letter in the key
        # If the letter doesn't exist, return False
        # If the letter exists, go down a level
        # We will return true only if we reach the leafNode and
        # have traversed the Trie based on the length of the key

        for letter in key:
            index = self.get_index(letter)
            if current.children[index] is None:
                return False
            current = current.children[index]

        if current is not None and current.is_end_word:
            return True

        return False

    # Recursive function to delete given key
    def delete_helper(self, key, current, length, level):
        deleted_self = False

        if current is None:
            return deleted_self

        # Base Case:
        # We have reached at the node which points
        # to the alphabet at the end of the key
        if level is length:
            # If there are no nodes ahead of this node in
            # this path, then we can delete this node
            if current.children.count(None) == len(current.children):
                current = None
                deleted_self = True

            # If there are nodes ahead of current in this path
            # Then we cannot delete current. We simply unmark this as leaf
            else:
                current.is_end_word = False
                deleted_self = False

        else:
            index = self.get_index(key[level])
            child_node = current.children[index]
            child_deleted = self.delete_helper(
                key, child_node, length, level + 1)
            # print( "Returned from", key[level] , "as",  child_deleted)
            if child_deleted:
                # Setting children pointer to None as child is deleted
                current.children[index] = None
                # If current is a leaf node then
                # current is part of another key
                # So, we cannot delete this node and it's parent path nodes
                if current.is_end_word:
                    deleted_self = False

                # If child_node is deleted and current has more children
                # then current must be part of another key
                # So, we cannot delete current Node
                elif current.children.count(None) != len(current.children):
                    deleted_self = False

                # Else we can delete current
                else:
                    current = None
                    deleted_self = True

            else:
                deleted_self = False

        return deleted_self

    # Function to delete given key from Trie
    def delete(self, key):
        if self.root is None or key is None:
            return
        self.delete_helper(key, self.root, len(key), 0)



######################################################################



def is_formation_possible(dictionary, word):
    
    # Create a trie and insert dictionary elements into it
    trie = Trie()
     
    for element in dictionary:
        trie.insert(element)

    # Obtain root of trie
    current = trie.root

    # Iterate over all letters of the word
    for i in range(len(word)):

        # Obtain index of the character from trie
        char = trie.get_index(word[i])

        # Check if prefix of word exists, if not return False
        if current.children[char] is None:
            return False

        # If prefix does exist, check if rest of word exists
        elif current.children[char].is_end_word:
            if trie.search(word[i+1:]):
                return True

        # Update current to the next node   
        current = current.children[char]

    return False



# Time Complexity = O(m+n)
# Space Complexitt = O(m)



######################################################################



# Driver code
def main():
    inputs = [ ["he","hello","home","work"],
               ["play","plot","bat"],
               ["p","q","r"],
               ["abc","def"],
               ["add","addi","number"]
    ]

    words =  ["hehome", "world", "pr", "abcdef", "subtract"]
    

    for i in range(len(inputs)):
        print("\tDictionary: ", inputs[i], sep="")
        print("\tword: ", words[i], sep="")
        print("\n\tResult: ", is_formation_possible(inputs[i], words[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()


