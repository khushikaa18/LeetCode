class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]

        for i in range(len(nums)):
            sq=nums[i]*nums[i]
            ans.append(sq)
        ans.sort()
        return ans