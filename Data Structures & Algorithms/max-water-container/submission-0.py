class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=0
        right=n-1
        area=0
        while left<right:
            width=right-left
            curr=width * min(heights[left],heights[right])

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
            area=max(area,curr)
        
        return area