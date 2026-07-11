class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_Area=0

        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                index=stack.pop()
                height=heights[index]

                if stack:
                    width=i-stack[-1]-1
                else:
                    width=i
                
                area=width*height
                max_Area=max(max_Area,area)
            stack.append(i)

        heights.pop()
        return max_Area