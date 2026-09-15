class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        sval=numbers[start]
        end=len(numbers)-1
        eval=numbers[end]
        while start  != end:
            if eval + sval > target:
                end-=1
                eval=numbers[end]
            elif eval + sval < target:
                start+=1
                sval=numbers[start]
            else:
                return [start+1,end+1]
        return [start,end]