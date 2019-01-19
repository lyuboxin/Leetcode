class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        count=0
        largecount=[]
        index=[]
        i=0
        a=None
        for x in S:
            if x!=a:
                a=x
                if count>2:
                    largecount.append(count)
                    index.append(i-count)
                count=1
                    
            else:
                count=count+1
            i=i+1
            if i ==len(S):
                if count>2:
                    largecount.append(count)
                    index.append(i-count)                
        # L=[[0]*2]*len(index)
        L=[([0]*2) for i in range(len(index))]
        for i in range(len(index)):
            L[i][0]=index[i]
            L[i][1]=index[i]+largecount[i]-1
        if len(largecount)!=0:
            return L
        else:
            return []

