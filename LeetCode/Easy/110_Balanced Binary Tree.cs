using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _110_Balanced_Binary_Tree
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();

            TreeNode root = new TreeNode(3)
            {
                left = new TreeNode(9)
                {
                    left = new TreeNode(15)
                    {
                        left = new TreeNode(10)

                    }
                }
            };

            solution.IsBalanced(root);
        }

        //Definition for a binary tree node.
        public class TreeNode
        {
            public int val;
            public TreeNode left;
            public TreeNode right;
            public TreeNode(int x) { val = x; }
        }

        public class Solution
        {
            public bool IsBalanced(TreeNode root)
            {
                bool isBalanced = true;
                
                Dfs(root, ref  isBalanced);

                return isBalanced;
            }
            //Depth-First-Search
            int Dfs(TreeNode node, ref bool isBalanced)
            {
                //最底層為0
                if (node == null)
                    return 0;

                int leftLevel = Dfs(node.left, ref isBalanced), rightLevel = Dfs(node.right, ref  isBalanced);

                if (Math.Abs(leftLevel - rightLevel) > 1)
                    isBalanced = false;

                //每網上一層深度加一
                return Math.Max(leftLevel, rightLevel) + 1;
            }
        }
    }
}
