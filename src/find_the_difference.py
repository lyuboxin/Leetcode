class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s=list(s)
        t=list(t)
        for i in t:
            if i not in s:
                return i
            else:
                s.remove(i)

