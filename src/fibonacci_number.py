def abc(N):
    if N==0:
        return 0
    elif N==1:
        return 1
    else:
        return abc(N-1)+abc(N-2)
    
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        return abc(N)

