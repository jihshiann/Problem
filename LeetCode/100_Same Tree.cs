using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _100_Same_Tree
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            TreeNode p = new TreeNode(1)
            {
                left = new TreeNode(2)
            };
            TreeNode q = new TreeNode(1)
            {
                right = new TreeNode(2)
            };

            Console.WriteLine(solution.IsSameTree(p, q));
            Console.ReadLine();
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
            public bool IsSameTree(TreeNode p, TreeNode q)
            {
                return (p == null && q == null) ||
                    (p != null && q != null && p.val == q.val 
                    && IsSameTree(p.left, q.left) && IsSameTree(p.right, q.right));
            }
        }
    }
}
