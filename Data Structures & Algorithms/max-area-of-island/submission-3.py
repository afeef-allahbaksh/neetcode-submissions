
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0
        directions = [[1,0], [-1,0], [0, 1], [0,-1]]

        def bfs(r,c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            res = 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr 
                    >= rows or nc >= cols or grid[nr][nc] == 0):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = 0
                    res += 1     
            return res
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, bfs(r,c))
        
        return area
        # visit = set()
        # ROWS, COLS = len(grid), len(grid[0])
        # def dfs(r,c):
        #     if (r < 0 or c < 0 or c == COLS or r == ROWS or (r,c) in visit or grid[r][c] == 0):
        #         return 0
        #     visit.add((r,c))
        #     return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r,c - 1))

        
        # area = 0
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         area = max(area, dfs(r,c))
        # return area