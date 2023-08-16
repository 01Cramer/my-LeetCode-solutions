from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if (
                tokens[i] != "+"
                and tokens[i] != "-"
                and tokens[i] != "*"
                and tokens[i] != "/"
            ):
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b + a)
                elif tokens[i] == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                elif tokens[i] == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b * a)
                elif tokens[i] == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))
        return stack[-1]
