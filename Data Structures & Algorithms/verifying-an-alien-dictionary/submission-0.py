class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # create a hashmap of letter, position
        # iterate through the words and compare the i-th with the i + 1-th
        def compareWords(word1: str, word2: str, letterPosition):
            i = 0
            n = min(len(word1), len(word2))
            for i in range(n):
                if letterPosition[word1[i]] < letterPosition[word2[i]]:
                    return -1 # word1 is before word2
                if letterPosition[word1[i]] > letterPosition[word2[i]]:
                    return 1 # word1 is after word2
            if len(word1) < len(word2):
                return -1
            if len(word1) > len(word2):
                return 1
            return 0

        letterPosition = {order[i]: i for i in range(len(order))}
        for i in range(len(words) - 1):
            if compareWords(words[i], words[i + 1], letterPosition) == 1:
                return False
        return True