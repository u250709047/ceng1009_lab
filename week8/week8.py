# def get_grade(mark):
#     if mark >= 90:
#         return "A"
#     elif 80 <= mark < 90:
#         return "B"
#     elif 70 <= mark < 80:
#         return "C"
#     elif 60 <= mark < 70:
#         return "D"
#     else:
#         return "F"
#
# # Testing the function with a number of different marks
# test_marks = [95, 90, 85, 79.99999, 80, 70, 65, 55]
#
# for m in test_marks:
#     print(f"Mark: {m} -> Grade: {get_grade(m)}")

# import turtle
#
#
# def draw_bar(t, height):
#     # Set fill color based on the bar value
#     if height >= 200:
#         t.fillcolor("red")
#     elif 100 <= height < 200:
#         t.fillcolor("yellow")
#     else:
#         t.fillcolor("green")
#
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.write(str(height))
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#     t.forward(10)  # Gap between bars
#
#
# # Test list of values
# xs = [48, 117, 200, 240, 160, 260, 85]
#
# tess = turtle.Turtle()
# tess.color("blue")
# tess.pensize(3)
#
# for v in xs:
#     draw_bar(tess, v)
#
# turtle.mainloop()


# import turtle
#
#
# def draw_bar(t, height):
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#
#     # Position text above the 0 axis if the height is negative
#     if height < 0:
#         t.penup()
#         t.goto(t.xcor(), 5)  # Write just above the 0 axis
#         t.write(str(height))
#         t.goto(t.xcor(), height)  # Return back to the top of the bar
#         t.pendown()
#     else:
#         t.write(str(height))
#
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#     t.forward(10)
#
#
# # Test list containing negative values
# xs = [48, -30, 117, 200, -50, 160]
#
# tess = turtle.Turtle()
# tess.color("blue")
# tess.pensize(3)
# tess.penup()
# tess.goto(-200, 0)  # Center the starting position
# tess.pendown()
#
# for v in xs:
#     draw_bar(tess, v)
#
# turtle.mainloop()


import math

# def findHypot(a, b):
#     # Calculates the hypotenuse using x ** 0.5 (square root)
#     hypotenuse = (a ** 2 + b ** 2) ** 0.5
#     return hypotenuse
#
# # Testing the function
# side1 = 3
# side2 = 4
# result = findHypot(side1, side2)
#
# print(f"The length of the hypotenuse for sides {side1} and {side2} is: {result}")
