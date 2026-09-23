# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    rightint=0
    leftint=0
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkBal(root)!=-1
    def checkBal(self,root:Optional[TreeNode])-> int:
        if root is None:
            return 0
        lefth=self.checkBal(root.left)
        if lefth==-1:
            return -1
        righth=self.checkBal(root.right)
        if righth==-1:
            return -1
        dif = abs(lefth-righth)
        if dif >1:
            return -1
        return max(lefth,righth)+1
