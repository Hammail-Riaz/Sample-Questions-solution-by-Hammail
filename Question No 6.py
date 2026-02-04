#Qno6. Write a Python program that asks the user to enter a height value and prints a hollow diamond shape made of stars (*). 

# Sol no 6:
height = int(input("Enter Height to print Hollow Diamond: "))

for row in range((height // 2)+1):
    for spaces in range((height//2), row, -1):
        print(' ', end='')
    
    for star in range(2*row+1):
        if star == 0 or star ==  row*2:
            print('X', end='')
        else:
            print(' ', end='')
    print()
    
for row in range((height // 2)):
    for spaces in range(row+1):
        print(' ', end='')
    
    for star in range((height//2)*2-1 , 2*row, -1):
        if star ==  (height//2)*2-1 or star == 2*row+1:
            print('X', end='')
        else:
            print(' ', end='')
        
    print()
        
    
    