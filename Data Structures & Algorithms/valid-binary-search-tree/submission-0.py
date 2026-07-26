
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #go left -> high becomes current node's value, low stays the same
        #go right -> left becomes current node's value, high stays the same
        #At each node, check low < node.val < high
        node = root
        return self.validate(node, float('-inf'), float('inf'))

    def validate(self, node, low, high):
        if not node:
            return True
        if low < node.val < high:
            return self.validate(node.left, low, node.val ) and self.validate(node.right, node.val, high)
        return False
        