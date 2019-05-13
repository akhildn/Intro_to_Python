import turtle


def draw_square(cursor):
    for i in range(4):
        cursor.forward(100)
        cursor.right(90)


def draw_circle_with_square():
    window = turtle.Screen()
    window.bgcolor("white")
    cursor = turtle.Turtle()

    for i in range(24):
        draw_square(cursor)
        cursor.right(15)

    window.exitonclick()


draw_circle_with_square()