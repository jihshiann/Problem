using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Maximum_Subarray
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            int[] nums = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
            Console.WriteLine(solution.MaxSubArray(nums));
            Console.ReadLine();
        }

        public class Solution
        {
            public int MaxSubArray(int[] nums)
            {
                for (int i = 1; i < nums.Length; i++)
                {
                    if (nums[i - 1] + nums[i] > nums[i])//找到正數後，並向後累加，直到總和<=0(失去最大值可能)再找一新正數
                    {
                        nums[i] += nums[i - 1];
                    }
                }
                return nums.Max();
            }
        }
    }
}
