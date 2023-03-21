%module example

%{
#include "example.h"
%}

%include "std_string.i"
using namespace std;
int add(int x, int y);
double multiply(double x, double y);
float subtract(float x, float y);
string concatenate(string str1, string str2);
