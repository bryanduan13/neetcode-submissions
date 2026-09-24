class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr=[]
        first = 1
        last = 1
        for i in range(len(nums)):
            arr.append(first)
            first *= nums[i]

        for l in range(len(nums)):
            arr[len(nums)-1-l] *=last
            last *= nums[len(nums)-1-l]

        return arr