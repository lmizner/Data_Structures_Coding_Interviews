class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26
        self.is_end_word = False
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, t):
        return ord(t) - ord('a')

    def insert(self, key):
        if key is None:
            return False

        key = key.lower()
        current = self.root

        for letter in key:
            index = self.get_index(letter)

            if current.children[index] is None:
                current.children[index] = TrieNode(letter)

            current = current.children[index]

        current.is_end_word = True

    def search(self, key):
        if key is None:
            return False

        key = key.lower()
        current = self.root

        for letter in key:
            index = self.get_index(letter)
            if current.children[index] is None:
                return False
            current = current.children[index]

        if current is not None and current.is_end_word:
            return True

        return False

    def delete_helper(self, key, current, length, level):
        deleted_self = False

        if current is None:
            return deleted_self

        if level is length:
            if current.children.count(None) == len(current.children):
                current = None
                deleted_self = True
            else:
                current.is_end_word = False
                deleted_self = False

        else:
            index = self.get_index(key[level])
            child_node = current.children[index]
            child_deleted = self.delete_helper(
                key, child_node, length, level + 1)
            if child_deleted:
                current.children[index] = None
                if current.is_end_word:
                    deleted_self = False
                elif current.children.count(None) != len(current.children):
                    deleted_self = False
                else:
                    current = None
                    deleted_self = True
            else:
                deleted_self = False

        return deleted_self

    def delete(self, key):
        if self.root is None or key is None:
            return
        self.delete_helper(key, self.root, len(key), 0)



######################################################################



# Recursive function to get maximum depth of trie
def get_max_depth(root, level):

    # If root is null, return the current level
    if not root:
        return level
    
    max_depth = level

    for child in root.children:
        if child:
            # Recursively calculate the maximum depth of the subtree
            max_depth = max(max_depth, get_max_depth(child, level + 1))

    return max_depth


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


# Helper Function to call get_words
def find_words(root):
    result = []
    word = [None] * get_max_depth(root, 0)
    get_words(root, result, 0, word)
    return result



# Time Complexity = O(n)
# Space Complexity = O(n+m)



######################################################################



# Driver Code
def main():
    num = 1
    words = [["gram", "groom", "ace", "act", "actor"],
            ["abs", "crow", "crop", "abstain", "crunch"],
            ["dorm", "norm", "prom", "loom", "room"],
            ["prey", "prep", "press", "preps", "prefix"],
            ["moon", "once", "face", "dice", "mole"]]
    
    for word in words:
        t = Trie()
        for w in word:
            print("Insert word: '", w, "'", sep="")
            t.insert(w)
            num += 1
            words_found = find_words(t.root)
        print("\nWords found: ", words_found, sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
