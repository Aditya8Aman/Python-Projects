# import package
import turtle
 
# make screen object
# and set size
sc = turtle.Screen()
sc.setup(400,300)
 
# make turtle object
t1=turtle.Turtle(shape='square')
 
# do some motion with properties
t1.color("red")
t1.circle(50)
 
# make another turtle object
t2=turtle.Turtle(shape='circle')
 
# do some motion with properties
t2.color("green")
t2.circle(40)
 
# get all turtle objects on screen
print(sc.turtles())