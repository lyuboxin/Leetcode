class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in xrange(len(A)):
            A[i].reverse()
            for j in xrange(len(A[0])):
                if A[i][j]==1:
                    A[i][j]=0
                else:
                    A[i][j]=1
        return A

