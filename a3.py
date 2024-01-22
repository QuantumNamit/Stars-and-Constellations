

# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# Wi52C3g7ZzkJ7XBcVRHY
# DO NOT EDIT THE ABOVE LINES

# INFORMATION FOR YOUR TA

import sys
import os
import turtle
import math

# STARTER CONSTANTS

BACKGROUND_COLOR = "black"
WIDTH = 600
HEIGHT = 600
RATIO=75
TICK_OFFSET=6
LABEL_OFFSET_X=20
LABEL_OFFSET_Y=20
SCREEN_X_ORIGIN=0
SCREEN_Y_ORIGIN=0
DIVIDING_OFFSET=4

# AXIS CONSTANTS
AXIS_COLOR = "blue"

# STAR CONSTANTS
STAR_COLOR = "white"
STAR_COLOR2 = "grey"

def read_star(entry):
        """
        :param entry:entry is the input filename
        :return:returns  None
        """

#file handling
        fileHandler=open(entry,"r")
        # variable c_1 represents list of all lines in file
        c_1=fileHandler.readlines()
        fileHandler.close()

        for line in c_1:
            line=line.rstrip()
            line=line.split(",")
            line[6]=line[6].split(";")

            if(line[6][0]!=""):
             print("%s is at (%.6f,%.6f) with magnitude %.2f"%(line[6][0],float(line[0]),float(line[1]),float(line[4])) )


        return None

def read_constellations(entry_1):
        '''
        :param entry_1: entry_1 is the input constellation name
        :return: None
        '''

#file handling

        fileHandler_1=open(entry_1,"r")

# constellation name is the first line in constellation file
        c_1=fileHandler_1.readlines()
        fileHandler_1.close()
        constellation_name=c_1[0].rstrip()

# creating a blank set for storing stars names
        a_1=set()

        for line in c_1:
            d_1=line.rstrip()
            d_1=d_1.split(",")
            e_1=set(d_1)
            f_1=a_1.update(e_1)

# a_1 now is the set  all the stars in the constellation file
            a_1.discard(constellation_name)

        print(f"%s constellation contains {a_1}"%(constellation_name))

        return None



def draw_constellations(entry,entry_1,equation_counter,pointer):
      """
      :param entry:entry is the input filename
      :param entry_1: entry_1 is the input constellation name
      :param equation_counter: variable for drawing constellations in different colors
      :param pointer: pointer is the pen
      :return: None
      """

# code for drawing constellations in different colors
      if(equation_counter%3==0):
       line_color="red"
      elif(equation_counter%3==1):
       line_color="green"
      elif(equation_counter%3==2):
       line_color="yellow"

 # creating blank dictionary
      dict={}

#file handling
      fileHandler=open(entry,"r")
# variable c_1 represents list of all lines in file
      c_1=fileHandler.readlines()
      fileHandler.close()
      for line in c_1:
            line=line.rstrip()
            line=line.split(",")
            line[6]=line[6].split(";")

            if(line[6][0]!=""):
             dict[line[6][0]]=[line[0],line[1]]

             if(len(line[6])==2)  :
                 dict[line[6][1]]=[line[0],line[1]]

             elif(len(line[6])==3) :
                 dict[line[6][1]]=[line[0],line[1]]
                 dict[line[6][2]]=[line[0],line[1]]

      #file handling
      fileHandler_1=open(entry_1,"r")
      e_1=fileHandler_1.readlines()
      fileHandler_1.close()
      constellation_name=e_1[0].rstrip()

      for line in e_1 :
        line=line.rstrip()
        line=line.split(",")

        if(line[0]!=constellation_name):
         key_1=line[0]
         key_2=line[1]

#l_1 and m_1 represents lists of x and y coordinates of stars in the constellation file
         l_1=dict[key_1]
         m_1=dict[key_2]

# converting to screen coordinates
         x_1,y_1=calc_to_screen_coord(DIVIDING_OFFSET*float(l_1[0]), DIVIDING_OFFSET*float(l_1[1]), WIDTH, HEIGHT, RATIO)
         x_2,y_2=calc_to_screen_coord(DIVIDING_OFFSET*float(m_1[0]), DIVIDING_OFFSET*float(m_1[1]), WIDTH, HEIGHT, RATIO)

