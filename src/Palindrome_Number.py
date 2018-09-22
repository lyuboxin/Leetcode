src
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=str(x)
        for index in range(len(y)):
            if y[index] != y[len(y)-index-1]:
                return False
        return True
