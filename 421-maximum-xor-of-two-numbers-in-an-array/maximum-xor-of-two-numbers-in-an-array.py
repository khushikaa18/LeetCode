class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_or=0
        mask=0

        for i in range(31,-1,-1):
            mask|=(1<<i)

            prefix={num & mask for num in nums}

            candidate=max_or |(1<<i)

            for p in prefix:
                if (candidate^p) in prefix:
                    max_or=candidate
                    break
        
        return max_or
