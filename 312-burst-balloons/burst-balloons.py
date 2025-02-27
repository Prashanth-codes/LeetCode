class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        a=[]
        a.append(1)
        for i in nums:
            a.append(i)
        a.append(1)
        #same as matrix chain multiplication
        n=len(a)-1
        dp=[[0]*n for _ in range(n)]
        for s in range(2,n+1):
            for i in range(n-s+1):
                j=i+s-1
                mx=float('-inf')
                for k in range(i,j):
                    mx=max(mx,dp[i][k]+dp[k+1][j]+a[i]*a[j+1]*a[k+1])
                dp[i][j]=mx
        return dp[0][n-1]