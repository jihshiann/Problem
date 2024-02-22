class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        def dfs(node):
            if node is None:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)

        graph = defaultdict(list)
        dfs(root)
        visited = set()
        queue = deque([start])
        time = -1
        while queue:
            time += 1
            for _ in range(len(queue)):
                current_node = queue.popleft()
                visited.add(current_node)
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return time

# Example Usage
root = TreeNode(1, TreeNode(5, None, TreeNode(4)), TreeNode(3, TreeNode(10, TreeNode(9), TreeNode(2)), TreeNode(6)))
print(Solution.amountOfTime(root, 3)) # ���T����X���ӬO4




# �d�s�ƥ�

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def amountOfTime(self, root: TreeNode, start: int) -> int:

#         # �p��`�I���`��
#         def depth(node):
#             if not node:
#                 return 0
#             return 1 + max(depth(node.left), depth(node.right))

#         def distance_from_root_to_start(root, start):
#             # Helper function to find the distance to the target
#             def find_distance(node, target, distance):
#                 if node is None:
#                     return -1
#                 if node.val == target:
#                     return distance
#                 left_distance = find_distance(node.left, target, distance + 1)
#                 if left_distance != -1:
#                     return left_distance
#                 right_distance = find_distance(node.right, target, distance + 1)
#                 return right_distance

#             return find_distance(root, start, 0)
        
#         def is_in_left_or_right_subtree(root, start):
#             # Helper function to check if target exists in subtree
#             def exists_in_subtree(node, target):
#                 if node is None:
#                     return False
#                 if node.val == target:
#                     return True
#                 return exists_in_subtree(node.left, target) or exists_in_subtree(node.right, target)

#             if root is None:
#                 return None
#             if exists_in_subtree(root.left, start):
#                 return True
#             elif exists_in_subtree(root.right, start):
#                 return False
#             else:
#                 return None

#         # �M��start�`�I�íp��һݮɶ�
#         def dfs(node):
#             if not node:
#                 return 0
#             elif node.val == start:
#                 # start�`�I�O�ڸ`�I�A��^�̤j�`��
#                 return depth(node)-1
            
#             depthL = depth(node.left)
#             depthR = depth(node.right)
#             depthStart = distance_from_root_to_start(node, start)
#             # TODO 
#             # isLeft = is_in_left_or_right_subtree(node, start)
#             # if isLeft and depthStart>depthR:
#             #   depthR + root��start�Z��
#             # if start�b�k�l�� & depthL>depthR:
#             #   depth + root��start�Z��
                 

#         return dfs(root)
        
       

#     # Create the binary search trees from the examples
#     # Example 1
#     root1 = TreeNode(10)
#     root1.left = TreeNode(5, TreeNode(3), TreeNode(7))
#     root1.right = TreeNode(15, None, TreeNode(18))
       
