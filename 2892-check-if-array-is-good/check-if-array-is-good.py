class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) != max(nums)+1:
            return False
        
        n = max(nums)

        expected= list(range(1,n))+[n,n]

        return sorted(nums)== expected