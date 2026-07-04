class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        left=0
        right=len(arr)

        while left<right:
            if arr[left]==0:
                arr.insert(left+1,0)
                arr.pop()
                left+=2
            else:
                left+=1
            
        