using System;

class Program
{
    static void Main()
    {
        PrintEven(100);
        PrintOdd(100);
    }

    public void PrintEven(int n)
    {
        for (int i = 0; i < n; i++)
        {
            if (i % 2 == 0)
            {
                Console.WriteLine(i);
            }
        }
    }

    public void PrintOdd(int n)
    {
        for (int i = 0; i < n; i++)
        {
            if (i % 2 == 1)
            {
                Console.WriteLine(i);
            }
        }
    }
}
