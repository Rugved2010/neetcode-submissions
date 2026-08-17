class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1_count={}
        for i in s1:
            s1_count[i]=s1_count.get(i,0)+1
        
        window={}
        window_length=len(s1)

        for i in range(window_length):
            char=s2[i]
            window[char]=window.get(char,0)+1
        
        if window==s1_count:
            return True
        
        left=0
        for right in range(window_length,len(s2)):
            char_right=s2[right]
            window[char_right]=window.get(char_right,0)+1
            window[s2[left]]-=1
            if window[s2[left]]==0:
                del window[s2[left]]
            left+=1

            if window==s1_count:
                return True
        return False