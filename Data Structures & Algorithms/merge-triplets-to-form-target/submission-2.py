class Solution:
    def mergeTriplets3(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3
        
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1 and triplets[0] == target:
            return True

        # compute triplets that form the target[pos]
        candTriplets = set([i for i in range(len(triplets))])
        posMatches = {pos: 0 for pos in range(len(target))}
        for pos in range(len(target)):
            toRemove = set()
            for idx in candTriplets:
                if triplets[idx][pos] > target[pos]:
                    toRemove.add(idx)
                
            for idx in toRemove:
                candTriplets.remove(idx)
        
        for pos in range(len(target)):
            foundPos = False
            for idx in candTriplets:
                if triplets[idx][pos] == target[pos]:
                    foundPos = True
            if not foundPos:
                return False
        return True



    def mergeTriplets2(self, triplets: List[List[int]], target: List[int]) -> bool:
        # brute force
        for i in range(len(triplets)):
            for j in range(i + 1, len(triplets)):
                if max(triplets[i][0], triplets[j][0]) == target[0] and \
                   max(triplets[i][1], triplets[j][1]) == target[1] and \
                   max(triplets[i][2], triplets[j][2]) == target[2]:
                   return True
        return False