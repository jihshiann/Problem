using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _88_Merge_Sorted_Array
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            int[] nums1 = { 1, 2, 3, 0, 0, 0 };
            int[] nums2 = { 2, 5, 6 };
            solution.Merge(nums1, 3, nums2, 3);
            Console.WriteLine(nums1);
            Console.ReadLine();
        }

        public class Solution
        {
            public void Merge(int[] nums1, int m, int[] nums2, int n)
            {
                for (int i = 0; i < n; i++)
                {
                    nums1[m + i] = nums2[i];
                }

                if (nums1.Length <= 2)
                {
                    if (nums1.Length > 1 && nums1[1] < nums1[0])
                    {
                        Array.Reverse(nums1);
                        return;
                    }
                    return;
                }
                sort(nums1, 0, nums1.Length - 1);
                return;
            }
            #region quick sort
            public void sort(int[] array, int left, int right)
            {
                if (right <= left)
                {
                    return;
                }

                int temp = 0;
                int pivotIndex = (left + right) / 2;
                int pivot = array[pivotIndex];
                int swapIndex = left;
                array[pivotIndex] = array[right];
                array[right] = pivot;


                for (int i = left; i < right; i++)
                {
                    if (array[i] <= pivot)
                    {
                        temp = array[swapIndex];
                        array[swapIndex] = array[i];
                        array[i] = temp;
                        swapIndex++;
                    }
                }
                array[right] = array[swapIndex];
                array[swapIndex] = pivot;

                sort(array, left, swapIndex - 1);
                sort(array, swapIndex + 1, right);
            }
            #endregion
        }
    }
}
