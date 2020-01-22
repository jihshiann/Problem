using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

namespace Titansoft_Programming
{
    //GetMiddleCharacters
    class Result1
    {
        /*
         * Complete the 'GetMiddleCharacters' function below.
         *
         * The function is expected to return a STRING.
         * The function accepts STRING inputStr as parameter.
         */
        public static string GetMiddleCharacters(string inputStr)
        {
            int mid = inputStr.Length / 2;
            int remainder = inputStr.Length % 2;
            string ans = string.Empty;
            if (remainder == 0)
            {
                ans = inputStr[mid - 1].ToString() + inputStr[mid].ToString();
            }
            else
            {
                ans = inputStr[mid].ToString();
            }
            return ans;
        }
    }
    //Find the Winner
    class Result2
    {
        /*
         * Complete the 'winner' function below.
         *
         * The function is expected to return a STRING.
         * The function accepts following parameters:
         *  1. INTEGER_ARRAY andrea
         *  2. INTEGER_ARRAY maria
         *  3. STRING s
         */
        public static string winner(List<int> andrea, List<int> maria, string s)
        {
            int begin, APiont = 0, MPiont = 0;
            string ans = string.Empty;
            if (s == "Even")
            {
                begin = 0;
            }
            else
            {
                begin = 1;
            }
            for (int j = begin; j < andrea.Count(); j += 2)
            {
                APiont += andrea[j] - maria[j];
                MPiont += maria[j] - andrea[j];
            }
            if (APiont - MPiont > 0)
            {
                ans = "Andrea";
            }
            else if (APiont - MPiont < 0)
            {
                ans = "Maria";
            }
            else
                ans = "Tie";

            return ans;
        }

    }
    //missingWords
    class Result3
    {
        /*
         * Complete the 'missingWords' function below.
         *
         * The function is expected to return a STRING_ARRAY.
         * The function accepts following parameters:
         *  1. STRING s
         *  2. STRING t
         */
        public static List<string> missingWords(string s, string t)
        {
            List<string> sList = s.Split(' ').ToList();
            List<string> tList = t.Split(' ').ToList();
            List<string> ans = new List<string>();
            foreach (string tStr in tList)
            {
                if (sList.Contains(tStr))
                {
                    int count = sList.FindIndex(str => str == tStr);
                    ans.AddRange(sList.GetRange(0, count));
                    sList.RemoveRange(0, count + 1);
                }
            }
            ans.AddRange(sList);
            return ans;
        }
    }
    //getMostVisited
    class Result
    {
        /*
         * Complete the 'getMostVisited' function below.
         *
         * The function is expected to return an INTEGER.
         * The function accepts following parameters:
         *  1. INTEGER n
         *  2. INTEGER_ARRAY sprints
         */
        public static int getMostVisited(int n, List<int> sprints)
        {
            Dictionary<int, int> count = new Dictionary<int, int>();
            for (int i = 1; i < sprints.Count; i++)
            {
                int length = sprints[i] - sprints[i - 1];
                if (length > 0)
                {
                    for (int j = 0; j <= length; j++)
                    {
                        if (!count.ContainsKey(sprints[i - 1] + j))
                        {
                            count.Add(sprints[i - 1] + j, 1);
                        }
                        else
                        {
                            count[sprints[i - 1] + j]++;
                        }
                    }
                }
                else
                {
                    for (int j = 0; j >= length; j--)
                    {
                        if (!count.ContainsKey(sprints[i - 1] + j))
                        {
                            count.Add(sprints[i - 1] + j, 1);
                        }
                        else
                        {
                            count[sprints[i - 1] + j]++;
                        }
                    }
                }
            }
            return count.FirstOrDefault(x => x.Value == count.Values.Max()).Key;
        }

    }
    class Solution
    {
        public static void Main(string[] args)
        {
            #region GetMiddleCharacters
            //string inputStr = Console.ReadLine();
            //string result1 = Result1.GetMiddleCharacters(inputStr);
            #endregion
            #region Find the Winner
            //int andreaCount = Convert.ToInt32(Console.ReadLine().Trim());

            //List<int> andrea = new List<int>();

            //for (int i = 0; i < andreaCount; i++)
            //{
            //    int andreaItem = Convert.ToInt32(Console.ReadLine().Trim());
            //    andrea.Add(andreaItem);
            //}

            //int mariaCount = Convert.ToInt32(Console.ReadLine().Trim());

            //List<int> maria = new List<int>();

            //for (int i = 0; i < mariaCount; i++)
            //{
            //    int mariaItem = Convert.ToInt32(Console.ReadLine().Trim());
            //    maria.Add(mariaItem);
            //}

            //string s = Console.ReadLine();

            //string result = Result2.winner(andrea, maria, s);
            #endregion
            #region missingWords
            //string s = Console.ReadLine();

            //string t = Console.ReadLine();

            //List<string> result = Result3.missingWords(s, t);
            #endregion
            #region
            int n = Convert.ToInt32(Console.ReadLine().Trim());

            int sprintsCount = Convert.ToInt32(Console.ReadLine().Trim());

            List<int> sprints = new List<int>();

            for (int i = 0; i < sprintsCount; i++)
            {
                int sprintsItem = Convert.ToInt32(Console.ReadLine().Trim());
                sprints.Add(sprintsItem);
            }

            int result = Result.getMostVisited(n, sprints);
            #endregion
        }
    }
}
