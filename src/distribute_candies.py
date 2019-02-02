class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        count=0
        candy=collections.Counter(candies)
        count=count+len(candy.values())
        if count>len(candies)/2:
            count=len(candies)/2
        return count
