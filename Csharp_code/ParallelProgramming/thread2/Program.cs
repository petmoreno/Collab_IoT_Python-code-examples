using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace thread2
{
    class Program
    {
        static void Main(string[] args)
        {
            Test t1 = new Test(1);
            Test t2 = new Test(2);
            Test t3 = new Test(3);
            Test t4 = new Test(4);

            Thread thread1 = new Thread(t1.Print);
            Thread thread2 = new Thread(t2.Print);
            Thread thread3 = new Thread(t3.Print);
            Thread thread4 = new Thread(t4.Print);

            Console.WriteLine("Main: set the priorities");

            thread1.Priority = ThreadPriority.Lowest;
            thread2.Priority = ThreadPriority.Lowest;
            thread3.Priority = ThreadPriority.Lowest;
            thread4.Priority = ThreadPriority.Highest;

            Console.WriteLine("Main: start threads");

            thread1.Start();
            thread2.Start();
            thread3.Start();
            thread4.Start();

            Console.WriteLine("Main ready");

            Console.ReadKey();
        }
    }

    public class Test
    {
        int a;

        public Test(int j)
        {
            a = j;
        }

        public void Print()
        {
            for (int i=0; i < 100; i++)
            {
                Console.Write(a);
            }
        }
    }

}
