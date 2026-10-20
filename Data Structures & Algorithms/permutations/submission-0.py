class Solution:
    #Backtracking!!
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            else:
                for x in nums:
                    if x in path:
                        continue #skip it since permutations can't have duplicates
                    path.append(x)
                    backtrack()
                    path.pop()
        backtrack()
        return res
        