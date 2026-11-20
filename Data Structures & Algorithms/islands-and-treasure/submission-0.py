class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append([r,c])

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visit and 
                        grid[nr][nc] == 2147483647
                    ):
                        q.append([nr, nc])
                        visit.add((nr, nc))
            
            dist += 1
