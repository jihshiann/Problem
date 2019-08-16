using System;
using System.Collections.Generic;
using System.Linq;

namespace Count_and_Say
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            Console.WriteLine(solution.CountAndSay(1));
            Console.ReadLine();
        }

        public class Solution
        {
            public string CountAndSay(int n)
            {
                string response = "1";
                List<char> element = response.ToList();
                List<char> countAndSay = response.ToList();
                for (int i = 1; i < n; i++)
                {
                    char stored = element[0];
                    int count = 0;
                    int repeat = element.Count;
                    countAndSay.Clear();
                    for (int j = 0; j < repeat; j++)
                    {
                        if (stored == element[j])
                        {
                            count++;
                        }
                        else if (stored != element[j])
                        {
                            countAndSay.Add(char.Parse(count.ToString()));
                            countAndSay.Add(stored);
                            stored = element[j];
                            count = 1;
                        }
                    }
                    countAndSay.Add(char.Parse(count.ToString()));
                    countAndSay.Add(stored);
                    element.Clear();
                    element.AddRange(countAndSay);
                }
                element.Clear();
                response = string.Join("", countAndSay);
                countAndSay.Clear();
                return response;
            }
        }
    }
}
