class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams={}
        arr=[]
        ind = 0
        for string in strs:
            key = "".join(sorted(string))
            if key not in anagrams:
                anagrams[key]= ind
                ind+=1
                arr.append([])
                arr[anagrams[key]].append(string)
            else:
                arr[anagrams[key]].append(string)
            
        return arr