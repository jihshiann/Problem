# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        
        def depth(node):
            if not node:
                return 0
            # ���k�p�⥪�l��M�k�l�𪺲`��
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # ��s���|
            self.diameter = max(self.diameter, left_depth + right_depth)
            # ��^�Ӹ`�I���`��
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.diameter
    
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
#      1
#     / \
#    2   3
#   / \
#  4   5
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5


solution = Solution()
diameter = solution.diameterOfBinaryTree(node1)