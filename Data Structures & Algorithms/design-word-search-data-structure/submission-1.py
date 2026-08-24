class Node:
    def __init__(self, letter = ''):
        self.is_end_of_word = False
        self.letter_to_child = {}

class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        curr = self.head

        for letter in word:
            if letter not in curr.letter_to_child:
                curr.letter_to_child[letter] = Node()
            curr = curr.letter_to_child[letter]

        curr.is_end_of_word = True



    def search(self, word: str) -> bool:
        def traverse(curr: Node, idx: int) -> bool:
            if idx == len(word):
                return curr.is_end_of_word

            char = word[idx]

            if char != ".":
                if char not in curr.letter_to_child:
                    return False
                if idx == len(word):
                    return curr.is_end_of_word

                curr = curr.letter_to_child[char]
                return traverse(curr, idx + 1)
            else:
                for child in curr.letter_to_child.values():
                    if traverse(child, idx + 1):
                        return True
                return False


        return traverse(self.head, 0)