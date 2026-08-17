class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
        for k,v in enumerate(nums):
            diff=target-v
            if diff in res:
                return [res[diff],k]
            res[v]=k