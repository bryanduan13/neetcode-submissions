class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token =="+":
                one = stack.pop()
                two = stack.pop()
                one = two + one
                stack.append(one)
            elif token =="-":
                one = stack.pop()
                two = stack.pop()
                one = two - one
                stack.append(one)
            elif token =="*":
                one = stack.pop()
                two = stack.pop()
                one = two * one
                stack.append(one)
            elif token =="/":
                one = stack.pop()
                two = stack.pop()
                one = two / one
                stack.append(int(one))            
            else:
                stack.append(int(token))
        return stack[0]