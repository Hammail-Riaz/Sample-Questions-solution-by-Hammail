#Qno3. Write a Python program that prints the word PGC using stars (*). Use nested loops to draw each letter.  

def print_P(h):
    for r in range(1, h+1):
        for c in range(1, h+1):
            if r == 1 or c == 1 or r == (h//2) or (c == h and r <= (h // 2)):
                print('*', end='')
            else:
                print(' ', end='')
        print()
    print()
        
def print_G(h):
    for r in range(1, h + 1):
        for c in range(1, h + 1):
            if r == 1 or c == 1 or r == h or (c == h and r > (h // 2) + 1) or (r == (h // 2) + 1 and c > (h // 2) + 1):
                print('*', end='')
            else:
                print(' ', end='')
        print()
    print()
        
def print_C(h):
    for r in range(1, h + 1):
        for c in range(1, h + 1):
            if r == 1 or c == 1 or r == h:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    print()
        


print_P(10)
print_G(10)
print_C(10)