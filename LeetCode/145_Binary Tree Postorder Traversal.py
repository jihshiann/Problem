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




# 輔助函數：根據層序遍歷的列表建立二叉樹
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    # 先建立所有節點（None 仍然保持 None）
    tree_nodes = [TreeNode(val) if val is not None else None for val in nodes]
    # 將節點列表反轉，用作彈出子節點
    kids = tree_nodes[::-1]
    # 第一個元素是根節點
    root = kids.pop()
    for node in tree_nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

# 測試案例
if __name__ == '__main__':
    # 定義樹的層序遍歷列表表示，None 表示空節點
    test_list = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
    # 建立二叉樹
    root = build_tree(test_list)
    
    # 建立解法實例，並呼叫中序遍歷
    s = Solution()
    output = s.postorderTraversal(root)
    
    # 印出中序遍歷結果
    print(output)
