class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        left=0
        check=set()
        max_length=0

        for right in range(n):
            while s[right] in check:
                check.remove(s[left])
                left+=1
            check.add(s[right])
            max_length=max(max_length,right-left+1)
        return max_length