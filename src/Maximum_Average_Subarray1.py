class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        value=-100000000000
        temp=0
        if len(nums)<=k:
            for i in range(len(nums)):
                temp=temp+nums[i]
            return float(temp)/float(k)
        else:
            for i in range(len(nums)-k+1):
                if i==0:
                    for j in range(k):
                        temp=temp+nums[i+j]
                else:
                    temp=temp-nums[i-1]+nums[i+k-1]
                if value <temp:
                    value=temp
            return float(value)/float(k) 
