using System;

// �w�q���D�����O
public class Solution
{
    // C# ����kñ�W�ݭn���w�Ѽƫ��O�M�^�ǫ��O
    public int TitleToNumber(string columnTitle)
    {
        int result = 0;

        foreach (char c in columnTitle)
        {
            int value = c - 'A' + 1;

            result = result * 26 + value;
        }

        return result;
    }
}

// �D�{���A�Ω����
public class Program
{
    public static void Main(string[] args)
    {
        Solution sol = new Solution();

        Console.WriteLine($"A �����s���O: {sol.TitleToNumber("A")}");      // ��X: 1
        Console.WriteLine($"Z �����s���O: {sol.TitleToNumber("Z")}");      // ��X: 26
        Console.WriteLine($"AA �����s���O: {sol.TitleToNumber("AA")}");     // ��X: 27
        Console.WriteLine($"AB �����s���O: {sol.TitleToNumber("AB")}");     // ��X: 28
        Console.WriteLine($"ZY �����s���O: {sol.TitleToNumber("ZY")}");     // ��X: 701
        Console.WriteLine($"FXSHRXW �����s���O: {sol.TitleToNumber("FXSHRXW")}"); // ��X: 2147483647
    }
}