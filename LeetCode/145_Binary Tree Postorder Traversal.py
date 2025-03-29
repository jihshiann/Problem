from turtle import right
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        prev = None

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                result.append(curr.val)
                prev = curr
                if curr.right != prev:
                    curr = curr.right

        return result




# ���U��ơG�ھڼh�ǹM�����C��إߤG�e��
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    # ���إߩҦ��`�I�]None ���M�O�� None�^
    tree_nodes = [TreeNode(val) if val is not None else None for val in nodes]
    # �N�`�I�C�����A�Χ@�u�X�l�`�I
    kids = tree_nodes[::-1]
    # �Ĥ@�Ӥ����O�ڸ`�I
    root = kids.pop()
    for node in tree_nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

# ���ծר�
if __name__ == '__main__':
    # �w�q�𪺼h�ǹM���C���ܡANone ��ܪŸ`�I
    test_list = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
    # �إߤG�e��
    root = build_tree(test_list)
    
    # �إ߸Ѫk��ҡA�éI�s���ǹM��
    s = Solution()
    output = s.postorderTraversal(root)
    
    # �L�X���ǹM�����G
    print(output)
