using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _70_Climbing_Stairs
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            Console.WriteLine(solution.ClimbStairs(6));
            Console.ReadLine();
        }

        public class Solution
        {
            public int ClimbStairs(int n)
            {
                if (n <= 3)
                    return n;
                int way = 3;
                int added = 1;
                int preAdded = 0;

                for (int j = 3; j < n; j++)
                {
                    preAdded = added - preAdded;
                    added = added + preAdded;
                    way += added;
                }

                return way;
            }
        }
    }
}
