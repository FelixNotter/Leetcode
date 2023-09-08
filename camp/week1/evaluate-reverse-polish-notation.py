class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])

        for char in tokens:
            if char.lstrip('-').isdigit():
                stack.append(char)

            else:
                res = 0
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())
                if char == '+':
                    res += operand2 + operand1
                elif char == '*':
                    res += operand2 * operand1
                elif char == '/':
                    res += int(operand2 / operand1)
                elif char == '-':
                    res += operand2 - operand1

                stack.append(res)

        return res