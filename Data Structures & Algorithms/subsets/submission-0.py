class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        path = []

        def backtrack(i): #Keep the counter
            #base case- return when we run out of options
            if i == len(nums):
                results.append(path[:])
                return
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

            #We skip it
            backtrack(i+1)
        backtrack(0)
        return results
        