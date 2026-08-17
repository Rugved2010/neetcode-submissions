class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={')':'(',']':'[','}':'{'}
        stack=[]

        for c in s:
            if c in hashmap:
                top=stack.pop() if stack else '#'
                if hashmap[c]!=top:
                    return False
            else:
                stack.append(c)
        return not stack