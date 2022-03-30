'''
Author: Ashish Namdev
Date: 30 Mar 2022

Probelm URL: https://codingbat.com/prob/p197466

Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.


diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
'''

def diff21(n):
  """
  Returns the absolute difference between n and 21
  
  Parameters:
    n (int): integer value
  
  Returns:
    int: difference between n and 21
  """
  return (21 - n) if n <= 21 else (n - 21) * 2  
