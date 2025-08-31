using System.Text;

public class Solution
{
    public string ConvertToTitle(int columnNumber)
    {
        StringBuilder result = new StringBuilder();

        while (columnNumber > 0)
        {
            columnNumber--;

            // 餘數0-25對應 'A' 到 'Z'
            int remainder = columnNumber % 26;

            // 將餘數轉換成字元，直接對 char 做數學運算，再轉型回來
            char ch = (char)('A' + remainder);

            // 將新字元插入到字串的最前面
            result.Insert(0, ch);

            // 5. 更新 columnNumber，準備計算更高一位
            columnNumber /= 26;
        }

        return result.ToString();
    }
}