'''
Author: Ashish Namdev
Date: 29 Mar 2022
Probelm URL: https://codingbat.com/prob/p141905

Given two int values, return their sum.
Unless the two values are the same, then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''

def sum_double(a, b):
  """
  Return sum of a and b, if both values are same then
  return double their sum.
  
  Parameters:
    a (int): integer value
    b (int): integer value
  
    Returns:
    int: sum or double sum of a and b
  """
  return (a + b) * 2 if a == b else (a + b)
