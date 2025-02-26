class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n=len(s)
        a=[]
        ans=[]
        for i,ch in enumerate(s):
            if ch==c:
                a.append(i)
        print(*a)
        for i in range(n):
            mn=float('inf')
            for idx in a:
                mn=min(mn,abs(i-idx))
            ans.append(mn)
        return ans