class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        dp=[[-1]*n for _ in range(m)]
        def mindist(i,j):
            if i==m:
                return n-j
            if j==n:
                return m-i
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i]==word2[j]:
                return mindist(i+1,j+1)
            ins=1+mindist(i,j+1)
            rem=1+mindist(i+1,j)
            rep=1+mindist(i+1,j+1)
            dp[i][j]=min(ins,rem,rep)
            return dp[i][j]
        return mindist(0,0)