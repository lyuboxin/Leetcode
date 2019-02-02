class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        L=[]
        s1=collections.Counter(s)
        for x in s1.values():
            if x%2!=0:
                L.append(x)
        if len(L)!=0:
            return (len(s)-len(L)+1)
        return len(s)

