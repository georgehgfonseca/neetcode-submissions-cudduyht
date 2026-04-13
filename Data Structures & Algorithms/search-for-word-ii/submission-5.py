class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False
        self.index = -1

    def add(self, word: str, index: int):
        root = self
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.isWord = True
        root.index = index

    def search(self, word: str):
        root = self
        for char in word:
            if char not in root.children:
                return -1
            root = root.children[char]
        
        return root.index if root.isWord else -1
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for i, word in enumerate(words):
            trie.add(word, i)

        foundIndexes = set()
        def dfs(i, j, trieNode):
            out_of_bounds = i < 0 or j < 0 or i >= len(board) or j >= len(board[i])
            if out_of_bounds or board[i][j] not in trieNode.children or (i, j) in visited:
                return
            
            visited.add((i, j))
            nextNode = trieNode.children[board[i][j]]

            if nextNode.isWord:
                foundIndexes.add(nextNode.index)

            dfs(i + 1, j, nextNode)
            dfs(i - 1, j, nextNode)
            dfs(i, j + 1, nextNode)
            dfs(i, j - 1, nextNode)
            visited.discard((i, j))
            
        # compute the words that can be found starting at each board cell
        for i in range(len(board)):
            for j in range(len(board[i])):
                visited = set()
                dfs(i, j, trie)

        return [words[i] for i in foundIndexes]
