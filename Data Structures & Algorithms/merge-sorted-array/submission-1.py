class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1        = [1, 2, 3, 0, 5, 6]
        # idx1         =        *
        # nums2        = [2, 5, 6]
        # idx2         =  *
        # numPlace     = 2
        idx1 = m - 1
        idx2 = len(nums2) - 1
        numPlaceholders = len(nums1) - m
        while idx1 >= 0 and idx2 >= 0:
            if nums2[idx2] > nums1[idx1]:
                nums1[idx1 + numPlaceholders] = nums2[idx2]
                idx2 -= 1
                numPlaceholders -= 1
            else:
                nums1[idx1 + numPlaceholders] = nums1[idx1]
                nums1[idx1] = 0
                idx1 -= 1
        
        while idx2 >= 0:
            nums1[idx2] = nums2[idx2]
            idx2 -= 1

            # add all elements of nums2 in the beginning of nums1


                # shift postion

        