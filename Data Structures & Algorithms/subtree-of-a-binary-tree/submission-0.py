# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def issametree(self, p:[TreeNode],q:[TreeNode]) ->bool:
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        
        left=self.issametree(p.left,q.left)
        right=self.issametree(p.right,q.right)

        return left and right
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        if self.issametree(root,subRoot):
            return True

        left=self.isSubtree(root.left,subRoot)
        right=self.isSubtree(root.right,subRoot)

        return left or right