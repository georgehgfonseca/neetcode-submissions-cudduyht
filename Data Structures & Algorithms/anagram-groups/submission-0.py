class Solution:
    def createLetterCount(self, str: str):
        letterCount = dict()
        for char in str:
            letterCount[char] = letterCount.get(char, 0) + 1
        return letterCount

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate over each str in strs
        processed = [False for _ in strs]
        anagrams = []
        for i in range(len(strs)):
            if processed[i]:
                continue

            strAnagrams = [strs[i]]
            processed[i] = True
            # compute a hashmap of char:count
            iLetterCount = self.createLetterCount(strs[i])

            # seek for anagrams of strs[i]
            for j in range(i + 1, len(strs)):
                if processed[j]:
                    continue

                jLetterCount = self.createLetterCount(strs[j])
                if iLetterCount == jLetterCount:
                    # mark a str as procesed to avoid duplicated work whenever it is added to any anagram
                    strAnagrams.append(strs[j])
                    processed[j] = True
            anagrams.append(strAnagrams)
        return anagrams