using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _112_Path_Sum
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            TreeNode root = new TreeNode(3)
            {
                //left = new TreeNode(9),
                right = new TreeNode(15)
                //{
                //    left = new TreeNode(15),
                //    right = new TreeNode(0)
                //}
            };

            solution.HasPathSum(root, 33);
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
            public bool HasPathSum(TreeNode root, int sum)
            {
                return root == null ? false ://無樹
                       
                    
                    root.val == sum && root.left == null && root.right == null//無葉
                       
                    || HasPathSum(root.left, sum - root.val)//至底:F；有葉:往下探
                    
                    || HasPathSum(root.right, sum - root.val);
            }
        }
    }
}
