class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = COLS = len(grid)
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        minTime = {}
        minHeap = [(grid[0][0],0,0)]
        visit = set()

        while minHeap:
            curTime, r, c = heapq.heappop(minHeap)
            visit.add((r,c))

            if r == ROWS - 1 and c == COLS - 1:
                return curTime

            if (r,c) not in minTime:
                minTime[(r,c)] = curTime
            else:
                continue
            

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    (nr, nc) not in visit and
                    0 <= nr < ROWS and
                    0 <= nc < COLS
                ):
                    heapq.heappush(minHeap, (max(curTime, grid[nr][nc]), nr, nc))
                    visit.add((nr,nc))
    





