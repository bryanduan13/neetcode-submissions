class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s=s.lower()
        if len(s)<=1:
            return True
        scurr=0
        ecurr=len(s)-1
        start = s[scurr]
        end=s[ecurr]
        while start==end:
            if ecurr==scurr or ecurr-1 == scurr:
                return True
            scurr+=1
            ecurr-=1
            start = s[scurr]
            end=s[ecurr]

        return False