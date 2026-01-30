    
# Qno11: Write a turtle graphics program to draw a traffic signal with three circles colored red, yellow, and green
    
# sol no 11:
import turtle as t
def draw_circle(x, y, color, radius):
    """it can be used to draw circle with custom colors , radius and can we place at any cordinate you want"""
    t.color(color)
    t.begin_fill()
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(radius)
    t.end_fill()

# Drawing the base-Rectangular Shape of traffic light
t.begin_fill()
for count in range(4):
    if count%2 == 0:
        t.forward(150)
    else:
        t.forward(400)
        
    t.left(90)
t.end_fill()

# Drawing the circles
draw_circle(75,250,  "red", 50)
draw_circle(75,150, "yellow", 50)
draw_circle(75, 50, "green", 50)

    
t.done()

