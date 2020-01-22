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

namespace FizzBuzz
{
    class Result
    {
        /*
         * Complete the 'fizzBuzz' function below.
         *
         * The function accepts INTEGER n as parameter.
         */
        public static void fizzBuzz(int n)
        {
            if (n > 0 && n < 2 * (long)Math.Pow(10, 5))
            {
                for (int i = 1; i <= n; i++)
                {
                    switch (i % 3)
                    {
                        case 0:
                            if (i % 5 == 0)
                                Console.WriteLine("FizzBuzz");
                            else
                                Console.WriteLine("Fizz");
                            break;
                        default:
                            if (i % 5 == 0)
                                Console.WriteLine("Buzz");
                            else
                                Console.WriteLine(i.ToString());
                            break;

                    }
                }
            }
        }

    }
    class Program
    {
        static void Main(string[] args)
        {
            int n = Convert.ToInt32(Console.ReadLine().Trim());

            Result.fizzBuzz(n);
            Console.ReadLine();
        }
    }
}
