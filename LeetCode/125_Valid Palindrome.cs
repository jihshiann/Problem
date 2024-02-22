using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _125_Valid_Palindrome
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            string s = "A man, a plan, a canal: Panama";
            solution.IsPalindrome(s);
        }
    }

    public class Solution
    {
        public bool IsPalindrome(string s)
        {
            s = s.ToUpper();
            for (int l = 0, r = s.Length-1; l<r;)
            {
                if (!char.IsLetterOrDigit(s[l])) l++;
                else if (!char.IsLetterOrDigit(s[r])) r--;
                else if (s[l++] != s[r--]) return false;
            }
            return true;
        }
    }
}
