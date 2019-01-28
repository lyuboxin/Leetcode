def digit(M):
    count=0
    s=str(M)
    for x in s:
        count=count+int(x)*int(x)
    return count
        

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        L=[]
        tmp=n
        if n<0:
            return False
        else:
            while tmp!=1:
                tmp=digit(tmp)
                if tmp not in L:
                    L.append(tmp)
                else:
                    return False
            return True

