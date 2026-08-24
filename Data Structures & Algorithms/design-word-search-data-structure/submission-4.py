class Node:
    def __init__(self):
        self.is_end_of_word = False
        self.letter_to_child = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.letter_to_child:
                curr.letter_to_child[letter] = Node()
            curr = curr.letter_to_child[letter]

        curr.is_end_of_word = True


    def search(self, word: str) -> bool:
        def traverse(node: Node, idx: int) -> bool:
            if idx == len(word):
                return node.is_end_of_word

            char = word[idx]
            if char != ".":
                if char not in node.letter_to_child:
                    return False

                node = node.letter_to_child[char]
                return traverse(node, idx + 1)
            else:
                for child in node.letter_to_child.values():
                    if traverse(child, idx + 1):
                        return True
                return False

        return traverse(self.root, 0)