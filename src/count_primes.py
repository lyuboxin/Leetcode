class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [True for i in range(n)]
        p = 2
        if n<p:
            return 0
        else:
            while(p*p<=n):
                if nums[p] == True:
                    for i in range(p*p, n, p):
                        nums[i] = False
                p = p+1
            counter = 0
            for i in range(2,len(nums)):
                if nums[i]==True:
                    counter+=1
            return counter

