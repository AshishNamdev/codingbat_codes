'''
Author: Ashish Namdev
Date: 29 Mar 2022

Probelm URL: https://codingbat.com/prob/p120546

We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
We are in trouble if they are both smiling or if neither of them is smiling.
Return True if we are in trouble.

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
'''

def monkey_trouble(a_smile, b_smile):
  """
  Return True if we are in trouble.
  
  Parameters:
    a_smile (bool): parameter a_smile is True if moneky a is smiling
    b_smile (bool): parameter b_smile is True if moneky a is smiling
  
    Returns:
    bool: True if we are in trouble
  """
  return True if (a_smile and b_smile) or (not a_smile and not b_smile) else False
