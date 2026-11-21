class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        visit = set()
        fresh = 0

        # use multisource BFS approach
        # initialze queue with rotten fruit pos
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
        
        time = 0
        while q:
            if fresh == 0:
                return time
            for i in range(len(q)):
                r,c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visit and
                        grid[nr][nc] == 1
                    ):
                        q.append([nr, nc])
                        visit.add((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
                
            time += 1
        
        if fresh == 0:
            return time
        return -1

        