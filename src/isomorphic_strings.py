class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] not in dic.values():
                    dic[s[i]]=t[i]
                else:
                    return False
            else:
                if dic[s[i]]!=t[i]:
                    return False
        return True

