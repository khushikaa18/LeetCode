class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arr=[]
        depth=0

        for ch in s:
            if ch =='(':
                if depth > 0:
                    arr.append(ch)
                depth+=1
            else:
                depth-=1
                if depth>0:
                    arr.append(ch)

        return "".join(arr)