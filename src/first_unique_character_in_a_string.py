class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=list(s)
        groups={}
        value=0
        L=[]
        for x in s:
            if x not in groups:
                groups[x]=True
            else:
                groups[x]=False
        for i in groups.keys():
            if groups[i]==True:
                L.append(i)
        if len(L)==0:
            return -1
        for j in s:
            if j in L:
                return s.index(j)

