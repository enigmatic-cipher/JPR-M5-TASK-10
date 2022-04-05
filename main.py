"""
Given n and x as input, print the sum of 1^n + 2^n + 3^n+....+ x^n.
Input-> n=2, x= 5
Output-> 55
"""

def power_of_n(x,n):
  sum = 0
  for i in range(1,x+1):
    sum = sum + i**n
  print(sum)

n = 2
x = 5
power_of_n(x,n)