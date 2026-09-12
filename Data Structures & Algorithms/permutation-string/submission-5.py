class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen= self.makeDict(s1)
        backup= seen.copy()
        for i in range(len(s2)):
            if i + len(s1) > len(s2):
                break
            if s2[i] in seen:
                for l in range(len(s1)):
                    if s2[i+l] not in seen:
                            break
                    seen[s2[i+l]]-=1
                    if seen[s2[i+l]]==0:
                            seen.pop(s2[i+l])
                if seen =={}:
                    return True
                else:
                    seen = backup.copy()
        return False

    def makeDict(self, s1:str) -> dict:
        seen={}
        for char in s1:
            if char not in seen:
                seen[char]=1
            else:
                seen[char]+=1
        return seen
