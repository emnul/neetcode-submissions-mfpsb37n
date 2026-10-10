class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        def dfs(r, c, visit):
            nonlocal orig
            ROWS, COLS = len(image), len(image[0])
            # bounds checks
            if (
                min(r, c) < 0 or
                r == ROWS or
                c == COLS or
                (r, c) in visit or
                image[r][c] != orig
            ):
                return
            # adjacent pixel equals orig
            if image[r][c] == orig:
                image[r][c] = color

            visit.add((r,c))

            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)

            visit.remove((r,c))

        dfs(sr, sc, set())
        return image
            

            