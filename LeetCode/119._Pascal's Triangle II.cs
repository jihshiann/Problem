using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _119._Pascal_s_Triangle_II
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            solution.GetRow(3);
            solution.GetLine(3);
        }

        public class Solution
        {
            public IList<int> GetRow(int rowIndex)
            {
                var result = new List<int>() { 1 };
                for (int i = 0; i < rowIndex; i++)
                {
                    var arr = new List<int>() { 1 };
                    arr.AddRange(result.Zip(result.Skip(1), (a, b) => a + b));
                    //a = this = result(List<int>)
                    //b = result.Skip(1)(List<int>)
                    //(a, b) = math.min(a.count, b.count)
                    //=> a + b = new Lisy<int> {foreach (a[0~math.min] + b[0~math.min])}

                    //if 想看委派中斷點
                    //{
                    //    return a + b;
                    //}));
                    arr.Add(1);
                    result = arr;
                }
                //首尾項為1
                //result = result + result[1~last] + Add(1)
                return result;
            }

            public IList<int> GetLine(int rowIndex)
            {
                int[] result = new int[rowIndex + 1];
                result[0] = 1;

                // bottom up dynamic programming, iterate up from row 1
                for (int row = 1; row < rowIndex + 1; row++)
                {
                    // iterate over columns working from right to left
                    // also stopping before last column, this will always remain 1
                    // Note: you could iterate columns left to right but that would require use of temp int variable
                    for (int column = rowIndex - 1; column > 0; column--)
                    {
                        result[column] = result[column] + result[column - 1];
                        //1,0,0,0
                        //1,1,0,0
                        //1,2,1,0
                        //1,3,3,1
                        //1,4,6,4
                        //this = this + this[-1]
                    }

                    // set right edge to 1
                    result[rowIndex] = 1;
                }

                return new List<int>(result);
            }
        }
    }
}
