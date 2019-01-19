class Solution(object):
    def maximumproductofthreenumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1=sorted(nums)
        value=nums1[len(nums1)-1]*nums1[len(nums1)-2]*nums1[len(nums1)-3]
        value1=nums1[0]*nums1[1]*nums1[len(nums1)-1]
        if value>value1:
            return value
        return value1

