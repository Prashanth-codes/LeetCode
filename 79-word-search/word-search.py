class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        di=[-1,0,1,0]
        dj=[0,1,0,-1]
        ans=True
        def dfs(idx,i,j):
            if idx==len(word):
                return True
            if i<0 or i>=m or j<0 or j>=n or board[i][j]!=word[idx]:
                return False
            temp,board[i][j]=board[i][j],'#'
            for k in range(4):
                ni,nj=i+di[k],j+dj[k]
                if dfs(idx+1,ni,nj):
                    return True
            board[i][j]=temp
            return False
        for i in range(m):
            for j in range(n):
                if word[0]==board[i][j]:
                    if dfs(0,i,j):
                        return True
        return False