'''
Author: Ashish Namdev
Date: 28 Mar 2022

Probelm URL: https://codingbat.com/prob/p173401

The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''

def sleep_in(weekday, vacation):
  """
  Return True if we sleep in
  
  Parameters:
    arg1 (bool): parameter weekday is True if it is a weekday
    arg2 (bool): parameter vacation is True if are on vacation
  
    Returns:
    bool: True if we sleep in
  """
  return True if not weekday or vacation else False
