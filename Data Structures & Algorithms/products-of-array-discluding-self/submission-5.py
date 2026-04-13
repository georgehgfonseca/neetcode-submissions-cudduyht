class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # compute the product of elements at the left of i and of elements at the right of i
        # if out of bound place 1 instead
        # for each element at i-th position, multiply left[i] * right[i]
        # nums  = [1, 2, 4, 6]
        # left  = [1, 1, 2, 8]
        # left  = [48, 24, 6, 1]
        # ans   = []
        left = [1]
        currProduct = 1
        for i in range(1, len(nums)):
            currProduct *= nums[i - 1]
            left.append(currProduct)

        nums.reverse()
        right = [1]
        currProduct = 1
        for i in range(1, len(nums)):
            currProduct *= nums[i - 1]
            right.insert(0, currProduct)
        nums.reverse()

        return [left[i] * right[i] for i in range(len(nums))]

        