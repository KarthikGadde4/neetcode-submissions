class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}" : "{", ")" : "(", "]" : "["}
        stack = []

        for c in s:
            if c in hashmap:
                if not stack or hashmap[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack