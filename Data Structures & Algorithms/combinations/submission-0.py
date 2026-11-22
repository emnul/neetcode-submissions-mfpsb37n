class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combos = []

        def dfs(i, curCombo):
            if len(curCombo) == k:
                combos.append(curCombo[::])
                return

            for j in range(i, n+1):
                curCombo.append(j)
                dfs(j+1, curCombo)
                curCombo.pop()
            

        dfs(1, [])
        return combos