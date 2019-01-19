class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return -1
        elif len(nums)==1:
            return 0
        else:
            nums1=sorted(nums)
            print nums1
            print nums
            if nums1[-1]>=2*nums1[-2]:
                return nums.index(nums1[-1])
            else:
                return -1

