# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:08:11 2019

@author: Bernard
"""
###########################################################
#Computer Project #2
# Accepts user input
#  Algorithm
#   Prompts user to enter integer
# Uses input to create visually appealing circles and squares
###########################################################

import random
import turtle
user_str = input("Enter 0 to quit, 1 for circles, or 2 for filled square\
 spirals:"   )
user_choice = int(user_str)
while user_choice > 2 or user_choice <0:
    print("Error invalid command")
    user_str = input("Enter 0 to quit, 1 for circles, or 2 for filled square\
 spirals:"   )
    user_choice =  int(user_str)
    
if user_choice ==1:
    AMOUNT_OF_CIRCLES = input("Enter the number of circles to draw: ")
    AMOUNT_OF_CIRCLES =int(AMOUNT_OF_CIRCLES)
   
    while AMOUNT_OF_CIRCLES < 1:
       print ("Number of circles must be positive; try again.")
       AMOUNT_OF_CIRCLES = input("Enter the number of circles to draw: ")
       AMOUNT_OF_CIRCLES =int(AMOUNT_OF_CIRCLES)
    
    if AMOUNT_OF_CIRCLES >= 1:
         LARGEST_RADIUS = input("Enter the radius (>=50, <=200) of the largest\
 circle: ")
         LARGEST_RADIUS =int(LARGEST_RADIUS)
         
         while LARGEST_RADIUS  <50 or LARGEST_RADIUS >200:
             print("The radius must be an integer between 50 and 200; try agai\
n.")
             LARGEST_RADIUS = input("Enter the radius (>=50, <=200) of the lar\
gest circle: ")
             LARGEST_RADIUS =int(LARGEST_RADIUS)
         
         if    50<=LARGEST_RADIUS <=200:
             START_SPOT =  float(LARGEST_RADIUS/AMOUNT_OF_CIRCLES)
             NUMB_OF_CIRCLES =  int(AMOUNT_OF_CIRCLES)
             turtle.clear()
             turtle.goto(0,0)
             turtle.color(random.random(),random.random(),random.random())
             turtle.begin_fill()
             turtle.circle(LARGEST_RADIUS)
             turtle.end_fill()
             NUMB_OF_CIRCLES -=1
             LOOP = int(1)
         
         while NUMB_OF_CIRCLES > 0:
             turtle.goto(0,START_SPOT*LOOP)
             turtle.color(random.random(),random.random(),random.random())
             turtle.begin_fill()
             turtle.circle(LARGEST_RADIUS-(START_SPOT*LOOP))
             turtle.end_fill()
             NUMB_OF_CIRCLES -=1
             LOOP +=1


if user_choice ==2:
    
    AMOUNT_OF_SQUARES =input("Enter the number of squares to draw: ")
    AMOUNT_OF_SQUARES =int(AMOUNT_OF_SQUARES)
    
    while AMOUNT_OF_SQUARES < 1:
        print("Number of squares must be positive; try again.")
        AMOUNT_OF_SQUARES =input("Enter the number of squares to draw: ")
        AMOUNT_OF_SQUARES =int(AMOUNT_OF_SQUARES)
    
    if AMOUNT_OF_SQUARES >=1:
        LARGEST_SIDE = input("Enter the side length (>=50, <=200) of the\
 largest square: ")
        LARGEST_SIDE =int(LARGEST_SIDE)
    
        while LARGEST_SIDE < 50 or LARGEST_SIDE > 200:
            print("The side length must be an integer between 50 and 200;\
 try again.")
            LARGEST_SIDE = input("Enter the side length (>=50, <=200) of the\
 largest square: ")
            LARGEST_SIDE =int(LARGEST_SIDE)
        
        if 50<= LARGEST_SIDE <=200:
            HEADING = float(360/AMOUNT_OF_SQUARES)
            NUMB_OF_SQUARES =int(AMOUNT_OF_SQUARES)
            turtle.clear()
            turtle.pendown()
            turtle.goto(0,0)
            turtle.setheading(0)
            turtle.color(random.random(),random.random(),random.random())
            turtle.begin_fill()
            turtle.forward(LARGEST_SIDE)
            turtle.left(90)
            turtle.forward(LARGEST_SIDE)
            turtle.left(90)
            turtle.forward(LARGEST_SIDE)
            turtle.left(90)
            turtle.forward(LARGEST_SIDE)
            turtle.end_fill()
            turtle.penup()
            NUMB_OF_SQUARES -=1
            LOOP2 =int(1)
       
        while NUMB_OF_SQUARES >0:
            turtle.pendown()
            turtle.goto(0,0)
            turtle.setheading(HEADING*LOOP2)
            turtle.color(random.random(),random.random(),random.random())
            turtle.begin_fill()
            turtle.forward(LARGEST_SIDE)
            turtle.left(90)
            turtle.forward(LARGEST_SIDE)
            turtle.left(90)
            turtle.forward(LARGEST_SIDE)
            turtle.left(90)
            turtle.forward(LARGEST_SIDE)
            turtle.end_fill()
            turtle.penup()
            NUMB_OF_SQUARES -=1
            LOOP2 +=1
            

if user_choice  == 0:
    print("Program Exited")
