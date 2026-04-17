class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse_num(x):
            return int(str(x)[::-1])

        mp = {}   # reverse(number) -> index
        min_dist = float('inf')

        for j in range(len(nums)):
            # check if current number matches any previous reverse
            if nums[j] in mp:
                i = mp[nums[j]]
                min_dist = min(min_dist, j - i)

            # store reverse of current number
            rev = reverse_num(nums[j])
            mp[rev] = j

        return min_dist if min_dist != float('inf') else -1

        