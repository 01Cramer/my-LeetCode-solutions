class Solution:
    def isValid(self, s: str) -> bool:
        stack_1 = []
        stack_2 = []

        for char in s:
            stack_1.append(char)
        for i in range(len(stack_1)):
            el = stack_1.pop()
            if el == "(":
                if len(stack_2) != 0 and stack_2[-1] == ")":
                    stack_2.pop()
                else:
                    stack_2.append(el)
            elif el == ")":
                if len(stack_2) != 0 and stack_2[-1] == "(":
                    return False
                else:
                    stack_2.append(el)
            elif el == "[":
                if len(stack_2) != 0 and stack_2[-1] == "]":
                    stack_2.pop()
                else:
                    stack_2.append(el)
            elif el == "]":
                if len(stack_2) != 0 and stack_2[-1] == "[":
                    return False
                else:
                    stack_2.append(el)
            elif el == "{":
                if len(stack_2) != 0 and stack_2[-1] == "}":
                    stack_2.pop()
                else:
                    stack_2.append(el)
            elif el == "}":
                if len(stack_2) != 0 and stack_2[-1] == "{":
                    return False
                else:
                    stack_2.append(el)
        return len(stack_2) == 0