#drawing constellations
         pointer.penup()
         pointer.color(line_color)
         pointer.goto(x_1,y_1)
         pointer.pendown()
         pointer.goto(x_2,y_2)

      return None

def draw_star(entry,pointer):
        '''

        :param entry:entry is the input filename
        :return:None
        '''

#File Handling
        fileHandler=open(entry,"r")
        # variable e_1 represents list of all lines in file
        e_1=fileHandler.readlines()
        fileHandler.close()

        for line in e_1:
            line=line.rstrip()
            line=line.split(",")
            pointer.penup()

            if(line[6]!="") :
#drawing stars which are named
             pointer.color(STAR_COLOR)
             x_1,y_1= calc_to_screen_coord(DIVIDING_OFFSET*float(line[0]), DIVIDING_OFFSET*float(line[1]), WIDTH, HEIGHT, RATIO)
             pointer.goto(x_1,y_1)
             pointer.pendown()
             diameter=10/((float(line[4])+2))
             pointer.circle(diameter/2)
             pointer.dot(diameter)

            elif(line[6]=="") :
#drawing stars which are not named
                pointer.color(STAR_COLOR2)
                x_2,y_2= calc_to_screen_coord(DIVIDING_OFFSET*float(line[0]), DIVIDING_OFFSET*float(line[1]), WIDTH, HEIGHT, RATIO)
                pointer.goto(x_2,y_2)
                pointer.pendown()
                diameter=10/((float(line[4])+2))
                pointer.circle(diameter/2)
                pointer.dot(diameter)

        return None

def stars_name(entry,pointer):
        '''

        :param entry: entry is the input filename
        :return: None
        '''

# file handling
        fileHandler=open(entry,"r")
        c_1=fileHandler.readlines()

        for line in c_1:

            line=line.rstrip()
            line=line.split(",")
            pointer.penup()

            if(line[6]!="") :
# WRITING NAMES OF THE NAMED STARS
             pointer.color(STAR_COLOR)
             a,b= calc_to_screen_coord(DIVIDING_OFFSET*float(line[0]), DIVIDING_OFFSET*float(line[1]), WIDTH, HEIGHT, RATIO)
             pointer.goto(a,b)
             pointer.pendown()
             line[6]=line[6].split(";")
             pointer.write(line[6][0],font=("Arial",5,"normal"))

        return None

def setup():
    """
    Setup the turtle window and return drawing pointer
    :return: Turtle pointer for drawing
    """

    turtle.bgcolor(BACKGROUND_COLOR)
    turtle.setup(WIDTH, HEIGHT, 0, 0)
    screen = turtle.getscreen()
    screen.delay(delay=0)
    screen.setworldcoordinates(SCREEN_X_ORIGIN, SCREEN_Y_ORIGIN, WIDTH, HEIGHT)
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(0)
    pointer.up()
    return pointer


#TOOK THE BELOW calc_minmax_x and calc_minmax_y from my previous work in ASSIGNMENT 2

def calc_to_screen_coord(x, y, WIDTH, HEIGHT, RATIO):
    """
    Convert a calculator (x,y) to a pixel (screen_x, screen_y) based on origin location and ratio
    :param x: Calculator x
    :param y: Calculator y
    :param WIDTH: Width of turtle graphics screen
    :param HEIGHT: Height of turtle graphics screen
    :param RATIO: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (screen_x, screen_y) pixel version of calculator (x,y)
    """

# this mathematical approach calculates screen_x and screen_y coordinates

    screen_x=x*RATIO+WIDTH/2
    screen_y=y*RATIO+HEIGHT/2
    return screen_x,screen_y

def calc_minmax_x(WIDTH, RATIO):

    """
    Calculate smallest and largest calculator INTEGER x value to draw for a 0->WIDTH of screen
    Smallest: Convert a pixel x=0 to a calculator value and return integer floor
    Largest : Convert a pixel x=WIDTH to a calculator value and return integer ceiling
    :param WIDTH: Width of turtle graphics screen
    :param RATIO: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) x value to draw for a 0->WIDTH of screen
    """

