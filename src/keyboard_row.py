class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l1=['q','w','e','r','t','y','u','i','o','p']
        l2=['a','s','d','f','g','h','j','k','l']
        l3=['z','x','c','v','b','n','m']
        L=[]
        flag1,flag2,flag3=0,0,0
        for i in range(len(words)):
            for x in words[i]:
                if x in l1:
                    flag1=1
                if x in l2:
                    flag2=1
                if x in l3:
                    flag3=1         
            if flag1+flag2+flag3==1:
                L.append(words[i])
            flag1,flag2,flag3=0,0,0
        return L

