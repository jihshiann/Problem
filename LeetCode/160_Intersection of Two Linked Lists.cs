using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _160_Intersection_of_Two_Linked_Lists
{
    class Program
    {
        public class ListNode
        {
            public int val;
            public ListNode next;
            public ListNode(int x) { val = x; }
        }
        public class Solution
        {
            public ListNode GetIntersectionNode(ListNode headA, ListNode headB)
            {
                ListNode currA = headA;
                ListNode currB = headB;
                //比對項目為ListNode，故令其為key
                Dictionary<ListNode, int> node = new Dictionary<ListNode, int>();

                while (currA != null)
                {
                    node.Add(currA, currA.val);
                    currA = currA.next;
                }

                while (currB != null)
                {
                    if (node.ContainsKey(currB))
                        return currB;

                    currB = currB.next;
                }
                return null;
            }
        }
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            ListNode same = new ListNode(0);
            ListNode headA = new ListNode(2)
            {
                next = new ListNode(4)
                {
                    next = new ListNode(6)
                    {
                        next = new ListNode(8)
                        {
                            next = same
                        }
                    }
                }
            };
            ListNode headB = new ListNode(1)
            {
                next = new ListNode(3)
                {
                    next = new ListNode(5)
                    {
                        next = new ListNode(7)
                        {
                            next = new ListNode(9)
                            {
                                next = same
                            }
                        }
                    }
                }
            };
            bool ans = solution.GetIntersectionNode(headA, headB) == same;
        }
    }
}
