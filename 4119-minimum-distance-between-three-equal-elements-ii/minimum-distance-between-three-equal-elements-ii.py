class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        
        # Step 1: store indices
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        ans = float('inf')
        
        # Step 2: process each value
        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            # Step 3: check consecutive triplets
            for i in range(len(indices) - 2):
                first = indices[i]
                third = indices[i + 2]
                
                distance = 2 * (third - first)
                ans = min(ans, distance)
        
        return ans if ans != float('inf') else -1
        