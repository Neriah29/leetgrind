class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        z = [j for i in matrix for j in i]  

        def a(z, l, r):
            m = (l+r)//2
            if l > r:
                return False
            elif z[m] == target:
                return True
            elif z[m]> target:
                return a(z, l, m-1)
            else:
                return a(z, m+1, r)
        return a(z, 0, len(z)-1)
                