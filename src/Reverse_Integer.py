src
class Solution(object):
    def reverse(self, x):
        """
        :type dx: int
        :rtype: int
        """
        if x> math.pow(2, 31)-1 or x < -math.pow(2, 31):
            return 0
        elif x > 0 and x< math.pow(2, 31):
            y =str(x)
            y0=y[::-1]
            y1=int(y0)
            if y1 < math.pow(2,31)-1 or y1==math.pow(2,31)-1:
                return y1
            else:
                return 0
        elif x<0 and x > -math.pow(2, 31)-1:
            x=abs(x)
            y = str(x)
            y0 = y[::-1]
            y1 = int(y0)
            if y1 < math.pow(2,31) or y1==math.pow(2,31):
                return -y1
            else:
                return 0
        elif x==0:
            return 0
