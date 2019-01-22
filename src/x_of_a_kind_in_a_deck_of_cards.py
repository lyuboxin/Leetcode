class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        count=collections.Counter(deck)
        N=len(deck)
        for x in xrange(2,N+1):
            if N%x==0:
                if all(v%x==0 for v in count.values()):
                    return True
        return False

