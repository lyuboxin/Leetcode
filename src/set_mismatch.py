class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L=[]
        p=[]
        num=collections.Counter(nums)
        for i,x in num.items():
            if x==2:
                L.append(i)
        for i in range(1,len(nums)+1):
            p.append(i)
        for y in p:
            if y not in nums:
                L.append(y)
        return L

