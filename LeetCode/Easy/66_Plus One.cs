using System;
using System.Collections.Generic;

using System.Text;
using System.Threading.Tasks;

namespace _66_Plus_One
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            int[] digits = {8,9,9,9};
            Console.WriteLine(solution.PlusOne(digits));
            Console.ReadLine();
        }
        public class Solution
        {
            public int[] PlusOne(int[] digits)
            {
                if (digits[digits.Length - 1] == 9)
                {
                    for (int i = digits.Length - 1; i >= 0; i--)
                    {

                        if (i == 0 && digits[i] == 9)
                        {
                            digits[i] = 1;
                            Array.Resize(ref digits, digits.Length + 1);
                        }
                        else if (digits[i] == 9)
                        {
                            digits[i] = 0;
                        }
                        else
                        {
                            digits[i] += 1;
                            break;
                        }
                    }
                }
                else
                {
                    digits[digits.Length - 1] += 1;
                }

                return digits;
            }
        }
    }
}
