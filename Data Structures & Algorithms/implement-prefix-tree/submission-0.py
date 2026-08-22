class Node:
    def __init__(self, letter = ""):
        self.letter = letter
        self.last_of_word = False
        self.letter_to_child = {}


class PrefixTree:

    def __init__(self, letter=""):
        self.head = Node(letter)

    def insert(self, word: str) -> None:
        curr = self.head
        
        for letter in word:
            if letter not in curr.letter_to_child:
                curr.letter_to_child[letter] = Node(letter)
            curr = curr.letter_to_child[letter]
            
        curr.last_of_word = True

    def search(self, word: str) -> bool:
        curr = self.head
        
        for letter in word:
            if letter not in curr.letter_to_child:
                return False
            curr = curr.letter_to_child[letter]

        return curr.last_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        
        for letter in prefix:
            if letter not in curr.letter_to_child:
                return False
            curr = curr.letter_to_child[letter]
            
        return True