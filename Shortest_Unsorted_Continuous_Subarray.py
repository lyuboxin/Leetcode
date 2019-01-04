class Solution(object):
    def findUnsortedSubarray(self, nums):
        value1=0
        value2=0
        nums1=sorted(nums)
        for i in range(len(nums)):
            if nums1[i]!=nums[i]:
                value1=i
                break
        for i in range(len(nums)):
            j=len(nums)-i-1;
            if nums1[j]!=nums[j]:
                value2=j
                break
        if value1==value2:
            return 0
        return value2-value1+1
