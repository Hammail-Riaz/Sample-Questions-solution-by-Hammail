# print the name of in increasing order in each line
name = 'MUHAMMAD_ATIF'
for i in range(len(name)+1):
    print(name[:i])
    
# Prints the tirangle of name
name = 'MUHAMMAD_ATIF'
for i in range(len(name)+1):
    print(' '*((len(name) - i) // 2),end='')    
    print(name[:i])

# prints the pascal triangle 
from math import factorial
def combination(n, r):
    return ((factorial(n)) / (factorial(r) * factorial(n-r)))

for n in range(10):
    print(' '*(10-n), end='')
    for r in range(n+1):
        print(f" {int(combination(n, r))} ", end='')
    print()