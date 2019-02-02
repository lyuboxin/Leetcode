class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=1
        num=collections.Counter(nums)
        num1=sorted(num.keys())
        L=[]
        for i in range(1,len(num1)):
            if num1[i]-num1[i-1]==1:
                L.append((num[num1[i]]+num[num1[i-1]]))
        if len(L)>=1:
            return max(L)
        else:
            return 0

