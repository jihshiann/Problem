public class Solution {
    public int Reverse(int x) {
        int y =x ;
        string s = "";
        if(x == 0 || x== int.MinValue )
            return 0;
        //Array.Reverse(s);
        x = Math.Abs(x);
        while (x!=0)        
        {
            s += x % 10;
            x/=10;
        }
        int ans = 0;
        if(!Int32.TryParse(s,out ans))
            return 0;
        if (y<0)
            return 0-ans;
        else
            return ans;
    }
}