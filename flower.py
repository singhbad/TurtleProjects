import turtle

def draw_petal(t, radius, angle):
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

def draw_flower(t, x, y, petal_count, petal_color, center_color, petal_radius, petal_angle):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(petal_color)

    # Draw the petals
    for _ in range(petal_count):
        draw_petal(t, petal_radius, petal_angle)
        t.left(360 / petal_count)

    # Draw the center of the flower
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(center_color)
    t.begin_fill()
    t.circle(petal_radius / 5)
    t.end_fill()

def create_flower_garden():
    window = turtle.Screen()
    window.bgcolor("white")

    # Create a turtle
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(10)

    # Draw multiple flowers with different styles
    draw_flower(t, -200, 0, 6, "red", "yellow", 60, 60)      # Red flower with 6 petals
    draw_flower(t, 0, 0, 8, "blue", "orange", 80, 45)       # Blue flower with 8 petals
    draw_flower(t, 200, 0, 12, "purple", "white", 40, 30)   # Purple flower with 12 petals
    draw_flower(t, -100, -200, 10, "pink", "lightgreen", 70, 50) # Pink flower with 10 petals
    draw_flower(t, 100, -200, 7, "orange", "cyan", 50, 70)  # Orange flower with 7 petals

    # Hide the turtle and display the window
    t.hideturtle()
    window.exitonclick()

# Run the function to create the flower garden
create_flower_garden()
