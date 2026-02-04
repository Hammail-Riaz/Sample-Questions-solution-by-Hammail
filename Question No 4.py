# 4.  Write a Python program that prints a pyramid pattern of numbers like this:
"""
        1  
      2 3 2  
    3 4 5 4 3  
  4 5 6 7 6 5 4  
5 6 7 8 9 8 7 6 5  
"""

for row in range(1, 6):
  for spaces in range(5, row-1,-1):
    print(' ', end='')
  
  for left_half in range(row , row*2):
    print(left_half, end='')
    
  for right_half in range(left_half-1, row-1, -1):
    print(right_half, end='')
  
  print()