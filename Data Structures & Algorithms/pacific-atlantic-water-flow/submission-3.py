class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1,0], [-1, 0], [0, -1], [0, 1]]
        res = []

        # use these sets to quickly membership test cells
        pac, atl = set(), set()

        for r in range(ROWS):
            pac.add((r, 0))
            atl.add((r, COLS - 1))
        
        for c in range(COLS):
            pac.add((0, c))
            atl.add((ROWS - 1, c))

        def bfs(r,c):
            visit = set()
            visit.add((r,c))
            q = deque([[r,c]])
            canFlow = [False, False] # pac, atl

            while q:
                r, c = q.popleft()

                if (r,c) in pac:
                    canFlow[0] = True
                if (r,c) in atl:
                    canFlow[1] = True
                
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
            
            return canFlow[0] and canFlow[1]

        for r in range(ROWS):
            for c in range(COLS):
                canFlow = bfs(r,c)
                if canFlow:
                    res.append([r,c])
        return res