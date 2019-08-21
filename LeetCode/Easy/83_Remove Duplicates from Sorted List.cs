using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Remove_Duplicates_from_Sorted_List
{
    class Program
    {
        static void Main(string[] args)
        {
            ListNode listNode1 = new ListNode(1) { next = new ListNode(1) { next = new ListNode(2) { next = new ListNode(3) { next = new ListNode(3) } } } };//1->1->2->3->3
            Solution solution = new Solution();
            solution.DeleteDuplicates(listNode1);
        }


        //* Definition for singly-linked list.
        public class ListNode
        {
            public int val;
            public ListNode next;
            public ListNode(int x) { val = x; }
        }

        public class Solution
        {
            public ListNode DeleteDuplicates(ListNode head)
            {
                if (head == null || head.next == null)
                {
                    return head;
                }
                else if (head.val == head.next.val)
                {
                    head.next = head.next.next;
                    head = DeleteDuplicates(head);
                    return head;
                }
                else
                {
                    head.next = DeleteDuplicates(head.next);
                    return head;
                }
                
            }
        }
    }
}
