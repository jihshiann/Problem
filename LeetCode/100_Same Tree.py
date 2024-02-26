# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # �p�G��Ӹ`�I���ONone�A�h�{�����̬ۦP
        if not p and not q:
            return True
        # �p�G�䤤�@�Ӹ`�I�ONone�ӥt�@�Ӥ��O�A�h���̤��ۦP
        if not p or not q:
            return False
        # �p�G�`�I���Ȥ��۵��A�h���̤��ۦP
        if p.val != q.val:
            return False
        # ���j�ˬd���l��M�k�l��
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        