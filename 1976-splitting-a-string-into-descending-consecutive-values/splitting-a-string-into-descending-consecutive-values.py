class Solution:
    def splitString(self, s: str) -> bool:
        n=len(s)
        ans=[]
        def backtrack(idx,l):
            if idx==n:
                return True
            for i in range(idx,n):
                num=int(s[idx:i+1])
                if l is None or num==l-1:
                    if backtrack(i+1,num):
                        return True
        for i in range(n-1):
            num=int(s[:i+1])
            if backtrack(i+1,num):
                return True
        return False