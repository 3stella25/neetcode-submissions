# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Base case is node is None --> return
swap left and right

recursive call invertTree(self, node.right)
                invertTree(self, node.left)
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        if not node:
            return None
        else:
            temp = node.left
            node.left = node.right
            node.right = temp
            self.invertTree(node.right)
            self.invertTree(node.left)
            return node
        
            