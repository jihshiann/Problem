using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _107_Binary_Tree_Level_Order_Traversal_II
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            TreeNode tree = new TreeNode(3)
            {
                left = new TreeNode(9)
                {
                    left = new TreeNode(9)
                    {
                        left = new TreeNode(15),
                        right = new TreeNode(7)

                    },
                    right = new TreeNode(9)
                    {
                        left = new TreeNode(15),
                        right = new TreeNode(7)

                    }
                },
                right = new TreeNode(20)
                {
                    left = new TreeNode(9)
                    {
                        left = new TreeNode(15),
                        right = new TreeNode(7)

                    },
                    right = new TreeNode(9)
                    {
                        left = new TreeNode(15),
                        right = new TreeNode(7)

                    }
                }
            };
            solution.LevelOrderBottom(tree);
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
            public IList<IList<int>> LevelOrderBottom(TreeNode root)
            {
                IList<IList<int>> tree = new List<IList<int>>();
                if (root == null)
                    return tree;

                Queue<TreeNode> queue = new Queue<TreeNode>();
                queue.Enqueue(root);
                makeList(queue, tree);

                return tree;
            }

            void makeList(Queue<TreeNode> queue, IList<IList<int>> tree)
            {

                var branch = new List<int>();
                int sameLevelBranchs = queue.Count();
                while (sameLevelBranchs > 0)
                {
                    var curBranch = queue.Dequeue();
                    branch.Add(curBranch.val);

                    if (curBranch.left != null)
                    {
                        queue.Enqueue(curBranch.left);
                    }

                    if (curBranch.right != null)
                    {
                        queue.Enqueue(curBranch.right);
                    }
                    sameLevelBranchs--;
                }

                tree.Insert(0, branch);
                if(queue.Any())
                makeList(queue, tree);
            }
        }
    }
}
