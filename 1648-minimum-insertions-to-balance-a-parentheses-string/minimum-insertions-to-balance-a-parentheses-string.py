class Solution:
    def minInsertions(self, s: str) -> int:
        insertions=0
        needed=0

        for ch in s:
            if ch=='(':
                if needed % 2 !=0:
                    insertions+=1
                    needed-=1
                needed+=2
            else:
                needed-=1
                if needed <0:
                    insertions+=1
                    needed+=2
            
        return insertions+needed
            
            
        