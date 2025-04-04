from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # DFS 返回 (depth, lca)
        def dfs(node: Optional[TreeNode]):
            if not node:
                return (0, None)
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            # 如果左右子樹深度相同，則當前 node 是最低公共祖先
            if left_depth == right_depth:
                return (left_depth + 1, node)
            elif left_depth > right_depth:
                return (left_depth + 1, left_lca)
            else:
                return (right_depth + 1, right_lca)
        
        return dfs(root)[1]

# --------------------
# 輔助函數：建立二叉樹（層序遍歷的列表表示，None 表示空節點）
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes or nodes[0] is None:
        return None
    root = TreeNode(nodes[0])
    queue = deque([root])
    index = 1
    while queue and index < len(nodes):
        node = queue.popleft()
        if index < len(nodes):
            left_val = nodes[index]
            index += 1
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
        if index < len(nodes):
            right_val = nodes[index]
            index += 1
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
    return root

# 輔助函數：將樹轉換為列表（層序遍歷）
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # 去除末尾多餘的 None
    while result and result[-1] is None:
        result.pop()
    return result

# --------------------
# 測試案例
if __name__ == "__main__":
    sol = Solution()

    # Example 1:
    # Input: root = [3,5,1,6,2,0,8,null,null,7,4]
    # Output: [2,7,4]
    # 說明：最深葉節點為 7 和 4，LCA 為 2，故返回節點 2 的子樹： [2,7,4]
    tree_list1 = [3,5,1,6,2,0,8,None,None,7,4]
    root1 = build_tree(tree_list1)
    lca1 = sol.lcaDeepestLeaves(root1)
    print("Example 1 LCA subtree (level order):", tree_to_list(lca1))  # 預期輸出 [2,7,4]

    # Example 2:
    # Input: root = [1]
    # Output: [1]
    tree_list2 = [1]
    root2 = build_tree(tree_list2)
    lca2 = sol.lcaDeepestLeaves(root2)
    print("Example 2 LCA subtree (level order):", tree_to_list(lca2))  # 預期輸出 [1]

    # Example 3:
    # Input: root = [0,1,3,null,2]
    # Output: [2]
    tree_list3 = [0,1,3,None,2]
    root3 = build_tree(tree_list3)
    lca3 = sol.lcaDeepestLeaves(root3)
    print("Example 3 LCA subtree (level order):", tree_to_list(lca3))  # 預期輸出 [2]
