#Start = int(raw_input ("Enter Start Number"))
#End = int(raw_input ("Enter End Number"))
#for i in range (Start, End):
  #print i

## Odd Numbers

#for numbers in range (1,10,2):
#    print numbers



## Print a Square
def star():
    star = "*" * 5
    for i in range(5):
       print star
star()


# Print a Box
def star(height, width):

    star = "*" * (width)
    for i in range(height):
       print star

h = int(raw_input ("Enter height"))
w = int(raw_input ("Enter width"))

star(h,w)



# Print a Triangle
def triangle(height,width):
    for i in range(height):
       if i == 0 or i == height -1:
           print "*" * (width)
       else:
           print "*" + (' ' * (width - 2)) + "*"

h = int(raw_input ("Enter height"))
w = int(raw_input ("Enter width"))

triangle(h, w)


# Print a Triangle II
def triangle
height = 4
width = 7

for i in range(height):
   space = 3 - i
   aval_space = width - (space * 2)
   print (" " * space) + ("*" * aval_space) + (" " * space)

   height = int(raw_input ("Enter height"))
triangle()


adam(height):

width = (height * 2) -1

for i in range(height):
    space = (width/2) - i
    aval_space = width - (space * 2)
    print (" " * space) + ("*" * aval_space) + (" " * space)
h = int(raw_input ("Enter height"))

adam(h)
