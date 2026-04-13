class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # if started with x, goes all the way until there's no x left - can add others until find a new letter
        # s                 = [xyxxyzbzbibsl]
        # i                 =              *
        # letterCount       = {x: 0, y: 0, z: 0, b: 0, i: 0, s: 0, l: 0}
        # openLettersSubstr = {}
        # substr            = "l"
        # res               = [5, 6, 1, 1]
    

        letterCount = Counter(s)
        res = []
        i = 0
        while i < len(s):
            substr = s[i]
            openLettersSubstr = set()
            letterCount[s[i]] -= 1
            if letterCount[s[i]] > 0:
                openLettersSubstr.add(s[i])
            while openLettersSubstr and i + 1 < len(s):
                i += 1
                substr += s[i]
                letterCount[s[i]] -= 1
                if s[i] not in openLettersSubstr:
                    openLettersSubstr.add(s[i])
                if letterCount[s[i]] == 0:
                    openLettersSubstr.remove(s[i])
            res.append(len(substr))
            i += 1
        return res
        
        