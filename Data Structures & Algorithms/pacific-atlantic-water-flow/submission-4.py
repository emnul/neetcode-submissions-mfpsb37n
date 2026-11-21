class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1,0], [-1, 0], [0, -1], [0, 1]]
        res = []

        def bfs(r,c):
            visit = set()
            visit.add((r,c))
            q = deque([[r,c]])
            canFlow = [False, False] # pac, atl

            while q:
                r, c = q.popleft()

                if r < 0 or c < 0:
                    canFlow[0] = True
                    continue
                if r >= ROWS or c >= COLS:
                    canFlow[1] = True
                    continue
                
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    # bounds check
                    # visit check
                    # rule check
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visit and
                        heights[nr][nc] <= heights[r][c]
                    ):
                        q.append([nr, nc])
                        visit.add((nr, nc))
                    
                    if (
                        nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS
                    ):
                        q.append([nr, nc])
                        visit.add((nr, nc))
            
            return canFlow[0] and canFlow[1]

        for r in range(ROWS):
            for c in range(COLS):
                canFlow = bfs(r,c)
                if canFlow:
                    res.append([r,c])
        return res