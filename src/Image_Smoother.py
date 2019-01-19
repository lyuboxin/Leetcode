class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        N = [[0]*len(M[0]) for i in range(len(M))]
        if len(M)==1 or len(M[0])==1:
            if len(M)==1 and len(M[0])!=1:
                for j in range(len(M[0])):
                    if j==0:
                        N[0][j]=(M[0][j]+M[0][j+1])/2
                    elif j==len(M[0])-1:
                        N[0][j]=(M[0][j-1]+M[0][j])/2
                    else:
                        N[0][j]=(M[0][j-1]+M[0][j]+M[0][j+1])/3
            elif len(M[0])==1 and len(M)!=1:
                for i in range(len(M)):
                    if i==0:
                        N[i][0]=(M[i][0]+M[i+1][0])/2
                    elif i==len(M)-1:
                        N[i][0]=(M[i-1][0]+M[i][0])/2
                    else:
                        N[i][0]=(M[i-1][0]+M[i][0]+M[i+1][0])/3
            else:
                N[0][0]=M[0][0]
        else:
            for i in range(len(M)):
                for j in range(len(M[0])):
                    if i==0:
                        if j==0:
                            N[i][j]=(M[i][j]+M[i][j+1]+M[i+1][j]+M[i+1][j+1])/4
                        elif j==len(M[0])-1:
                            N[i][j]=(M[i][j-1]+M[i][j]+M[i+1][j-1]+M[i+1][j])/4
                        else:
                            N[i][j]=(M[i][j-1]+M[i][j]+M[i][j+1]+M[i+1][j-1]+M[i+1][j]+M[i+1][j+1])/6
                    elif i==len(M)-1:
                        if j==0:
                            N[i][j]=(M[i-1][j]+M[i-1][j+1]+M[i][j]+M[i][j+1])/4
                        elif j==len(M[0])-1:
                            N[i][j]=(M[i-1][j-1]+M[i-1][j]+M[i][j-1]+M[i][j])/4
                        else:
                            N[i][j]=(M[i-1][j-1]+M[i-1][j]+M[i-1][j+1]+M[i][j-1]+M[i][j]+M[i][j+1])/6
                            
                    else:
                        if j==0:
                            N[i][j]=(M[i-1][j]+M[i-1][j+1]+M[i][j]+M[i][j+1]+M[i+1][j]+M[i+1][j+1])/6
                        elif j==len(M[0])-1:
                            N[i][j]=(M[i-1][j-1]+M[i-1][j]+M[i][j-1]+M[i][j]+M[i+1][j-1]+M[i+1][j])/6
                        else:
                            N[i][j]=(M[i][j]+M[i-1][j-1]+M[i-1][j]+M[i-1][j+1]+M[i][j-1]+M[i][j+1]+M[i+1][j-1]+M[i+1][j]+M[i+1][j+1])/9
        return N 
