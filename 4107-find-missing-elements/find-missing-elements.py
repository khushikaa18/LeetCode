class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num=set(nums)
        max_val=max(nums)
        min_val=min(nums)

        return [x for x in range(min_val,max_val+1) if x not in num]