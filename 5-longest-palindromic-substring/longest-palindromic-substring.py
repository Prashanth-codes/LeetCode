class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans=""
        def center(i,j):
            while i>=0 and j<n and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]
        for i in range(n):
            s1=center(i,i)
            s2=center(i,i+1)
            st=s1 if len(s1)>len(s2) else s2
            if len(st)>len(ans):
                ans=st
        return ans