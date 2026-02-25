class Solution:
    def decodeString(self, s: str) -> str:
        stack = []          # stores previous strings
        num_stack = []      # stores repeat counts
        curr = ""           # current working string
        num = 0             # current number being built

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)   # handle multi-digit numbers

            elif ch == "[":
                num_stack.append(num)
                stack.append(curr)
                num = 0
                curr = ""

            elif ch == "]":
                repeat = num_stack.pop()
                prev = stack.pop()
                curr = prev + curr * repeat

            else:  # alphabet
                curr += ch

        return curr