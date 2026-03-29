class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_abs = float('inf')
        neg_count = 0

        n = len(matrix)

        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                total += abs(val)
                min_abs = min(min_abs, abs(val))
                if val < 0:
                    neg_count += 1

        # If odd number of negative elements, subtract twice the smallest absolute value
        if neg_count % 2 == 1:
            total -= 2 * min_abs

        return total