class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        i=0
        distance=0
        dis=0
        for j in range(len(seats)):
            if seats[j]==1:
                if distance< j-i:
                    distance=j-i
                if seats[0]==0 and i==0: 
                    dis =j-i
                    print dis
                i = j
            else:
                if j==len(seats)-1:
                    if (distance+1)<=2*(j-i) and dis < (j-i):
                        return j-i
        if distance+1<= 2*dis:
            return dis
        else:
            # print distance%2
            if distance%2==0:
                return (distance+1)/2
            else:
                return (distance-1)/2

