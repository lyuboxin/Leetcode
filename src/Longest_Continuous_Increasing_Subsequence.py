class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=1
        temp=1
        if len(nums)==0:
            return 0
        else:
            for i in range(len(nums)-1):
                if nums[i]<nums[i+1]:
                    count=count+1
                    print count
                else:
                    if count>temp:
                        temp=count
                    count=1
            if count >temp:
                temp=count
            return temp

