class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            match i:
                case "+":
                    stack.append(stack.pop()+stack.pop())
                case "-":
                    a,b=stack.pop(),stack.pop()
                    stack.append(b-a)
                case "*":
                    stack.append(stack.pop()*stack.pop())
                case "/":
                    a,b=stack.pop(),stack.pop()
                    stack.append(int(b/a))
                case _:
                    stack.append(int(i))
        return stack[0]
                    
                