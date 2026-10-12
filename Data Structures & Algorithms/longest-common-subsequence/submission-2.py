class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # i = index in text1, j = index in text2
        memo = {}
        def dfs(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            # avoid recalculating prev paths
            if (i,j) in memo:
                return memo[(i,j)]
            # found a match so we increment both ptrs, store in memo
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + dfs(i + 1, j + 1)
            else:
                # no match so we take the max of 2 possible decisions
                memo[(i,j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return memo[(i,j)]

        return dfs(0,0)