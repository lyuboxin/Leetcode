class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits)==0:
            return False
        elif len(bits)==1:
            return True
        else:
            while True:
                if bits[0]==0:
                    bits.pop(0)
                else:
                    bits.pop(0)
                    bits.pop(0)
                if len(bits)==1:
                    return True
                if len(bits)==0:
                    return False

