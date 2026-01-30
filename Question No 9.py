                
# Qno9: Write a recursive function to calculate the sum of all numbers from 1 to n.
# sol no 9:
def sum(n):
    """find the sum of number from 1 to n by using the recursive logic"""
    result = 0
    if n==1:
        return 1
    else:
        return n + sum(n-1)
        
print(sum(10))
