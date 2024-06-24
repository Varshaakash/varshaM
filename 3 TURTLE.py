import turtle

# Create a screen object
screen = turtle.Screen()
screen.title("Turtle Graphics - Flower")

# Create a turtle object
t = turtle.Turtle()
t.speed(10)  # Set the drawing speed

# Function to draw a petal
def draw_petal():
    t.circle(100, 60)  # Draw the first half of the petal
    t.left(120)
    t.circle(100, 60)  # Draw the second half of the petal
    t.left(120)

# Function to draw a flower with a given number of petals
def draw_flower(petals):
    for _ in range(petals):
        draw_petal()
        t.right(360 / petals)

# Draw a flower with 6 petals
draw_flower(6)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
