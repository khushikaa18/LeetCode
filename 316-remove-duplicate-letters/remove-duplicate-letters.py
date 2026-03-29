class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last={}

        for i,ch in enumerate(s):
            last[ch]=i
        
        visited=set()
        stack=[]

        for i,ch in enumerate(s):
            if ch in visited:
                continue
            
            while stack and ch < stack[-1] and last[stack[-1]] > i:
                removed = stack.pop()
                visited.remove(removed)

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)