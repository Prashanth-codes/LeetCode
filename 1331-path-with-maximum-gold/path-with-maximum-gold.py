class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        ans=0
        di=[-1,0,1,0]
        dj=[0,1,0,-1]
        def dfs(i,j):
            c=grid[i][j]
            grid[i][j]=0
            mx=0
            for k in range(4):
                ni,nj=i+di[k],j+dj[k]
                if 0<=ni<m and 0<=nj<n and grid[ni][nj]>0:
                    mx=max(mx,dfs(ni,nj))
            grid[i][j]=c
            return c+mx
        for i in range(m):
            for j in range(n):
                if grid[i][j]>0:
                    ans=max(ans,dfs(i,j))
        return ans