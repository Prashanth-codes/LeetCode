class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[[-1]*n for _ in range(n)]
        def lps(i,j):
            if i>j:
                return 0
            if i==j:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==s[j]:
                dp[i][j]=2+lps(i+1,j-1)
                return dp[i][j]
            dp[i][j]=max(lps(i,j-1),lps(i+1,j))
            return dp[i][j]
        return lps(0,n-1)
