#Qno3. Write a Python program that prints the word PGC using stars (*). Use nested loops to draw each letter.  

# def print_P(h):
#     for r in range(1, h+1):
#         for c in range(1, h+1):
#             if r == 1 or c == 1 or r == (h//2) or (c == h and r <= (h // 2)):
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#         print()
#     print()
        
# def print_G(h):
#     for r in range(1, h + 1):
#         for c in range(1, h + 1):
#             if r == 1 or c == 1 or r == h or (c == h and r > (h // 2) + 1) or (r == (h // 2) + 1 and c > (h // 2) + 1):
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#         print()
#     print()
        
# def print_C(h):
#     for r in range(1, h + 1):
#         for c in range(1, h + 1):
#             if r == 1 or c == 1 or r == h:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#         print()
#     print()
        


# print_P(10)
# print_G(10)
# print_C(10)


# initialzing 3 list for each letter
# looping and if condition is true so add the * in the line of each letter
# at the end concatinating each corresponding element of list and joining them with the gap.
# hence the PGC will print on screen...



def print_PGC(h):
    P, G, C = [], [], []
    
    for row in range(1, h+1):
        line_of_P = ''
        line_of_G = ''
        line_of_C = ''
        
        for col in range(1, (h//2)+1):
            char_of_P = ' '
            char_of_G = ' '
            char_of_C = ' '
            
            # Condition for P alphabet
            if row == 1 or col == 1 or row == (h//2) or (c == (h//2) and row <= (h // 2)):
                char_of_P = '*'
                
            # Condition for G alphabet
            if row == 1 or col == 1 or row == h or (col == (h//2) and row > (h // 2) + 1) or (row == (h // 2)+1 and col> h//4):
                char_of_G = '*'
                
            # Condition for C alphabet
            if row == 1 or c == 1 or row == h:
                char_of_C = '*'
            
            line_of_P += char_of_P
            line_of_G += char_of_G
            line_of_C += char_of_C
            
        P.append(line_of_P)
        G.append(line_of_G)
        C.append(line_of_C)
            
    word = []
    gap = '\t'
    for p, g, c in zip(P, G, C):
        word.append(p + gap + g + gap + c)
        
    for line in word:
        print(line)
        
print_PGC(10)
