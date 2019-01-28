class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        string = []
        string = str.split(" ")
        dic={}
        if len(string)!=len(pattern):
            return False
        else:
            for i in range(len(pattern)):
                if pattern[i] not in dic:
                    if string[i] not in dic.values():
                        dic[pattern[i]]=string[i]
                    else:
                        return False
                else:
                    if dic[pattern[i]]!=string[i]:
                        return False
            return True

