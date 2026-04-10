class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = {}
        for i, val in enumerate(nums):
            if val not in pos:
                pos[val] = []
            pos[val].append(i)
    
        min_dist = float('inf')
        found = False
    
        for val in pos:
            indices = pos[val]
        # We need at least 3 occurrences to form a good tuple
            if len(indices) >= 3:
                for p in range(len(indices) - 2):
                # distance = abs(i-j) + abs(j-k) + abs(k-i)
                # For sorted i < j < k, distance is 2 * (k - i)
                    i, k = indices[p], indices[p+2]
                    dist = 2 * (k - i)
                    min_dist = min(min_dist, dist)
                    found = True
                
        return min_dist if found else -1