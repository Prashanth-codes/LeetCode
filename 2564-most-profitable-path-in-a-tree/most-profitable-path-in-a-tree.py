class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        mp=defaultdict(list)
        for u,v in edges:
            mp[u].append(v)
            mp[v].append(u)
        b={}
        def dfs(src,p,t):
            if src==0:
                b[src]=t
                return True
            for nbr in mp[src]:
                if nbr==p:
                    continue
                if dfs(nbr,src,t+1):
                    b[src]=t
                    return True
            return False
        dfs(bob,-1,0)
        ans=float('-inf')
        q=deque([(0,-1,0,amount[0])])
        while q:
            n,prnt,t,p=q.popleft()
            for nbr in mp[n]:
                if nbr==prnt:
                    continue
                g=amount[nbr]
                if nbr in b:
                    if t+1>b[nbr]:
                        g=0
                    elif t+1==b[nbr]:
                        g=amount[nbr]//2
                q.append((nbr,n,t+1,p+g))
                if len(mp[nbr])==1:
                    ans=max(ans,p+g)
        return ans