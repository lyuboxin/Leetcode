class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        groups={}
        nums1=set(nums1)
        nums2=set(nums2)
        nums1=list(nums1)
        nums2=list(nums2)
        L=[]
        for i in range(len(nums1)):
            groups[i]=nums1[i]
        for i in range(len(nums2)):
            if nums2[i] in groups.values():
                L.append(nums2[i])
        return L

