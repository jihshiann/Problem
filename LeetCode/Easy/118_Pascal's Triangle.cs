using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _118_Pascal_s_Triangle
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            solution.Generate(5);
        }

        public class Solution
        {
            public IList<IList<int>> Generate(int numRows)
            {
                List<IList<int>> triangle = new List<IList<int>>();

                for (int row = 1; row <= numRows; row++)
                {
                    List<int> line = new List<int>();
                    triangle.Add(line);

                    for (int index = 0; index < row; index++)
                    {
                        if (index == 0 || index == row - 1)
                        {
                            line.Add(1);
                        }
                        else
                        {
                            line.Add(triangle[row - 2][index] + triangle[row - 2][index - 1]);
                        }
                    }
                }

                return triangle;
            }
        }
    }
}
