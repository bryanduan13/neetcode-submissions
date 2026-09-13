class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        stack = []
        prev=""
        count=-1
        for char in s:
            if char == ")" :
                if stack==[]:
                    return False
                if stack[count] =="(":
                    stack.pop()
                    count-=1
                else:
                    return False
            elif char == "}":
                if stack==[]:
                    return False
                if stack[count] == "{":
                    stack.pop()
                    count-=1
                else:
                    return False
            elif char == "]":
                if stack==[]:
                    return False
                if stack[count] == "[":
                    stack.pop()
                    count-=1
                else:
                    return False
            else:
                stack.append(char)
                count+=1

        return stack ==[]