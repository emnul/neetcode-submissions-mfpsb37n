class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1,0], [-1, 0], [0, -1], [0, 1]]
        pac, atl = set(), set()
        pacific, atlantic = [], []
        res = []

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))
        
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        def bfs(sources, ocean):
            q = deque(sources)

            while q:
                r, c = q.popleft()
                ocean.add((r,c))

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    # bounds check
                    # visit check
                    # rule check
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr,nc) not in ocean and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        q.append([nr, nc])

        bfs(pacific, pac)
        bfs(atlantic, atl)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res