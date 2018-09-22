src
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)):
            for index1 in range(index+1, len(nums)):
                if nums[index] + nums[index1] == target:
                    list = [index, index1]
                    return list
