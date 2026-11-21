class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]
        q = deque()
        INF = 2147483647

        # find all treasure chests and add to queue
        # in order to perform BFS from multiple points
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
        
        dist = 0
        visit = set()
        while q:
            # do one BFS loop from each treasure chest
            # location
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                visit.add((r,c))

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    # bounds check
                    # land check
                    # visit check
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == INF and
                        (nr, nc) not in visit
                    ):
                        q.append([nr, nc])
                        visit.add((nr,nc))
            
            dist += 1
        


