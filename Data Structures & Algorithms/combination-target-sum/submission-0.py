class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, pos = [], []
        n = len(nums)
        nums = sorted(nums)

        #keep finding the remainder to get to target
        def backtrack(i, target):
            #Base case- when we reach the end of all option
            if target == 0:
                return res.append(list(pos))
            #Case 1- we are less than, so keep adding
            if target < 0 or i == n:
                return

            pos.append(nums[i])
            backtrack(i, target - nums[i])
            pos.pop()
            
            #Case 2- we skip the current number
            backtrack(i + 1, target)

        backtrack(0, target)
        return res