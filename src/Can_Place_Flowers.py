class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                n=n-1
        else:
            for i in range(len(flowerbed)):
                if i==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                    n=n-1
                    flowerbed[i]=1
                elif i==len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i-1]==0:
                    n=n-1
                    flowerbed[i]=1
                elif i!=0 and i!=len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i-1]==0 and                                   flowerbed[i+1]==0:
                        n=n-1
                        flowerbed[i]=1
        if n<=0:
            return True
        return False
