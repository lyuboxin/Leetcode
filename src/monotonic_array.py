class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)<2:
            return True
        else:
            for i in range(1,len(A)):
                if A[i-1]<A[i]:
                    for i in range(1,len(A)):
                        if A[i-1]>A[i]:
                            return False
                    return True
                elif A[i-1]>A[i]:
                    for i in range(1,len(A)):
                        if A[i-1]<A[i]:
                            return False
                    return True
                else:
                    continue
            return True

