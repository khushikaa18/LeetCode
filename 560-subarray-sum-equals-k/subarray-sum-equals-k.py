class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix={0:1}
        currentSum=0
        count=0

        for num in nums:
            currentSum+=num

            if currentSum-k in prefix:
                count+=prefix[currentSum-k]
            prefix[currentSum]=prefix.get(currentSum,0)+1

        return count