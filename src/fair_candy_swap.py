class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        total_a=sum(A)
        total_b=sum(B)
        exchange=(total_b-total_a)/2
        for i in A:
            element_b=i + exchange
            if element_b in B:
                return [i, element_b]

