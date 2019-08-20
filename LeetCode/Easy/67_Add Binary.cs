using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Add_Binary
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            Console.WriteLine(solution.AddBinary("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101", "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"));
            Console.ReadLine();
        }

        public class Solution
        {
            public string AddBinary(string a, string b)
            {
                List<char> aList = a.ToCharArray().ToList();
                List<char> bList = b.ToCharArray().ToList();
                if (a.Length > b.Length)
                {
                    for (int i = 0; i < a.Length - b.Length; i++)
                    {
                        bList = bList.Prepend('0').ToList();
                    }
                }
                else if (b.Length > a.Length)
                {
                    for (int i = 0; i < b.Length - a.Length; i++)
                    {
                        aList = aList.Prepend('0').ToList();
                    }
                }

                List<int> sumList = new List<int>(new int[aList.Count]);

                for (int i = aList.Count - 1; i >= 0; i--)
                {
                    sumList[i] += int.Parse(aList[i].ToString()) + int.Parse(bList[i].ToString());
                    if (i > 0 && sumList[i] >= 2)
                    {
                        sumList[i] -= 2;
                        sumList[i - 1] += 1;
                    }
                    else if (i == 0 && sumList[0] >= 2)
                    {
                        sumList[0] -= 2;
                        sumList = sumList.Prepend(1).ToList();
                    }
                }
                string sumStr = string.Join("", sumList);

                return sumStr;
            }
        }
    }
}
