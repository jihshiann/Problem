# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Create the binary search trees from the examples
# Example 1
root1 = TreeNode(10)
root1.left = TreeNode(5, TreeNode(3), TreeNode(7))
root1.right = TreeNode(15, None, TreeNode(18))

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0

        # �p�G�`�I�Ȥp��d�򪺤U���A�h�u�Ҽ{�k�l��
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        # �p�G�`�I�Ȥj��d�򪺤W���A�h�u�Ҽ{���l��
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        # �p�G�`�I�Ȧb�d�򤺡A�h�[�W�Ӹ`�I�Ȩû��j�B�z���k�l��
        else:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        

    # Calculate the sums for the given ranges
    sum1 = rangeSumBST(root1, 7, 15)  # Example 1