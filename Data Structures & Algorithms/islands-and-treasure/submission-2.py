class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        q = deque()
        visit = set()
        dist = 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        def addRow(r,c):
            if (
                0 <= r < ROWS and
                0 <= c < COLS and
                (r,c) not in visit and
                grid[r][c] == 2147483647
            ):
                q.append([r,c])
                visit.add((r,c))
                
        dist = 0
        while q:
            # start BFS from each elem currently in q simultaneously
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    addRow(r + dr, c + dc)
                
            dist += 1
        
                
            
                

