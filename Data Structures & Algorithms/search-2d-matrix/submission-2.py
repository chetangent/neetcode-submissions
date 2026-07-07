class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = 0, len(matrix) - 1
        while (h - l) > 1:
            mid = l + (h - l) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                h = mid
            else:
                l = mid
        if matrix[h][0] > target:
            res = l
        else:
            res = h
        l, h = 0, len(matrix[l]) - 1
        while l <= h:
            mid = l + (h - l) // 2
            if matrix[res][mid] == target:
                return True
            elif matrix[res][mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        return False