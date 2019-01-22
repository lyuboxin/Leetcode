class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        L=[]
        for i in range(len(A)):
            L.append(A[i]*A[i])
        L.sort()
        return L

