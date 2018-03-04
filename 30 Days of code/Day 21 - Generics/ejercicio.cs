// >>> Day 21: Generics
// >>> https://www.hackerrank.com/challenges/30-generics/problem

using System;

class Printer
{
    static T PrintArray<T>(T array)
    {
        foreach (T item in array)
        {
            Console.Writeline(item);
        }
    }

    
    static void Main(string[] args)
	{
		int n = Convert.ToInt32(Console.ReadLine());
		int[] intArray = new int[n];
		for (int i = 0; i < n; i++)
		{
			intArray[i] = Convert.ToInt32(Console.ReadLine());
		}
		
		n = Convert.ToInt32(Console.ReadLine());
		string[] stringArray = new string[n];
		for (int i = 0; i < n; i++)
		{
			stringArray[i] = Console.ReadLine();
		}
		
		PrintArray<Int32>(intArray);
		PrintArray<String>(stringArray);
	}
}