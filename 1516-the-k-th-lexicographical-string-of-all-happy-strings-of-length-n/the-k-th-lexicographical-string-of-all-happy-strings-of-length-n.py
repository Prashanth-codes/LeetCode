class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans=[]
        arr=["a","b","c"]
        def backtrack(l):
            if len(l)==n:
                s="".join(l)
                ans.append(s)
                return
            for v in arr:
                if l:
                    if l[-1]!=v:
                        l.append(v)
                        backtrack(l)
                        l.pop()
                else:
                    l.append(v)
                    backtrack(l)
                    l.pop()
        backtrack([])
        print(*ans)
        if len(ans)<k:
            return ""
        return ans[k-1]