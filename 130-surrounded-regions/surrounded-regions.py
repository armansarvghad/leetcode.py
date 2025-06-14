def dfs(row,col,vis,board,d):
    vis[row][col]=1
    for dx,dy in d:
        nrow=dx+row
        ncol=dy+col
        if 0<=nrow<len(board) and 0<=ncol<len(board[0]) and board[nrow][ncol]=='O' and vis[nrow][ncol]==0:
            dfs(nrow,ncol,vis,board,d)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        d=[(1,0),(0,1),(-1,0),(0,-1)]
        vis=[[0]*n for _ in range(m)]
        for i in range(n):
            if not vis[0][i] and board[0][i]=='O':
                dfs(0,i,vis,board,d)
            if not vis[m-1][i] and board[m-1][i]=='O':
                dfs(m-1,i,vis,board,d)
        for i in range(m):
            if not vis[i][0] and board[i][0]=='O':
                dfs(i,0,vis,board,d)
            if not vis[i][n-1] and board[i][n-1]=='O':
                dfs(i,n-1,vis,board,d)
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and vis[i][j]==0:
                    board[i][j]="X"
            

        