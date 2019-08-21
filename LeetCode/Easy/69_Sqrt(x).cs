using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _69_Sqrt_x_
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            int x = 9;
            Console.Write(solution.MySqrt(x));
            Console.ReadLine();
        }

        public class Solution
        {
            public int MySqrt(int x)
            {
                if (x <= 1)
                    return x;
                
                int left = x / 2;
                int right = x / left;

                while (left > right)
                {
                    left /= 2;
                    right = x / left;
                }
                left = (right + left) / 2;
                while (right > left)
                {
                    right = (right + left) / 2;
                    left = x / right;
                }

                return right;
            }
        }
    }
}
