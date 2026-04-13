class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # limit          = 3
        # people         = [1, 2, 2, 3, 3]
        # l, r           =     * *
        # res            = 3

        people.sort()
        # try to match the heaviest with lightest person
        res = 0
        l, r = 0, len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                # perfect match: a boat for people in l and r
                res += 1
                l += 1
                r -= 1
            else:
                # one boat to person in r
                res += 1
                r -= 1
        return res


