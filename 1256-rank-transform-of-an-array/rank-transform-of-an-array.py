class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr=sorted(set(arr))

        rank={}
        ans=[]

        for i in range(len(sorted_arr)):
            rank[sorted_arr[i]] = i+1

        for num in arr:
            ans.append(rank[num])
        
        return ans
                