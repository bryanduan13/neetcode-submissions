class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for string in strs:
            result += str(len(string)) + "#" + string
        return result
    def decode(self, s: str) -> List[str]:
        i = 0
        arr=[]
        length = ""
        j=0
        while i < len(s):
            j=i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i=j+1
            arr.append(s[i:j + length + 1])
            i+=length
        return arr
