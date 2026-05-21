class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix=set()
        ans=0

        for num in arr1:
            s=str(num)

            for i in range(1,len(s)+1):
                prefix.add(s[:i])
        
        for num in arr2:
            s=str(num)

            for i in range(1,len(s)+1):
                if s[:i] in prefix:
                    ans=max(ans,i)

        return ans
