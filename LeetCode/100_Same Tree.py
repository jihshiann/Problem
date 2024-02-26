# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 如果兩個節點都是None，則認為它們相同
        if not p and not q:
            return True
        # 如果其中一個節點是None而另一個不是，則它們不相同
        if not p or not q:
            return False
        # 如果節點的值不相等，則它們不相同
        if p.val != q.val:
            return False
        # 遞迴檢查左子樹和右子樹
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        