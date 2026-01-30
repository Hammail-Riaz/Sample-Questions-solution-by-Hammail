#Qno1: Write a python program that takes a word from the user and prints the word in reverse order.
#Example: Input: apple output: elppa

# Sol : ans 1

word = input("Enter a word [to get reverse order]: ")
reversed_word = word[::-1]  # Using string slicing to reverse the word
print(reversed_word)
