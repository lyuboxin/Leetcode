class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        output=[]
        for i in range(len(A)):
            if A[i]%2==0:
                output.insert(0,A[i])
            else:
                output.append(A[i])
        return output

