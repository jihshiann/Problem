using System;

// 定義解題的類別
public class Solution
{
    // C# 的方法簽名需要指定參數型別和回傳型別
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

// 主程式，用於測試
public class Program
{
    public static void Main(string[] args)
    {
        Solution sol = new Solution();

        Console.WriteLine($"A 的欄位編號是: {sol.TitleToNumber("A")}");      // 輸出: 1
        Console.WriteLine($"Z 的欄位編號是: {sol.TitleToNumber("Z")}");      // 輸出: 26
        Console.WriteLine($"AA 的欄位編號是: {sol.TitleToNumber("AA")}");     // 輸出: 27
        Console.WriteLine($"AB 的欄位編號是: {sol.TitleToNumber("AB")}");     // 輸出: 28
        Console.WriteLine($"ZY 的欄位編號是: {sol.TitleToNumber("ZY")}");     // 輸出: 701
        Console.WriteLine($"FXSHRXW 的欄位編號是: {sol.TitleToNumber("FXSHRXW")}"); // 輸出: 2147483647
    }
}