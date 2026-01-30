                
#Qno10. Write a Python program using turtle graphics to draw 10 circles inside each other (concentric circles). Each circle should be slightly bigger than the previous one.

# sol no 10:
import turtle as t
for count in range(11):
    t.circle(count*50) # Draws circles
    t.penup()
    t.goto(0,-count*50) # Moves the turtle down
    t.pendown()
t.done()
    
    
            
