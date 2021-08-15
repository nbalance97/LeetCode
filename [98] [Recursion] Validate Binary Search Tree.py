# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        flag = False
        def validate(root, fr, to):
            if root == None:
                return True
            
            if fr < root.val and root.val < to:
                return validate(root.left, fr, root.val) and validate(root.right, root.val, to)
            else:
                return False
            
        return validate(root, -2**32, 2**32) 
