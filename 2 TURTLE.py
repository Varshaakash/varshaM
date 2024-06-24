import turtle

# Create a screen object
screen = turtle.Screen()
screen.title("Turtle Graphics - Spiral")

# Create a turtle object
t = turtle.Turtle()
t.speed(10)  # Increase the drawing speed

# Function to draw a spiral
def draw_spiral():
    for i in range(100):
        t.forward(i * 10)
        t.right(144)  # Angle for a star-like spiral

# Draw the spiral
draw_spiral()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
