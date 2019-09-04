using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _111_Minimum_Depth_of_Binary_Tree
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            TreeNode root = new TreeNode(3)
            {
                left = new TreeNode(9),
                right = new TreeNode(15)
                {
                    left = new TreeNode(15),
                    right = new TreeNode(0)
                }
            };

            solution.MinDepth(root);
        }

        public class TreeNode
        {
            public int val;
            public TreeNode left;
            public TreeNode right;
            public TreeNode(int x) { val = x; }
        }

        public class Solution
        {
            public int MinDepth(TreeNode root)
            {
                if (root == null)
                    return 0;
                else if (root.left == null && root.right == null)
                    return 1;

                List<int> depth = new List<int>();
                Count(root, depth);
                
                return depth.Min();
            }
            List<int> Count(TreeNode node, List<int> depth)
            {
                if (node.left == null && node.right == null)
                {
                    depth.Add(1);
                    return depth;
                }

                dfs(node, 0, ref depth);

                return depth;
            }
            void dfs(TreeNode node, int level, ref List<int> depth)
            {
                level++;
                if (node.left == null && node.right == null)
                {
                    depth.Add(level);
                    level--;
                    return;
                }
                else if (node.left != null)
                {
                    dfs(node.left, level, ref depth);
                }
                if (node.right != null)
                {
                    dfs(node.right, level, ref depth);
                }
            }
        }
    }
}
