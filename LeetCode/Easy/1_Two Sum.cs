public class Solution {
    public int[] TwoSum(int[] nums, int target)
    {
        int[] answer = null;
        for (int i=0; i<nums.Length-1; i++)
        {
            for (int j=i+1; j<nums.Length; j++)
            {
                if(target == nums[i]+nums[j])
                {
                    answer = new int[2]{i, j};
                    return answer;
                }
            }     
        }
        return answer;
    }
}