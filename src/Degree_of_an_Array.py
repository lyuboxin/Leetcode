class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=0
        distance=len(nums)
        L=list(set(nums))
        nums1=[]
        if len(nums)==1:
            return 1
        else:
            for i in range(len(L)):
                if temp<nums.count(L[i]):
                    temp=nums.count(L[i])
                    k=L[i]
            for i in range(len(L)):
                if temp==nums.count(L[i]):
                    nums1.append(L[i])
            for i in range(len(nums1)):
                m=nums.index(nums1[i])
                nums.reverse()
                n=len(nums)-nums.index(nums1[i])-1
                nums.reverse()
                if distance>n-m+1:
                    distance=n-m+1
            return distance

