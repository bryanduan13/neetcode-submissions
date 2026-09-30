class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums ==[]:
            return 0
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num]=1
        highest = 1
        counter =1
        for number in list(seen):
            if number not in seen:
                continue
            while number -1 in seen:
                number-=1
            while number +1 in seen:
                seen.pop(number+1)
                number +=1
                counter +=1
            if counter > highest:
                highest = counter
            counter = 1
        return highest
