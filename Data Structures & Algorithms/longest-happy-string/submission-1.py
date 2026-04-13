import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # use a max heap to choose next char
        # variable to forbid char for each char
        letterCount = []
        if a != 0:
            letterCount.append((-a, 'a'))
        if b != 0:
            letterCount.append((-b, 'b'))
        if c != 0:
            letterCount.append((-c, 'c'))
        heapq.heapify(letterCount)
        res = ""

        while letterCount:
            remaining, letter = heapq.heappop(letterCount)
            if len(res) >= 2 and res[-1] == letter and res[-2] == letter:
                # would imply on a sequence
                if not letterCount:
                    # no more letters to add other than the sequence
                    break
                altRemaining, altLetter = heapq.heappop(letterCount)
                res += altLetter
                altRemaining += 1
                if altRemaining != 0:
                    heapq.heappush(letterCount, (altRemaining, altLetter))
                
                # put unused letter back
                heapq.heappush(letterCount, (remaining, letter))
            else:
                res += letter
                remaining += 1
                if remaining != 0:
                    heapq.heappush(letterCount, (remaining, letter))
        return res
        