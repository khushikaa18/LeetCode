class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        common = 0

        result=[]

        for i in range(len(A)):
            for x in(A[i],B[i]):

                if x in seen:
                    common+=1
                else:
                    seen.add(x)
        
            result.append(common)

        return result
        

        
        

