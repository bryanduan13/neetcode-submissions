class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        seens={}
        for char in s:
            if char in seens:
                seens[char] +=1
            else:
                seens[char] = 1
        for chars in t:
            if chars not in seens:
                return False
            elif seens[chars] >1:
                seens[chars]-=1
            else:
                del seens[chars]
        if seens!={}:
            return False
        return True
