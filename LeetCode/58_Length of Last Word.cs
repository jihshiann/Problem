using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Length_of_Last_Word
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            Console.WriteLine(solution.LengthOfLastWord("a"));
            Console.ReadLine();
        }

        public class Solution
        {
            public int LengthOfLastWord(string s)
            {
                int emptyIndex = 0;
                int emptyCount = 0;
                int notEmptyCount = 0;
                for (int i = 0; i < s.Length; i++)
                {
                    if (s[i] == ' ')
                    {
                        emptyIndex = i + 1;
                        emptyCount++;
                    }
                    else if (i > 0 && s[i - 1] == ' ')
                    {
                        notEmptyCount = 1;
                    }
                    else
                    {
                        notEmptyCount++;
                    }
                }
                if (s.Length - emptyCount == 1)
                {
                    return 0;
                }
                return notEmptyCount;
            }
        }
    }
}
