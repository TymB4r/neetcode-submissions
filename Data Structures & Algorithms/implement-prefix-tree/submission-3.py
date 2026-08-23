class Node:
    def __init__(self):
        self.is_end_of_word = False
        self.letter_to_child = {}


class PrefixTree:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        curr = self.head

        for letter in word:
            if letter not in curr.letter_to_child:
                curr.letter_to_child[letter] = Node()
            curr = curr.letter_to_child[letter]

        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.head

        for letter in word:
            if letter not in curr.letter_to_child:
                return False
            curr = curr.letter_to_child[letter]

        return curr.is_end_of_word # This works, because only one path can be taken to follow each word

    def startsWith(self, prefix: str) -> bool:
        curr = self.head

        for letter in prefix:
            if letter not in curr.letter_to_child:
                return False
            curr = curr.letter_to_child[letter]

        return True