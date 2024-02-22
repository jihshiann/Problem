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

        # 如果節點值小於範圍的下限，則只考慮右子樹
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        # 如果節點值大於範圍的上限，則只考慮左子樹
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        # 如果節點值在範圍內，則加上該節點值並遞迴處理左右子樹
        else:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        

    # Calculate the sums for the given ranges
    sum1 = rangeSumBST(root1, 7, 15)  # Example 1