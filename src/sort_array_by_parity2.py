class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd=[]
        even=[]
        L=[]
        evencount=0
        oddcount=0
        for i in range(len(A)):
            if A[i]%2==0:
                even.append(A[i])
            else:
                odd.append(A[i])
        for i in range(len(A)):
            if i%2==0:
                L.append(even[evencount])
                evencount=evencount+1
            else:
                L.append(odd[oddcount])
                oddcount=oddcount+1
        return L
