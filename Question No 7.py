#Qno7: Write a Python program that takes a list of numbers from the user and finds the second largest number in the list.

# sol no 7

# initialization
numbers = []

number = int(input('Enter a number, press [button] to add another in list, or Enter "0" [Zero] to end list: '))
numbers.append(number)
while number != 0:
    number = int(input('Next number or Enter "0" [Zero] to end list: '))
    numbers.append(number)

# sorting the list in increasing order then we will get the 2nd last element for the 2nd largest number in our list
numbers.sort()

print(numbers)
print(numbers[-2]) # 2nd Maximum number is at 2nd last postion after sorting in increasing order
