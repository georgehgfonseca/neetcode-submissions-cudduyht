class WordDictionary:

    def __init__(self):
        self.children = dict()
        self.isWord = False
        

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = WordDictionary()
            curr = curr.children[char]
        curr.isWord = True
        

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i >= len(word):
                if node.isWord:
                    return True
                return False
            if not node.children:
                return False

            if word[i] == ".":
                foundAny = False
                for child in node.children:
                    found = dfs(node.children[child], i + 1)
                    if found:
                        foundAny = True
                return foundAny
            elif word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)
            else:
                return False
            
        return dfs(self, 0)

    def searchWithoutDot(self, word: str) -> bool:
        curr = self
        options = [curr]
        for i in range(len(word)):
            if word[i] == ".":
                options = curr.children
            if word[i] in curr.children:
                curr = curr.children[word[i]]
            else:
                return False

        return curr.isWord
