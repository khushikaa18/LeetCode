class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m=len(matrix)
        n=len(matrix[0])

        left=0
        right=n-1

        while left<m and right>=0:
            val=matrix[left][right]

            if val == target:
                return True
            
            elif val<target:
                left+=1
            else:
                right-=1
        
        return False