class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m=len(grid)
        n=len(grid[0])

        arr = []
        for row in grid:
            for val in row:
                arr.append(val)
        
        rem = arr[0] % x
        for val in arr:
            if val % x != rem:
                return -1
        
        # Step 3: Sort array
        arr.sort()
        
        # Step 4: Find median
        median = arr[len(arr)//2]
        
        # Step 5: Calculate operations
        operations = 0
        for val in arr:
            operations += abs(val - median) // x
        
        return operations
