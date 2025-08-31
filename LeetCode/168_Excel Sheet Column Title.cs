using System.Text;

public class Solution
{
    public string ConvertToTitle(int columnNumber)
    {
        StringBuilder result = new StringBuilder();

        while (columnNumber > 0)
        {
            columnNumber--;

            // �l��0-25���� 'A' �� 'Z'
            int remainder = columnNumber % 26;

            // �N�l���ഫ���r���A������ char ���ƾǹB��A�A�૬�^��
            char ch = (char)('A' + remainder);

            // �N�s�r�����J��r�ꪺ�̫e��
            result.Insert(0, ch);

            // 5. ��s columnNumber�A�ǳƭp��󰪤@��
            columnNumber /= 26;
        }

        return result.ToString();
    }
}