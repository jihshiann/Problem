public class Solution {
    public bool IsPalindrome(int x) {
        string rev="";
        int temp = x;
        if (x==0)
            return true;
        else if (x<0)
            return false;
       // if (x==int.MinValue)
         //   return false;
        
        while (x!=0)
        {
            rev += x%10;
            x/=10;
        }
        
        int ans =0;
        if(! int.TryParse(rev, out ans) )
            return false;  
        else if(temp != ans )
            return false;
        else 
            return true;
    }
}