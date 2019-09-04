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
            TreeNode root = new TreeNode(1)
            {
                left = new TreeNode(2)
                {
                    right = new TreeNode(3)
                },
                right = new TreeNode(2)
                {
                    right = new TreeNode(3)
                }
            };
            Console.WriteLine(solution.IsSymmetric(root));
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
            public bool IsSymmetric(TreeNode root)
            {
                List<int?> leftList = new List<int?>();
                List<int?> rightList = new List<int?>();
                if (root == null)
                {
                    return true;
                }

                LeftSearch(root, leftList);
                RightSearch(root, rightList);

                return string.Join(",", leftList) == string.Join(",", rightList);
            }
            void LeftSearch(TreeNode root, List<int?> leftList)
            {
                leftList.Add(root.val);

                if (root.left != null)
                {
                    LeftSearch(root.left, leftList);
                }
                else
                {
                    leftList.Add(null);
                }

                if (root.right != null)
                {
                    LeftSearch(root.right, leftList);
                }
                else
                {
                    leftList.Add(null);
                }

            }

            void RightSearch(TreeNode root, List<int?> rightList)
            {
                rightList.Add(root.val);

                if (root.right != null)
                {
                    RightSearch(root.right, rightList);
                }
                else
                {
                    rightList.Add(null);
                }

                if (root.left != null)
                {
                    RightSearch(root.left, rightList);
                }
                else
                {
                    rightList.Add(null);
                }

            }
        }
    }
}
