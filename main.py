# import colorgram
#
# colors = colorgram.extract('hirst.jpeg', 100)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(187, 162, 130), (131, 91, 67), (78, 93, 120), (145, 161, 183), (213, 209, 128), (181, 150, 162), (28, 34, 50), (120, 77, 92), (46, 25, 17), (54, 23, 34), (145, 170, 154), (166, 159, 51), (84, 108, 91), (122, 28, 42), (174, 105, 93), (26, 38, 33), (217, 175, 188), (168, 102, 114), (50, 56, 97), (106, 121, 159), (124, 33, 23), (223, 177, 169), (174, 205, 180), (177, 186, 215), (104, 146, 113), (68, 75, 32), (165, 201, 210), (212, 210, 18), (37, 73, 83), (55, 71, 62), (97, 140, 148)]

tim.speed('fastest')
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_dots = 100

for i in range(1, num_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






screen = turtle_module.Screen()
screen.exitonclick()