using System;
using System.Collections.Generic;
//using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _169_Majority_Element
{
    public class Solution
    {
        public int MajorityElement(int[] nums)
        {
            int length = nums.Length;
            Dictionary<int, int> count = new Dictionary<int, int>();

            foreach (var num in nums)
            {
                if (count.ContainsKey(num))
                {
                    count[num]++;
                }
                else
                    count[num] = 1;

                if (count[num] > length / 2)
                    return num;
            }
            return 0;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            int[] nums = new int[] { 3,2,3};

            int ans = solution.MajorityElement(nums);
        }
    }
}
