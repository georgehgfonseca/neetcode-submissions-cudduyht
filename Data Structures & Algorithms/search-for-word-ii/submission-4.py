class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

    def addWord(self, word):
        currNode = self
        for i in range(len(word)):
            if word[i] not in currNode.children:
                currNode.children[word[i]] = TrieNode()
            currNode = currNode.children[word[i]]
        currNode.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create a trie on the words
        trie = TrieNode()
        for w in words:
            trie.addWord(w)

        # iterate over each starting cell and add the words found from it on the res 
        res = set()
        visited = set()

        def dfs(i, j, node, currWord):
            outOfBounds = i < 0 or j < 0 or i >= len(board) or j >= len(board[i])
            if outOfBounds or (i, j) in visited or board[i][j] not in node.children:
                return

            visited.add((i, j))
            node = node.children[board[i][j]]
            currWord += board[i][j]
            if node.isWord:
                res.add(currWord)

            dfs(i - 1, j, node, currWord)
            dfs(i + 1, j, node, currWord)
            dfs(i, j - 1, node, currWord)
            dfs(i, j + 1, node, currWord)
            visited.remove((i, j))


        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, trie, "")
        
        return list(res)
