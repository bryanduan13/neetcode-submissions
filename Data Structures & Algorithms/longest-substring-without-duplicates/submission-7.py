class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s =="":
            return 0
        seen={}
        start=0
        longest=1
        for i,char in enumerate(s):
            if char in seen and seen[char]>=start:
                start=seen[char]+1
            seen[char]=i
            if i-start+1 > longest:
                longest = i-start+1
        return longest