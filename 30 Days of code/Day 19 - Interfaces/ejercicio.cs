// >>> Day 19: Interfaces
// >>> https://www.hackerrank.com/challenges/30-interfaces/problem

using System;

public interface AdvancedArithmetic{
    int divisorSum(int n);
}

public class Calculator : AdvancedArithmetic
{
    public int divisorSum(int n)
    {
        int retorno = 0;
        for (int i = 1; i <= n; i++)
        {
            if(n % i == 0)
            {
                retorno += i;
            }
        }
        return retorno;
    }
}
class Solution{
    static void Main(string[] args){
        int n = Int32.Parse(Console.ReadLine());
      	AdvancedArithmetic myCalculator = new Calculator();
        int sum = myCalculator.divisorSum(n);
        Console.WriteLine("I implemented: AdvancedArithmetic\n" + sum); 
    }
}