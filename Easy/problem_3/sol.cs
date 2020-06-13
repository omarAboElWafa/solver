public static int Factorial(int num)
{
    int factorial = 1;
    for (int i = 1; i < num + 1; i++)
    {
        factorial *= i;
    }

    return factorial;
}