class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        ans=[]
        def backtrack(v,l):
            if v==n-1:
                print(*l)
                ans.append(l)
                return
            for nd in graph[v]:
                backtrack(nd,l+[nd])
        backtrack(0,[0])
        return ans