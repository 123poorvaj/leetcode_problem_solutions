

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)

        # If total is odd → cannot split equally
        if total % 2 != 0:
            return False

        target = total // 2

        # Check horizontal cut
        prefix = 0
        for i in range(len(grid) - 1):   # last row cannot be cut
            prefix += sum(grid[i])
            if prefix == target:
                return True

        # Check vertical cut
        prefix = 0
        n = len(grid[0])
        for j in range(n - 1):   # last column cannot be cut
            col_sum = 0
            for i in range(len(grid)):
                col_sum += grid[i][j]
            prefix += col_sum
            if prefix == target:
                return True

        return False