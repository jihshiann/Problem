using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _108_Convert_Sorted_Array_to_Binary_Search_Tree
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            int[] nums = new int[] { -10,-5, -3, 0, 3,5, 6, 9 };
            solution.SortedArrayToBST(nums);
        }
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
        public TreeNode SortedArrayToBST(int[] nums)
        {
            if (nums.Length == 0)
                return null;

            int left = 0;
            int right = nums.Length-1;
            int mid = (left + right) / 2;
            TreeNode tree = new TreeNode(nums[mid]);
            if (left < right)
            {
                MakeTree(tree, nums, left, mid);
                MakeTree(tree, nums, mid+1, right);
            }

            return tree;
        }
        void MakeTree(TreeNode tree, int[] nums, int left, int right)
        {
            if (left < right)
            {
                int mid = (left + right) / 2;
                if (nums[mid] > tree.val)
                {
                    tree.right = new TreeNode(nums[mid]);
                    MakeTree(tree.right, nums, left, mid);
                    MakeTree(tree.right, nums, mid + 1, right);
                }
                else if (nums[mid] < tree.val)
                {
                    tree.left = new TreeNode(nums[mid]);
                    MakeTree(tree.left, nums, left, mid);
                    MakeTree(tree.left, nums, mid + 1, right);
                }
            }
            else if (left == right && right == nums.Length - 1)
            {
                tree.right = new TreeNode(nums[right]) ;
            }
        }
    }
}
