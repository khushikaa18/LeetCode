class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n=len(nums)
        answer=0
        for i in range(32):
            c1=0
            for num in nums:
                if ((num >> i) & 1):
                    c1+=1
            answer+=c1 * (n-c1)
        return answer
