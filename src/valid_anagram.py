def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        value=collections.Counter(s)
        value1=collections.Counter(t)
        if len(value)!=len(value1):
            return False
        else:
            for i in value.keys():
                if i not in value1.keys():
                    return False
                else:
                    if value[i]!=value1[i]:
                        return False
            return True

