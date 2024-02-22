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
                if (root == null) return 0;
                else if (root.left == null) return 1 + MinDepth(root.right);
                else if (root.right == null) return 1 + MinDepth(root.left);

                return 1 + Math.Min(MinDepth(root.left), MinDepth(root.right));
            }
        }
    }
}
