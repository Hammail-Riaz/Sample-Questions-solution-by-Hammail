        
# Qno5: Write a Python program that checks whether a number entered by the user is a palindrome or not.
# (A palindrome number reads the same backward as forward, such as 121 or 4554.)

# sol no 5
number = input("Enter a number [to check palindrome]: ")

def check_palindrome(number):
    """get the number as argument and return True if the number is palindrome otherwise return False"""
    number = str(number)
    reversed_number = number[::-1] # using string slicing to reverse the number string
    if number == reversed_number:
        return True
    return False

is_palindrome = check_palindrome(number)

if is_palindrome:
    print(f"Yes, the number : {number} is a Palindrome")
else:
    print(f"NO, the number : {number} is not a Palindrome")
    
