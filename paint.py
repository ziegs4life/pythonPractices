def paintShape():
    i = 0
    while i < 1:
        shape = raw_input("""What shape do you want to print?
1.Triangle
2.Square
3.Circle
""")
        if shape.lower() == 'triangle':
            shape = 1
            i += 1
        elif shape.lower() == 'square':
            shape = 2
            i += 2
        elif shape.lower() == 'circle':
            shape = 3
            i += 3
        else:
            print "Invalid input"
            i = 0

    height = int(raw_input("How High?"))

    if shape == 1:
        print triangle(height)
    elif shape == 2:
        print square(height)
    elif shape == 3:
        print circle(height)
    else:
        print circle(height)

def triangle(height):
    for i in range(height):
       space = 3 - i
       aval_space = height - (space * 2)
       print (" " * space) + ("*" * aval_space) + (" " * space)
def square(height):
        square = "*" * (height)
        for i in range(height):
           print square
# def circle(height):
#     w = height
#     middle = 0
#     space = 0
#
#     if height % 2 == 0
#         middle = height / 2
#     else:
#         middle = round(height/2) +1
#
#     for i in range(height)
#         if (i + 1) - middle < 0:
#             space = (i + 1) - middle * -1
#         else:
#             (i + 1) - middle

paintShape()
