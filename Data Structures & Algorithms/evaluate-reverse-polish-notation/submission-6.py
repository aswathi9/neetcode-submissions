class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res=0
        for char in tokens:
            if char not in '+-/*':
                stack.append(int(char))
            else:
                a=stack.pop()
                b=stack.pop()
                if char=='+':
                    res=a+b
                elif char=='-':
                    res=b-a
                elif char=='*':
                    res=a*b
                elif char=='/':
                    res=int(b/a)
                stack.append(res)
        return stack[-1]
