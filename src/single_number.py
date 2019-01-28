class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        groups={}
        for x in nums:
            if x not in groups:
                groups[x]=1
            else:
                groups[x]=2
        for i in groups.keys():
            if groups.get(i)==1:
                return I

