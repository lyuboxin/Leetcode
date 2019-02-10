class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count=0
        L=collections.Counter(S)
        for i in J:
            if i in L.keys():
                count=count+L[i]
        return count

