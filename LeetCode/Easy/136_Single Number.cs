using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _136_Single_Number
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            int[] nums = new int[] { 4, 1, 2, 1, 2 };
            solution.SingleNumber(nums);
        }
    }

    public class Solution
    {
        public int SingleNumber(int[] nums)
        {
            int x = 0;
            for (int i = 0; i < nums.Length; i++)
                x ^= nums[i];
            return x;
        }
    }
}
