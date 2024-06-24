import turtle

# Create a screen object
screen = turtle.Screen()
screen.title("Turtle Graphics")

# Create a turtle object
t = turtle.Turtle()

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Draw a square of size 100
draw_square(100)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
