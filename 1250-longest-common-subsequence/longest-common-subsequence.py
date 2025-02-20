class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        dp=[[-1]*n for _ in range(m)]
        def lcs(i,j):
            if i==m or j==n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if text1[i]==text2[j]:
                dp[i][j]=1+lcs(i+1,j+1)
                return dp[i][j]
            op1=lcs(i+1,j)
            op2=lcs(i,j+1)
            dp[i][j]=max(op1,op2)
            return dp[i][j]
        return lcs(0,0)