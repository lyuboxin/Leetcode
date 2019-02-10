class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        dic="abcdefghijklmnopqrstuvwxyz";
        L=[]
        dic=list(dic)
        licensePlate=licensePlate.lower()
        for x in licensePlate:
            if x in dic:
                L.append(x)
        words=sorted(words,key=lambda i:len(i))        
        for a,i in enumerate(words):
            flag=0
            for j in L:
                if j in i:
                    i=list(i)
                    i.remove(j)
                else:
                    flag=1
                    break
            if flag==0:
                return words[a]

