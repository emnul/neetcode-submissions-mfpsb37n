class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = collections.deque([(0, 0, 1)])  # r, c, length
        visit = set((0, 0))
        neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        while q:
            r, c, length = q.popleft()
            if min(r, c) < 0 or max(r, c) >= N or grid[r][c] == 1:
                continue
            if r == N - 1 and c == N - 1:
                return length

            for dr, dc in neighbors:
                newRow, newCol = r + dr, c + dc

                if (newRow, newCol) not in visit:
                    q.append((newRow, newCol, length + 1))
                    visit.add((newRow, newCol))
        return -1
