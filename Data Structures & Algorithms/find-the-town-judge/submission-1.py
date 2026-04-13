class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # trust        = [[1, 3], [4, 3], [2, 3]]
        # trusted      = {3: {1, 4, 2}}
        # 3
        # if len of exactly one person is n - 1
        trusted = dict()
        trusts = dict()
        for i in range(len(trust)):
            truster = int(trust[i][0])
            trustee = int(trust[i][1])
            if trustee not in trusted:
                trusted[trustee] = {truster}
            else:
                trusted[trustee].add(truster)
            if truster not in trusts:
                trusts[truster] = {trustee}
            else:
                trusts[truster].add(trustee)
        
        maxTrustedPeople = set()
        for person in trusted:
            if len(trusted[person]) == n - 1 and person not in trusts:
                maxTrustedPeople.add(person)

        if len(maxTrustedPeople) != 1:
            return -1
        
        return maxTrustedPeople.pop()