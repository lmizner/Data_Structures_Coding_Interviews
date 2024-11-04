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
            print("Key does not exist")
            return deleted_self

        # Base Case:
        # We have reached at the node which points
        # to the alphabet at the end of the key
        if level is length:
            # If there are no nodes ahead of this node in
            # this path, then we can delete this node
            print("Level is length, we are at the end")
            if current.children.count(None) == len(current.children):
                print("- Node", current.char, ": has no children, delete it")
                current = None
                deleted_self = True

            # If there are nodes ahead of current in this path
            # Then we cannot delete current. We simply unmark this as leaf
            else:
                print("- Node", current.char, ": has children, don't delete \
                it")
                current.is_end_word = False
                deleted_self = False

        else:
            index = self.get_index(key[level])
            print("Traverse to", key[level])
            child_node = current.children[index]
            child_deleted = self.delete_helper(
                key, child_node, length, level + 1)
            # print( "Returned from", key[level] , "as",  child_deleted)
            if child_deleted:
                # Setting children pointer to None as child is deleted
                print("- Delete link from", current.char, "to", key[level])
                current.children[index] = None
                # If current is a leaf node then
                # current is part of another key
                # So, we cannot delete this node and it's parent path nodes
                if current.is_end_word:
                    print("- - Don't delete node", current.char, ": word end")
                    deleted_self = False

                # If child_node is deleted and current has more children
                # then current must be part of another key
                # So, we cannot delete current Node
                elif current.children.count(None) != len(current.children):
                    print("- - Don't delete node", current.char, ": has \
                    children")
                    deleted_self = False

                # Else we can delete current
                else:
                    print("- - Delete node", current.char, ": has no children")
                    current = None
                    deleted_self = True

            else:
                deleted_self = False

        return deleted_self

    # Function to delete given key from Trie
    def delete(self, key):
        if self.root is None or key is None:
            print("None key or empty trie error")
            return
        print("\nDeleting:", key)
        self.delete_helper(key, self.root, len(key), 0)



######################################################################



# Recursive function to find all words in trie using depth-first search approach
def get_words(root, result, level, word):

    # If the current node marks the end of a word, construct word and add to result
    if root.is_end_word:
        # Construct word
        temp = ""
        for i in range(level):
            temp += word[i]
        # Add to result
        result.append(str(temp))

    # Cycle through alphabet
    for i in range(26):
        if root.children[i]:
            # Update the word array with the character at the current level
            word[level] = chr(i + ord('a'))

            # Recursively explore the child node
            get_words(root.children[i], result, level + 1, word)



def sort_list(trie):
    result = []
    word = [''] * 20
    get_words(trie.root, result, 0, word)
    return result



# Time Complexity = O(n)
# Space Complexity = O(n+m)



######################################################################



# Driver Code
def main():
    keys = [["gram", "grammar", "grain", "grainy", "grape"],
            ["absent", "absorb", "abstain", "abstract", "absurd"],
            ["dormant", "dormitory", "dormouse", "dormant", "dormant"],
            ["prey", "preach", "prepare", "prestige", "prestigious"],
            ["moon", "moose", "mood", "moot", "moor"]]
    i = 0
    print("Input: ", keys[i])
    for words in keys:
        t = Trie()
        for word in words:
            print("Insert: '", word, "'", sep="")
            t.insert(word)
        
        result = sort_list(t)
        print("\nOutput: ", result, "", sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()


