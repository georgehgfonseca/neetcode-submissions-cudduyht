class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def countDiffChars(w1: str, w2: str):
            count = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    count += 1
            return count

        # create a graph that holds connections between neighbor words (words than can be generated from it by switching one char)
        wordList.append(beginWord)
        graph = {word: set() for word in wordList}
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if countDiffChars(wordList[i], wordList[j]) == 1:
                    graph[wordList[i]].add(wordList[j])
                    graph[wordList[j]].add(wordList[i])
        
        # find a path from beginWord to endWord in such a graph (bfs/dfs)
        # actually, I DO need BFS, but I DO NOT need the actual path
        level = {word: 0 for word in wordList} # 0 == not visited
        queue = deque()
        queue.append(beginWord)
        level[beginWord] = 1
        while queue:
            beginWord = queue.popleft()
            for neighbor in graph[beginWord]:
                if level[neighbor] == 0:
                    queue.append(neighbor)
                    level[neighbor] = level[beginWord] + 1
                    if neighbor == endWord:
                        return level[neighbor]
        return 0






        