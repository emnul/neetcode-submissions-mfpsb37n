class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1,0], [-1, 0], [0, -1], [0, 1]]
        res = []

        def bfs(ir,ic):
            visit = set()
            visit.add((ir,ic))
            q = deque([[ir,ic]])
            canFlow = [False, False] # pac, atl

            while q:
                r, c = q.popleft()

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
                    
                    if (nr < 0 or nc < 0):
                        canFlow[0] = True
                    if (nr >= ROWS or nc >= COLS):
                        canFlow[1] = True
            
            if canFlow[0] and canFlow[1]:
                res.append([ir,ic])

        for r in range(ROWS):
            for c in range(COLS):
                bfs(r,c)

        return res