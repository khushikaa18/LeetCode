class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n == 1:
            return 0

        position=defaultdict(list)

        for i,num in enumerate(arr):
            position[num].append(i)
        
        queue=deque([(0,0)])
        visited=set([0])

        while queue:
            i,steps=queue.popleft()

            if i == n - 1:
                return steps
            
            neighbors = [i - 1, i + 1] + position[arr[i]]

            for next_idx in neighbors:
                if 0 <= next_idx < n and next_idx not in visited:
                    visited.add(next_idx)
                    queue.append((next_idx, steps + 1))

            # Important optimization
            del position[arr[i]]

        return -1


        
        
        