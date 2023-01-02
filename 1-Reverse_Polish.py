class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        priority = {
            "*": lambda x,y: x*y,
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "/": lambda x,y: float(x)/y
        }

        lst = []
        for i in tokens:
            if i not in priority:
                lst.append(int(i))
            else:
                right = lst.pop()
                left = lst.pop()
                result = priority[i](left, right)
                lst.append(int(result))
        return lst.pop()
