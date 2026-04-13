class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1 and triplets[0] == target:
            return True

        # compute pairs that form the target[pos]
        candTriplets = set([i for i in range(len(triplets))])
        tripletsWithTargetPos = set()
        for pos in range(len(target)):
            if pos != 0 and len(tripletsWithTargetPos) == 0:
                return False
            tripletsWithTargetPos = set()
            toRemove = set()
            for idx in candTriplets:
                if triplets[idx][pos] > target[pos]:
                    toRemove.add(idx)
                elif triplets[idx][pos] == target[pos]:
                    tripletsWithTargetPos.add(idx)
            for idx in toRemove:
                candTriplets.remove(idx)

            #print(candTriplets, tripletsWithTargetPos)

        if len(candTriplets) >= 2:
            return True
        return False


    def mergeTriplets2(self, triplets: List[List[int]], target: List[int]) -> bool:
        # brute force
        for i in range(len(triplets)):
            for j in range(i + 1, len(triplets)):
                if max(triplets[i][0], triplets[j][0]) == target[0] and \
                   max(triplets[i][1], triplets[j][1]) == target[1] and \
                   max(triplets[i][2], triplets[j][2]) == target[2]:
                   return True
        return False