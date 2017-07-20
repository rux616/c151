/*************************************************************
C151 Multi-user operating systems.
Dan Cassidy
January 20, 2004.

This program computes the solution for the equation ax+b = 0.

It contains some compiling errors and is badly indented for the
purposes of the homework. This comment also contain spelling errors
for the purpose of the homework.
**************************************************************/

#include <iostream>
using namespace std;

int main()
{
  float a, b, x;
  // Input a.
  cout << "Enter a number a:" << endl;
  cin >> a;  
  // Input b
  cout << "Enter a number b:" << endl;
  cin >> b;
  // Compute x
  if (a == 0)
    if (b == 0)
      cout << "The equation has an infinity of solutions." << endl;
    else
      cout << "The equation has no solution." << endl;
  else{
    x = -b/a;
    cout << "The solution for the equation ax+b = 0 is "
	 << x << endl;
  }
  if (a == 0)
    if (b == 0)
      cout << "The equation has an infinity of solutions." << endl;
    else
      cout << "The equation has no solution." << endl;
  else{
    x = -a/b;
    cout << "The solution for the equation ax+b = 0 is "
	 << x << endl;
  }
  return 0;
}
