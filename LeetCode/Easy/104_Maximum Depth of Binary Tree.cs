using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _104_Maximum_Depth_of_Binary_Tree
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            TreeNode root = new TreeNode(9)
            {
                left = new TreeNode(9),
                right = new TreeNode(20)
                {
                    left = new TreeNode(15),
                    right = new TreeNode(7)
                }
            };
            Console.WriteLine(solution.MaxDepth(root));
            Console.ReadLine();
        }


        // Definition for a binary tree node.
        public class TreeNode
        {
            public int val;
            public TreeNode left;
            public TreeNode right;
            public TreeNode(int x) { val = x; }
        }

        public class Solution
        {
            public int MaxDepth(TreeNode root)
            {
                //int currDepth  = 1;
                //int totalDepth = 1;
                return (root == null) ? 0 : 1 + Math.Max(MaxDepth(root.left), MaxDepth(root.right));
            }
            //void search(TreeNode root, int currDepth, ref int totalDepth)
            //{
            //    bool sameLevel = false;
            //    if (root.left == null && root.right == null)
            //    {
            //        currDepth--;
            //    }
            //    else if (root.left != null)
            //    {
            //        sameLevel = true;
            //        currDepth++;
            //        if (currDepth > totalDepth)
            //        {
            //            totalDepth = currDepth;
            //        }
            //        search(root.left, currDepth, ref totalDepth);    
            //    }
            //    if (root.right != null)
            //    {
            //        if(!sameLevel)
            //        currDepth++;
            //        if (currDepth > totalDepth)
            //        {
            //            totalDepth = currDepth;
            //        }
            //        search(root.right, currDepth, ref totalDepth);
            //    }
            //}
        }
    }
}
