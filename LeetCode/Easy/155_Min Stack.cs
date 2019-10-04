using System;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _155_Min_Stack
{
    class Program
    {
        static void Main(string[] args)
        {
            MinStack minStack = new MinStack();
            minStack.Push(-2);
            minStack.Push(0);
            minStack.Push(-3);
            minStack.GetMin(); 
          minStack.Pop();
            minStack.Top(); 
       minStack.GetMin(); 
        }
    }
    public class MinStack
    {

        /** initialize your data structure here. */
        private int min;
        private Stack stack;

        public MinStack()
        {
            min = Int32.MaxValue;
            stack = new Stack();
        }

        public void Push(int x)
        {
            if (x <= min)
            {
                if (stack.Count != 0)
                    stack.Push(min);//因MinStack沒有Count功能，每當刷新min時先Push一次原來的min
                min = x;
            }
            stack.Push(x); 
        }

        public void Pop()
        {
            if (stack.Count > 0)
            {
                if ((int)stack.Pop() == min && stack.Count > 1)
                    min = (int)stack.Pop();//每當最小值被Pop時將最小值一起還原，再Pop一次上次多Push的
            }

            if (stack.Count == 0)
                min = Int32.MaxValue;
        }

        public int Top()
        {
            return (int)stack.Peek();
        }

        public int GetMin()
        {
            return min;
        }
    }
}
