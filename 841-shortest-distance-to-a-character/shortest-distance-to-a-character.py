class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n=len(s)
        ans=[0]*n
        l=float('inf')
        for i in range(n):
            if s[i]==c:       
                l=i
            ans[i]=abs(i-l)
        print(*ans)
        l=float('inf')
        for i in range(n-1,-1,-1):
            if s[i]==c:
                l=i
            ans[i]=min(ans[i],abs(i-l))
        return ans