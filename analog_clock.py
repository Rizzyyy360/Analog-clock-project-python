#YOU ARE FREE TO EDIT THIS PIECE OF CODE IF YOU KNOW MATHS WELL.

import turtle
import math
from datetime import datetime






s = turtle.Screen()
s.title("Analog Clock")
s.setup(width=500, height=800)

s.tracer(0)

#radius of the clock (for the border)
r = 200

#length of the second marker
rsec = r - 10           #10 unit shorter than the radius of the clock

#length of the minute marker
rmin = r -15            #...

#length of the hour marker
rhr = r - 60            #...

t = turtle.Turtle()
sec = turtle.Turtle()
min = turtle.Turtle()
hr = turtle.Turtle()


now = datetime.now()
starting_sec = now.second
starting_min = now.minute
starting_hr = now.hour

sec_angle = 90 - (90/15*(starting_sec))
min_angle = 90 - (90/15*(starting_min))
hr_angle = 90 - ((90/3)*(starting_hr - 12)+(1/2)*starting_min) #THE STARTING POINT
sec.hideturtle()


x_sec = r*math.cos(math.radians(sec_angle))
y_sec = r*math.sin(math.radians(sec_angle))

x_min = rmin*math.cos(math.radians(sec_angle))
y_min = rmin*math.sin(math.radians(sec_angle))

x_hr = rhr*math.cos(math.radians(hr_angle))
y_hr = rhr*math.sin(math.radians(hr_angle))
 
t.hideturtle()
t.speed(0)
angle = 0

x = r*math.cos(math.radians(angle))
y = r*math.sin(math.radians(angle))

def sec_marker():

    
    global sec_angle, sec
    sec.hideturtle()
    sec.goto(0, 0)
    sec.clear()
        
    x_sec = rsec*math.cos(math.radians(sec_angle))
    y_sec = rsec*math.sin(math.radians(sec_angle))
    sec_angle -= 6

    sec.goto(x_sec, y_sec)
    

    turtle.ontimer(sec_marker, 998)



def min_marker():

    global min_angle, starting_sec
    min.pensize(10)
    min.color("orange")
    min.hideturtle()
    min.goto(0, 0)
    min.clear()
        
    x_min = rmin*math.cos(math.radians(min_angle))
    y_min = rmin*math.sin(math.radians(min_angle))
    min_angle -= 6

    min.goto(x_min, y_min)
    

    turtle.ontimer(min_marker, 1000*(60-starting_sec))
    starting_sec = 0

def hr_marker():
    global hr_angle, starting_min
    hr.pensize(20)
    hr.color("lightblue")
    hr.hideturtle()
    hr.goto(0, 0)
    hr.clear()
        
    x_hr = rhr*math.cos(math.radians(hr_angle))
    y_hr = rhr*math.sin(math.radians(hr_angle))
    hr_angle -= 6

    hr.goto(x_hr, y_hr)
    

    turtle.ontimer(hr_marker, 1000*(abs(720-starting_min)))
    
    


def clock_border():  # setting up the boundary of the clock
    global t, x, y, angle

    #THE DOT MARKERS AROUND THE BORDER MARKING 3, 6, 9, 12
    border_marker = turtle.Turtle()
    border_marker.hideturtle()
    border_marker.color("#aaa")
    border_marker.shape("circle")      
    border_marker.shapesize(stretch_wid=1.5, stretch_len=1.5)
    border_marker.speed(0)

    #OTHER SURROUNDING MARKERS

    num_marker = turtle.Turtle()
    num_marker.hideturtle()
    num_marker.color("#aaa")
    num_marker.speed(0)
    num_marker.goto(0, 0)

    t.pensize(4)
    t.color("cyan")
    t.penup()
    t.goto(x, y)
    t.pendown()
    num = 2
    while angle <= 360:
        angle += 5
        x = r*math.cos(math.radians(angle))
        y = r*math.sin(math.radians(angle))
        t.goto(x, y)
        if angle % 90 == 0:

            x_dot = (r-20)*math.cos(math.radians(angle))
            y_dot = (r-20)*math.sin(math.radians(angle))
            border_marker.penup()
            border_marker.goto(x_dot, y_dot)
            border_marker.stamp()

        if angle % 30 == 0:

            x_num = (r-25)*math.cos(math.radians(angle))
            y_num = (r-25)*math.sin(math.radians(angle))
            num_marker.penup()
            num_marker.goto(x_num, y_num)
            if angle < 90:
                num_marker.write(f"{num}",align="left", font=("courier", 16, "normal")) if angle % 90 != 0 else num_marker.write("")
                num -=1

            else:
                num_marker.write(f"{12 - num}", align="left", font=("courier", 16, "normal")) if angle % 90 != 0 else num_marker.write("")
                num +=1



if __name__ == "__main__":
    clock_border()
    hr_marker()
    min_marker()
    sec_marker()


    while True:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        pen = turtle.Turtle()
        pen.speed(0)
        pen.hideturtle()
        pen.penup()
        pen.goto(0, -250)
        pen.write(current_time, align="center", font=("arial", 24, "bold"))
        s.update()
        pen.clear()

    
    