#calculating mininimum as well as maximum  x and y for the calculator on x axis

    X_1_CALC =(SCREEN_X_ORIGIN-WIDTH/2)/RATIO
    MIN_X=int(math.floor(X_1_CALC))
    X_2_CALC=(WIDTH-WIDTH/2)/RATIO
    MAX_X=int(math.ceil(X_2_CALC))
    return MIN_X,MAX_X

def calc_minmax_y(HEIGHT, RATIO):

    """
    Calculate smallest and largest calculator INTEGER y value to draw for a 0->HEIGHT of screen
    Smallest: Convert a pixel y=0 to a calculator value and return integer floor
    Largest : Convert a pixel y=HEIGHT to a calculator value and return integer ceiling
    :param HEIGHT: Height of turtle graphics screen
    :param RATIO: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) y value to draw for a 0->HEIGHT of screen
    """

#calculating mininimum as well as maximum  x and y for the calculator on y axis

    Y_1_CALC =(SCREEN_Y_ORIGIN-HEIGHT/2)/RATIO
    MIN_Y=int(math.floor(Y_1_CALC))
    Y_2_CALC=(HEIGHT-HEIGHT/2)/RATIO
    MAX_Y=int(math.ceil(Y_2_CALC))
    return MIN_Y,MAX_Y

def draw_line(pointer, screen_x1, screen_y1, screen_x2, screen_y2):

    """
    Draw a line between two pixel coordinates (screen_x_1, screen_y_1) to (screen_x_2, screen_y_2)
    :param pointer: Turtle pointer to draw with
    :param screen_x1: The pixel x of line start
    :param screen_y1: The pixel y of line start
    :param screen_x2: The pixel x of line end
    :param screen_y2: The pixel y of line end
    :return: None (just draws in turtle)
    """

    pointer.penup()
    pointer.color(AXIS_COLOR)
    pointer.goto(screen_x1,screen_y1)
    pointer.pendown()
    pointer.goto(screen_x2,screen_y2)
    pointer.penup()
    return None

def draw_x_axis_tick(pointer, screen_x, screen_y):

    """
    Draw an x-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """

# subtracting and adding tick offset to  draw line
    draw_line(pointer,screen_x,screen_y-TICK_OFFSET,screen_x,screen_y+TICK_OFFSET)
    return None

def draw_x_axis_label(pointer, screen_x, screen_y, label_text):

    """
    Draw an x-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """

    pointer.penup()
    pointer.goto(screen_x,screen_y-LABEL_OFFSET_X)
    pointer.pendown()
    pointer.color(AXIS_COLOR)
    pointer.write(label_text,align="center")
    return None

def draw_y_axis_tick(pointer, screen_x, screen_y):

    """
    Draw an y-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """

# subtracting and adding tick offset to  draw line
    draw_line(pointer,screen_x-TICK_OFFSET,screen_y,screen_x+TICK_OFFSET,screen_y)
    return None

def draw_y_axis_label(pointer, screen_x, screen_y, label_text):

    """
    Draw an y-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """

    pointer.penup()
    pointer.goto(screen_x-LABEL_OFFSET_Y,screen_y)
    pointer.pendown()
    pointer.color(AXIS_COLOR)
    pointer.write(label_text,align="center")
    return None

def draw_axes(pointer):

    '''
    :return:returns None
    '''
# drawing x and y axes

    draw_line(pointer,0,HEIGHT/2,WIDTH,HEIGHT/2)
    draw_line(pointer,WIDTH/2,0,WIDTH/2,HEIGHT)
    C_MIN_X,D_MAX_X=calc_minmax_x(WIDTH,RATIO)
    C_MIN_Y,D_MAX_Y=calc_minmax_y(HEIGHT,RATIO)

    for i in range (C_MIN_X,D_MAX_X+1):
     e_screen_x,f_screen_y =calc_to_screen_coord(i,0,WIDTH,HEIGHT,RATIO)
     draw_x_axis_tick(pointer,e_screen_x,HEIGHT/2)
     draw_x_axis_label(pointer,e_screen_x,HEIGHT/2,i/DIVIDING_OFFSET)

    for i in range(C_MIN_Y,D_MAX_Y+1):
        g_screen_x,h_screen_y =calc_to_screen_coord(0,i,WIDTH,HEIGHT,RATIO)
        draw_y_axis_tick(pointer,WIDTH/2,h_screen_y)
        draw_y_axis_label(pointer,WIDTH/2,h_screen_y,i/DIVIDING_OFFSET)

    return None


