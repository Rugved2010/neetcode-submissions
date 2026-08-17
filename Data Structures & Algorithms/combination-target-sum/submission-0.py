class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        sol=[]

        def backtrack(i,rt):
            if rt==0:
                res.append(sol.copy())
                return
            
            if rt<0 or i>=len(nums):
                return
            
            #Include
            sol.append(nums[i])
            backtrack(i,rt-nums[i])
            sol.pop()

            #Skip
            backtrack(i+1,rt)
        
        backtrack(0,target)
        return res