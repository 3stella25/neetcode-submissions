# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    #queue for BFS should be a deque
    #Add the root, process 1 level at a time
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        node = root
        if not node:
            return []
        queue = deque([root])
        results = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val) 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(level)
        return results


        
        

        