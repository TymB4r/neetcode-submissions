from typing import List


class Node:
    def __init__(self, letter = ""):
        self.is_end_of_word = False
        self.letter_to_child = {}
        self.letter = letter

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.letter_to_child:
                curr.letter_to_child[letter] = Node(letter)
            curr = curr.letter_to_child[letter]

        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for letter in word:
            if letter not in curr.letter_to_child:
                return False
            curr = curr.letter_to_child[letter]

        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for letter in prefix:
            if letter not in curr.letter_to_child:
                return False
            curr = curr.letter_to_child[letter]

        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def search_from_point(start_row: int, start_col: int) -> List[str]:
            found_paths = []
            visited = set()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            def recur(node: Node, row: int, col: int, path: List[str]) -> None:
                if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0])) or (row, col) in visited:
                    return

                target_char = board[row][col]

                if target_char not in node.letter_to_child:
                    return

                node = node.letter_to_child[target_char]

                visited.add((row, col))
                path.append(node.letter)

                if node.is_end_of_word:
                    found_paths.append(path.copy())

                for d in directions:
                    new_row, new_col = row + d[0], col + d[1]
                    if (new_row, new_col) not in visited:
                        recur(node, new_row, new_col, path)

                path.pop()
                visited.remove((row, col))

            recur(dictionary.root, start_row, start_col, [])

            result = []
            for ele in found_paths:
                result.append("".join(ele))
            return result


        dictionary = PrefixTree()
        for word in words:
            dictionary.insert(word)

        found_set = set()

        for row in range(len(board)):
            for col in range(len(board[row])):
                for word in search_from_point(row, col):
                    found_set.add(word)


        return list(found_set)