class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen ={}
        arr=[]
        arrf=[]
        count=0
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num]+=1
        arr = sorted(seen.items(),key=lambda x: x[1])
        while k > 0:
            arrf.append(arr[len(arr)-k][0])
            k -=1

        return arrf