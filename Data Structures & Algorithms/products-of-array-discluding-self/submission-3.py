class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		arr=[]
		first = 1
		last = 1
		i = 0
		l =0
		while i < len(nums):
			arr.append(first)
			first *=nums[i]
			i+=1
		while l < len(nums):
			arr[len(nums)-1-l] *=last
			last *= nums[len(nums)-1-l]
			l+=1
		return arr