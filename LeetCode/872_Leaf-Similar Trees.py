class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Helper function to get the leaf sequence
        def getLeafSequence(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return getLeafSequence(node.left) + getLeafSequence(node.right)

        # Get leaf sequences for both trees
        leafSeq1 = getLeafSequence(root1)
        leafSeq2 = getLeafSequence(root2)

        # Check if the leaf sequences are equal
        return leafSeq1 == leafSeq2


# Example usage of the class
# Construct the trees according to the given example
# Tree 1
root1 = TreeNode(3)
root1.left = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
root1.right = TreeNode(1, TreeNode(9), TreeNode(8))

# Tree 2
root2 = TreeNode(3)
root2.left = TreeNode(5, TreeNode(6), TreeNode(7))
root2.right = TreeNode(1, TreeNode(4), TreeNode(2, None, TreeNode(9, TreeNode(8))))

# Create an instance of the solution and test
solution = Solution()
result = solution.leafSimilar(root1, root2)
result