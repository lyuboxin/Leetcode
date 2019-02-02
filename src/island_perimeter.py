class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            grid[i].append(0)
            grid[i].insert(0,0)
        L=[0 for i in range(len(grid[0]))]
        grid.append(L)
        grid.insert(0,L)
        count=0
        number=0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                if grid[i][j]==1:
                    number=number+1
                    if grid[i-1][j]==1:
                        count=count+1
                    if grid[i][j-1]==1:
                        count=count+1
                    if grid[i][j+1]==1:
                        count=count+1
                    if grid[i+1][j]==1:
                        count=count+1
        return number*4-count

