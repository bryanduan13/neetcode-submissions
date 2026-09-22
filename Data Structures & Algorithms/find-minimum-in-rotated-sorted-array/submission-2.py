class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        min = nums[left]
        while left <= right:
            mid = (right+left)//2
            if nums[mid]>nums[right]:
                left = mid +1
            else:
                right = mid-1
            if nums[mid]<min:
                min = nums[mid]
                index = mid
        return min