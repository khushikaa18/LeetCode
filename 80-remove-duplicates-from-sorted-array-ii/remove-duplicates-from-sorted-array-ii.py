class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0  # pointer for placing elements
        
        for num in nums:
            if i < 2 or nums[i-2] != num:
                nums[i] = num
                i += 1
        
        return i

        