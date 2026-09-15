class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        left = max
        right = len(heights)-1
        li=heights[left]
        ri=heights[right]
        while left !=right:
            if (right-left) * min(li,ri) > max:
                max = (right-left) * min(li,ri)
            if li < ri:
                left +=1
                li=heights[left]
            else:
                right-=1
                ri = heights[right]
        return max