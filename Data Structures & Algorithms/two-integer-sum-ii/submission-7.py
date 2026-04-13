class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # nums   = [1, 5, 9, 10]
        # target = 14
        # l      = 1
        # r      = 3
        # we can use two pointers starting at l = 0, r = len(n) - 1
        l = 0
        r = len(numbers) - 1
        while l < r:
            # while n[l] + n[r] > target, more r to left
            while numbers[l] + numbers[r] > target:
                r -= 1

            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            # at the end of each iteration, move l
            l += 1

        # brute-force first - run twice throught nums and return the pair
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]

        