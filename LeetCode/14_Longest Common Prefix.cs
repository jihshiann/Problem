public class Solution {
    public int RomanToInt(string s) {
        int M=1000, D= 500, C=100,L=50, X=10, V=5, I=1;
        char[] Ans=s.ToCharArray();
        int [] num=new int[s.Length+2];
        int sum=0;
    
        for(int i=0; i<s.Length; i++)
        {
            switch (Ans[i])
            {
                        case 'M':
                            num[i+1] = 1000;
                            break;
                        case 'D':
                            num[i+1] = 500;
                            break;
                        case 'C':
                            num[i+1] = 100;
                            break;
                        case 'L':
                            num[i+1] = 50;
                            break;
                        case 'X':
                            num[i+1] = 10;
                            break;
                        case 'V':
                            num[i+1] = 5;
                            break;
                        case 'I':
                            num[i+1] = 1;
                            break;
            }
        }
        for (int j=1; j<=s.Length; j++)
        {   
            if(num[j]>num[j-1] && num[j]>=num[j+1])
                 { sum += num[j];}
            else if(num[j]<=num[j-1] && num[j]>=num[j+1])
                {sum +=num[j];}
            else
                sum -=num[j];
        }
       
       
       return sum;
    }
}