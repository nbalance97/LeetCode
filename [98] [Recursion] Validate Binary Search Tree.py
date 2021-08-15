# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        flag = False
        def validate(root, parent_val, less):
            if root == None:
                return True
            
            if parent_val != None:
                if less: # left
                    if root.left and (root.left.val >= root.val or root.left.val >= parent_val):
                        return False
                    if root.right and (root.right.val <= root.val or root.right.val >= parent_val):
                        return False
                else: # right
                    if root.left and (root.left.val >= root.val or root.left.val <= parent_val):
                        return False
                    if root.right and (root.right.val <= root.val or root.right.val <= parent_val):
                        return False
            else:
                if root.left and root.left.val >= root.val:
                    return False
                if root.right and root.right.val <= root.val:
                    return False
                

            return validate(root.left, root.val, True) and validate(root.right, root.val, False)
        return validate(root, None, False) 