def main():

    """
    Main constellation program
    :return: None
    """

    pointer = setup()
 # Handle arguments

    if(len(sys.argv)==1):
     looping=True
     entry=input("Enter the name of the input file with star information (ex.stars.all.dat):")

     if(os.path.isfile(entry)):
        looping=True

     else:
        while looping:
            if(entry==""):
                sys.stderr.write("No filename was entered so program exiting !")
                sys.exit(1)

            elif(os.path.isfile(entry)):
                looping=False
            else:
                 entry=input("Entered wrong file name kindly enter  the name of the input file with star information (ex.stars.all.dat):")
                 looping=True
    # Read star information from file (function)
     read_star(entry)
    # Draw Axes (function)
     draw_axes(pointer)
    # Draw Stars (function)
     draw_star(entry,pointer)



    elif(len(sys.argv)==2 and "-names" not in sys.argv):
        entry=sys.argv[1]
      # Read star information from file (function)
        read_star(entry)
      # Draw Axes (function)
        draw_axes(pointer)
      # Draw Stars (function)
        draw_star(entry,pointer)



    elif(len(sys.argv)==2 and sys.argv[1]=="-names"):
          looping=True
          entry=input("Enter the name of the input file with star information (ex.stars.all.dat):")

          if(os.path.isfile(entry)):
            looping=True

          else:
           while looping:
            if(entry==""):
                looping=False
            elif(os.path.isfile(entry)):
                looping=False
            else:
                 entry=input("Entered wrong filename kindly enter  the name of the input file with star information (ex.stars.all.dat):")
                 looping=True

       # Read star information from file (function)
          read_star(entry)
       # Draw Axes (function)
          draw_axes(pointer)
       # Draw Stars (function)
          draw_star(entry,pointer)
       #Draw stars_name(function)
          stars_name(entry,pointer)

    elif(len(sys.argv)==3 and sys.argv[2]=="-names"):
        entry=sys.argv[1]
         # Read star information from file (function)
        read_star(entry)
        # Draw Axes (function)
        draw_axes(pointer)
        # Draw Stars (function)
        draw_star(entry,pointer)
        #Draw stars_name(function)
        stars_name(entry,pointer)


    elif(len(sys.argv)==3 and sys.argv[1]=="-names"):
        entry=sys.argv[2]
    # Read star information from file (function)
        read_star(entry)
    # Draw Axes (function)
        draw_axes(pointer)
    # Draw Stars (function)
        draw_star(entry,pointer)
    #Draw stars_name(function)
        stars_name(entry,pointer)


    elif(len(sys.argv)==3 and "-names" not in sys.argv):
        sys.stderr.write("Invalid argument as neither input was -names")
        sys.exit(1)


    elif(len(sys.argv)>3) :
        sys.stderr.write("Too Many Arguments")
        sys.exit(1)

    flag=True
    equation_counter=0
    while flag:
        # Read constellation file (function)
        # Draw Constellation (function)
        # Draw bounding box (Bonus) (function)
         entry_1=input("Enter constellation filename:")
         if(os.path.isfile(entry_1)):
          read_constellations(entry_1)
          draw_constellations(entry,entry_1,equation_counter,pointer)
          equation_counter+=1
          flag=True
         else:
            loop=True
            while loop:
              if((entry_1=="")):
                 sys.stderr.write("EXITING THE PROGRAM !")
                 sys.exit(1)

              elif(os.path.isfile(entry_1)==True):
                  read_constellations(entry_1)
                  draw_constellations(entry,entry_1,equation_counter,pointer)
                  loop=False

              elif( (os.path.isfile(entry_1)==False) ) :
                  entry_1=input("Enter a VALID  constellation filename:")
                  loop=True


main()

print("\nClick on window to exit!\n")
turtle.exitonclick()

