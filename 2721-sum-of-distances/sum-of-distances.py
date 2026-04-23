class Solution:
    def distance(self, nums: List[int]) -> List[int]:
            #arr=[]
            #for i in range(len(nums)):
             #   result=0
              #  for j in range(len(nums)):
               #     if nums[i]==nums[j] and j!=i:
                #        result+=abs(i-j)
                #arr.append(result)
            
            #return arr

            index_map=defaultdict(list) #creates a hashmap 
            for i, num in enumerate(nums):
                index_map[num].append(i)

            result = [0] * len(nums)

        # Step 2: Process each group
            for num in index_map:
                indices = index_map[num]
                prefix_sum = [0]

            # Build prefix sum
                for idx in indices:
                    prefix_sum.append(prefix_sum[-1] + idx)

                n = len(indices)

                for i in range(n):
                    idx = indices[i]

                # Left side
                    left = idx * i - prefix_sum[i]

                # Right side
                    right = (prefix_sum[n] - prefix_sum[i+1]) - idx * (n - i - 1)

                    result[idx] = left + right

            return result

                    