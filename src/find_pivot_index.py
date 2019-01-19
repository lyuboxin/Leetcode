class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)<2:
            return -1
        else:
            totalsum=sum(nums)
            left_sum=0
            for i in range(len(nums)):
                if left_sum==totalsum-left_sum-nums[i]:
                    return i
                left_sum=left_sum+nums[i]
            return -1

