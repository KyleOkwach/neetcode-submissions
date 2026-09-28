class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        w, h = len(matrix[0]), len(matrix)
        l, r = 0, (w * h) - 1

        while l <= r:
            m = (l + r) // 2
            i, j =  m // w, m % w
            val = matrix[i][j]

            if target == val:
                return True
            elif target < val:
                r = m - 1
            else:
                l = m + 1


        return False
        