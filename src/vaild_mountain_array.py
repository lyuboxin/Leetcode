class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        if len(A) <3:
            return False
        elif len(A)==3:
            if A[1]>A[0] and A[1]>A[2]:
                return True
            return False
        else:
            x,y=0,len(A)-1
            x1=1
            y1=len(A)-2
            if A[y1]<A[y] or A[x1] < A[x]:
                return False            
            for i in range(len(A)):                
                if A[x1] > A[x]:
                    x=x1
                    x1=x1+1
                if y-x==1 :
                    return True
                if A[y1] > A[y]:
                    y=y1
                    y1=y1-1
                if y-x==1:
                    return True
            return False

