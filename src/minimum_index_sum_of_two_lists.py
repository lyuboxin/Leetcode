class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res=10000
        L=[]
        for i, x in enumerate(list1):
            if x in list2:
                if i+list2.index(x)<res:
                    res=i+list2.index(x)
                    L.append(x)
                elif i+list2.index(x)==res:
                    L.append(x)
        l1=[]
        for i in range(len(L)-1,-1,-1): 
            if list1.index(L[i-1])+list2.index(L[i-1])!=list1.index(L[i])+list2.index(L[i]):               
                break
            l1.append(L[i])
        return l1

