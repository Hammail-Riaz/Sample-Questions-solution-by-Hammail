# Qno8: Create a function that takes two numbers (start and end) and returns a list of all prime numbers between them.

# sol no 8:
def prime_in_range(x, y):
    """
    return a list containing prime number in the given range (x, y)
    """
    prime_numbers = []
    for number in range(x, y+1):
        if number > 1: # prime number always start from 2
            is_prime = True
            for count in range(2, int(number**0.5)+1):
                if number % count == 0: #checking each possible factor of the current iteration number
                    is_prime = False
                    break
                
            if is_prime:
                prime_numbers.append(number) #adding the prime number in list
            
    return prime_numbers
        

for num in prime_in_range(1, 50):
    print(num)
    
