graph = ["11110",
		 "11010",
		 "11000",
		 "00000"]

graph2 = ["11000",
		  "11000",
		  "00100",
		  "00011"]

graph3 = ["111",
		  "010",
		  "111"]

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == "1":
                    islands += 1
                    self.sink(grid, i, j)
        return islands
    
    def sink(self, G, i, j):
        if (i >= 0) and (j >= 0) and (i < len(G)) and (j < len(G[i])) and (G[i][j] != "0"):
            G[i] = G[i][:j] + "0" + G[i][j+1:]
            self.sink(G, i+1, j)
            self.sink(G, i-1, j)
            self.sink(G, i, j+1)
            self.sink(G, i, j-1)

S = Solution()
print S.numIslands(graph)
print S.numIslands(graph2)
print S.numIslands(graph3)