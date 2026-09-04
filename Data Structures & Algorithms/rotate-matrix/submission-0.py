class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l<r:
            top, bottom = l, r
            for i in range(r-l):
                matrix[top][l+i], matrix[top+i][r], matrix[bottom-i][l], matrix[bottom][r-i] = matrix[bottom-i][l], matrix[top][l+i], matrix[bottom][r-i], matrix[top+i][r]
            l+=1
            r-=1
        