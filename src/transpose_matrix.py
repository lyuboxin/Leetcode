class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        r=len(A)
        c=len(A[0])
        B = [([0]*r) for i in range(c) ]
        for i in range(r):
            for j in range(c):
                B[j][i]=A[i][j]
        return B

