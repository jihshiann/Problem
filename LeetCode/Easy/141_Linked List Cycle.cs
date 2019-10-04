using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _141_Linked_List_Cycle
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();
            ListNode head = new ListNode(3)
            {
                next = new ListNode(2)
                {
                    next = new ListNode(0)
                    {
                        next = new ListNode(3)
                        {
                            next = new ListNode(1)
                            {
                                next = new ListNode(0)
                                {
                                    next = new ListNode(3)

                                }
                            }
                        }
                    }

                }
            };
            solution.HasCycle(head);
        }
    }

    //Definition for singly-linked list.
    public class ListNode
    {
        public int val;
        public ListNode next;
        public ListNode(int x)
        {
            val = x;
            next = null;
        }
    }

    public class Solution
    {
        public bool HasCycle(ListNode head)
        {
            if (head == null || head.next == null) return false;
            ListNode each = head;
            ListNode everyTwo = head.next;

            while (everyTwo != null && each != everyTwo)//以2倍數尋訪，直到同物件或是到底
            {
                each = each.next;
                everyTwo = everyTwo.next;
                if (everyTwo == null) return false;
                everyTwo = everyTwo.next;
            }

            if (each == everyTwo) return true;
            return false;
        }
    }
}
