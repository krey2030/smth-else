"""
Spider Commuons

Kurt Ashe Rey. Intal
9 Pinatubo
ValEd Creative Output Project on Human Fluorishing
"""
"""
Lines 1 ~ 8 - Class Format
Lines 9 ~ 20 - Table of Contents and important message
Lines 22 ~ 53 - Imports, Utility Functions and Variables
Function at line 55 - Running of Program
Function at line 73 - Run in Terminal
Function at line 112 - Run in Turtle
Lines 189 ~ 205 - Unimportant message 【ignore it】

※Color set used: Tau-Comlines
※Vscode is recommended to be used
"""
from os import system as sys #makes it simple
import time
from turtle import *
from turtle import color as tcolor #color is already used so replaced
from turtle import clearscreen as trueclearscreen
from important_module import *
from random import *

C = f"{effect(1)}{color('#000',ON)}{color('#4d6',OFF)}" #green text (brighter)
OS = f"{effect(22)}{color('#090',OFF)}{color('#000',ON)}" #green text (Darker)

def Program_run():#starts program
    global theme
    sys("cls")
    time.sleep(0.5)
    print(f"{effect(0)}{OS}You are about to open the {color('#fff',ON)}{color('#000',OFF)}『{effect(3)}title**{effect(23)}』{OS} game.")
    time.sleep(0.5)
    print(f"This game will utilize the terminal for input, turtle for designs, and both for text. VSCode is recommended.")
    while True:
        start = input(f"{effect(23)}{OS}Input {C}{effect(3)}x{effect(22)}{effect(23)}{OS} to cancel. Otherwise, continue. 【press enter】\n{effect(1)}{effect(3)}{C}").lower()
        print()
        if start != "x":GAMESEQUENCE()
        else:
            print(f"{effect(0)}{OS}")
        break
    time.sleep(1)
    sys("cls")#"cls" for VSCode, "clear" for onlinegdb
    time.sleep(0.4)
    print(f"{effect(3)}Game terminated.{effect(22)}")

def clearscreen(Hex,frame):#better clear screen lol
    pencolor(Hex)
    pendown()
    pensize(frame*8)
    forward(0)
    penup()

def GRID(frame,step,length):#debugging purposes
    Screen().tracer(0)
    pendown()
    pensize(0)
    speed(0)
    pencolor('#090')
    forward(step*length/2)
    right(90)
    forward(step*length/2)
    right(90)
    for gridth in range(round(length/2)):
        forward(step*length)
        right(90)
        forward(step)
        right(90)
        forward(step*length)
        left(90)
        forward(step)
        left(90)
    for gridth in range(round(length/2)):
        forward(step)
        left(90)
        forward(step*length)
        right(90)
        forward(step)
        right(90)
        forward(step*length)
        left(90)
    right(180)
    forward(step*length)
    right(90)
    forward(step*length/2)
    right(90)
    forward(step*length/2)
    left(180)
    penup()
    Screen().tracer(1)

class objects():
    def officecubicle(self,frame,step,sin,c1,c2,c3):
        pendown()
        speed(step/2)
        pensize(0)
        pencolor(c1)
        fillcolor(c1)

        #mainpart
        forward(step*6)
        begin_fill()
        right(90)
        forward(step*6)
        left(15)
        forward(step*sin[15]*24)
        right(105)
        forward(step*(36-6*3**0.5))
        right(90)
        forward(step*24)
        right(90)
        forward(step*(36-6*3**0.5))
        right(105)
        forward(step*sin[15]*24)
        left(15)
        forward(step*6)
        end_fill()
        right(90)
        forward(step*10)
        left(90)

        #borders
        pencolor(c2)
        forward(step*6)
        for _ in range(2):
            left(90)
            forward(step*10)
            left(90)
            forward(step*12)
        right(24)
        forward(step*6/sin[66])
        right(156)
        forward(step*24)
        right(156)
        forward(step*6/sin[66])
        forward(-step*6/sin[66])
        right(24)
        forward(step*6)

        fillcolor(c2)
        right(90)

        #left,right shadow, floor
        begin_fill()
        forward(step*(14-6*(sin[24]/sin[66]+sin[36]/sin[54])))
        left(90)
        forward(step*12)
        left(90)
        forward(step*(14-6*(sin[24]/sin[66]+sin[36]/sin[54])))
        right(90)
        forward(step*6)
        right(90)
        forward(step*(14-6*sin[24]/sin[66]))
        right(90)
        forward(step*24)
        right(90)
        forward(step*(14-6*sin[24]/sin[66]))
        right(90)
        forward(step*6)
        end_fill()

        #floor+borderfloor
        right(90)
        forward(step*(14-6*(sin[24]/sin[66]+sin[36]/sin[54])))
        pencolor(c3)
        right(54)
        forward(step*6/sin[54])
        penup()
        left(144)
        forward(step*24)
        left(144)
        pendown()
        forward(step*6/sin[54])
        right(54)
        penup()

        #back
        fillcolor(c3)
        begin_fill()
        forward(step*(14-6*(sin[24]/sin[66]+sin[36]/sin[54])))
        left(90)
        forward(step*12)
        left(90)
        forward(step*(14-6*(sin[24]/sin[66]+sin[36]/sin[54])))
        end_fill()
        forward(-step*(14-6*(sin[24]/sin[66]+sin[36]/sin[54])))

        left(90)
        forward(step*6)
        left(90)
        forward(step*6*sin[24]/sin[66])
        speed(0)

    def envelope(self,frame,step,sin,xpos,ypos,mirrored:bool,c1):
        Screen().tracer(0)
        forward(ypos)
        right(90)
        forward(xpos)
        Screen().tracer(1)
        pensize(step/8)
        speed(step/16)

        pendown()
        pencolor(c1)
        fillcolor(c1)
        begin_fill()
        forward(step*2)
        if mirrored:#\\
            right(60)
            forward(step/sin[60])
            right(120)
            forward(step*2)
            right(60)
            forward(step/sin[60])
        else:#//
            right(120)
            forward(step/sin[60])
            right(60)
            forward(step*2)
            right(120)
            forward(step/sin[60])
            right(60)
        left(90)
        end_fill()

        penup()
        pensize(0)
        speed(0)
        Screen().tracer(0)
        right(90)
        forward(-xpos)
        left(90)
        forward(-ypos)


    class monitor:
        def __init__(self,frame,step,sin,c1,c2,c3,c4):
            #base
            pencolor(c4)
            pendown()
            fillcolor(c4)
            begin_fill()
            right(90)
            forward(step*2)
            left(90)
            circle(step,90)
            forward(step*2)
            circle(step,90)
            left(90)
            forward(step*2)
            left(90)
            end_fill()

            #neck
            forward(step)
            pensize(step/2)
            forward(step)

            #screen
            fillcolor(c2)
            pencolor(c1)
            begin_fill()
            right(90)
            pensize(step/2)
            forward(step*6)

            penup()#blink
            forward(-step)
            pendown()
            pensize(step/4)
            pencolor(c3)
            forward(0)
            pencolor(c1)
            pensize(step/2)
            penup()
            forward(step)
            pendown()

            left(90)
            pensize(step/4)
            forward(step*6.75)
            left(90)
            forward(step*12)
            left(90)
            forward(step*6.75)
            left(90)
            pensize(step/2)
            forward(step*6)
            end_fill()
            left(90)
            penup()
            pensize(0)

        def power(self):
            None
    
    
    
    class desktop:
        def __init__(self,frame,step,sin,xpos,ypos,c1,c2,c3,c4):#oddly enough the main part became the monitors
            speed(step/8)
            forward(ypos)
            right(90)
            forward(xpos)
            left(90)
            self.monitor = objects().monitor(frame,step,sin,c1,c2,c3,c4)
            right(90)
            forward(-xpos)
            left(90)
            forward(-ypos)

        def keyboard(self,frame,step,sin,xpos,ypos,c1,c2):#decoration only
            speed(step/8)
            forward(ypos)
            right(90)
            forward(xpos)
            pencolor(c2)
            pendown()
            fillcolor(c1)

            begin_fill()
            forward(step*4)
            left(114)
            forward(step/sin[66])
            left(66)
            forward(step*(8-2*sin[24]/sin[66]))
            left(66)
            forward(step/sin[66])
            left(114)
            forward(step*4)
            end_fill()
            for _ in range(3,-1,-1):
                forward(step*_)
                left(90+_*6)
                forward(step/sin[90-_*6])
                left(90-_*6)
                forward(step*2*(_-sin[_*6]/sin[90-_*6]))
                left(90-_*6)
                forward(step/sin[90-_*6])
                left(90+_*6)
                forward(step*_)
                
            
            penup()
            forward(-xpos)
            left(90)
            forward(-ypos)

        def mouse(self,frame,step,sin,xpos,ypos,c1,c2):
            forward(ypos)
            right(90)
            
            forward(xpos)

            pendown()
            pencolor(c2)
            fillcolor(c1)
            begin_fill()
            for _ in range(2):
                circle(step*1/3,90)
                forward(step*1/3)
                circle(step*1/3,90)
            end_fill()
            left(90)
            penup()
            forward(step*0.5)
            pendown()
            forward(step*0.15)
            pensize(step/8)
            forward(step*0.2)
            pensize(0)
            forward(step*0.15)
            penup()
            forward(-step*2)

            right(90)
            forward(-xpos)
            left(90)
            forward(-ypos)
            
        class sys_unit():
            def __init__(self,frame,step,sin,xpos,ypos,mirrored,c1,c2,c3,c4,c5,c6):
                self.xpos = xpos
                self.ypos = ypos
                self.step = step
                self.sin = sin
                self.c3 = c3

                forward(ypos)
                right(90)
                
                forward(xpos)
                left(90)
                
                pendown()
                pencolor(c1)
                fillcolor(c1)
                begin_fill()
                forward(step*7)
                if mirrored:left(60)
                else:right(60)
                
                forward(step*5/sin[60])#includes trig kasi yay
                if mirrored:right(150)
                else:left(150)
                forward(step*5)
                if mirrored:right(30)
                else:left(30)
                forward(step*5/sin[60])
                if mirrored:right(60)
                else:left(60)
                forward(step*7)
                if mirrored:right(90)
                else:left(90)
                forward(step*5)
                if mirrored:right(30)
                else:left(30)
                
                forward(step*5/sin[60])#includes trig kasi yay
                if mirrored:right(60)
                else:left(60)
                forward(step*7)
                right(120)
                forward(step*5/sin[60])
                end_fill()

                pencolor(c2)
                left(180)
                forward(step*5/sin[60])
                forward(-step*5/sin[60])
                right(60)
                forward(-step*7)
                forward(step*7)
                right(90)
                forward(step*5)
                forward(-step*5)
                left(90)
                penup()
                forward(-step*7)
                right(90)
                forward(-xpos)
                left(90)
                forward(-ypos)

            def power(self):
                forward(self.ypos)
                right(90)
                
                forward(self.xpos)
                left(90)

                forward(self.step*7)
                right(90)
                forward(self.step*4.5)
                left(120)
                forward(self.step*0.5/sin[60])
                pendown()
                pencolor(self.c3)
                pensize(self.step/2)
                forward(0)
                objects().desktop.monitor.power(self.frame,self.step,self.sin,self.c4,self.c5,self.c6)

class areas():
    def SSVEU_reset(self,frame,step,sin):
        Screen().tracer(0)
        clearscreen('#112',frame)
        objects().officecubicle(frame,step,sin,'#667','#445', '#334')
        objects().envelope(frame,step,sin,step*5,-step,False,'#765')
        SSVEUpc = objects().desktop(frame,step,sin,0,step*-1.5,'#555','#000','#00e','#444')
        SSVEUpc.keyboard(frame,step,sin,0,step*-4,'#000','#444')
        SSVEUpc.mouse(frame,step,sin,step*5,step*-4,'#000','#444')
        SSVEUpc.sys_unit(frame,step,sin,step*6.5,-step*(16-sin[60]),True,'#000','#112','#00e','#fff','#fff','#fff')
        Screen().tracer(1)
    
    def SSVEU(self,frame,step,sin):
        clearscreen('#000',frame)
        #Screen().update()
        print(f"{OS}{color('#667',OFF)}You're about to wake up... input {effect(1)}{effect(3)}x{effect(22)}{effect(23)} to go back to sleep.")
        decision = input(f"Otherwise you will start looking around.{effect(1)}{effect(3)}").lower()
        while decision == "x":
            print(f"{effect(22)}{effect(23)}You decided to go back to sleep again.")
            time.sleep(0.5)
            decision = input(f"{OS}{color('#667',OFF)}You are waking up. Input {effect(1)}{effect(3)}x{effect(22)}{effect(23)} or you will start looking around.").lower()
            time.sleep(0.5)
        print(f"{color('#112',ON)}{color('#667',OFF)}{effect(22)}{effect(23)}You look around. You found yourself in the SSVE Unit.")#SocSci ValEd Unit
        clearscreen('#112',frame)
        #Screen().update()

        GRID(frame,step,36)
        
        objects().officecubicle(frame,step,sin,'#667','#445', '#334')
        print(f"At front, your desk.",end=" ",flush=True)
        
        objects().envelope(frame,step,sin,step*5,-step,False,'#765')
        print(f"To the side is an envelope.",end=" ",flush=True)
        
        Screen().tracer(1)
        SSVEUpc = objects().desktop(frame,step,sin,0,step*-1.5,'#555','#000','#00e','#444')
        print(f"On the desk is a monitor.")

        SSVEUpc.keyboard(frame,step,sin,0,step*-4,'#000','#444')
        print(f"It has a keyboard ",end="",flush=True)
        SSVEUpc.mouse(frame,step,sin,step*5,step*-4,'#000','#444')
        print(f"and a mouse. And finally,",end=" ",flush=True)

        SSVEUpc.sys_unit(frame,step,sin,step*6.5,-step*(16-sin[60]),True,'#000','#112','#00e','#fff','#fff','#fff')
        print(f"below is a PC system unit.")
        
        time.sleep(2)
        print(f"You saw everything around you. What will you do now?")
        free = False
        while True:
            decision = input(f"{effect(22)}{effect(23)}Input {effect(1)}{effect(3)}v{effect(22)}{effect(23)} to see envelope. Input {effect(1)}{effect(3)}c{effect(22)}{effect(23)} to turn on computer. Input {effect(1)}{effect(3)}x{effect(22)}{effect(23)} to leave desk.{effect(1)}{effect(3)}\n").lower()
            if decision == "v":
                _ = areas.envelope(frame,step,sin,'#765','#cde','#9b9')
                print(f"{effect(22)}{effect(23)}Input {effect(1)}{effect(3)}hr{effect(22)}{effect(23)} to see {effect(1)}Learning Activity: Becoming a Pisay Scholar: Living the Core Values (Lesson 1){effect(22)}. ")
                decision2 = input(f"Input {effect(1)}{effect(3)}p{effect(22)}{effect(23)} to see periodic table. Otherwise, you will stop looking at the envelope.{effect(1)}{effect(3)}").lower()
                if decision2 == "hr":
                    _.HR_Lesson1()
                    input(f"{effect(22)}{effect(23)}You saw the homeroom activity.")
                elif decision2 == "p":
                    _.ptable()
                    input(f"{effect(22)}{effect(23)}You saw the Periodic Table. There is nothing important to know as of now.")
                del _
            elif decision == "c":
                while True:
                    #@class_method thingy
                    SSVEUpc.sys_unit.power()#NEXT THING TO DO
                areas().SSVEU_reset(frame,step,sin)
            elif decision == "x":
                if free:break
                else:
                    print(f"{effect(22)}{effect(23)}You decided to leave the desk.")
                    time.sleep(2)
                    print(f"You decided to go back to the desk since you have nothing else to do.")
            else:print(f"{effect(22)}You don't know what to do. You decided to {choice(["lick","stare at","brush your hand against"])} the {choice(["monitor", "mouse", "keyboard", "envelope", "glowing blue light shining from the monitor","desk","PC system unit"])}. Please decide better.")
    
    class envelope():
        def __init__(self, frame,step,sin,c1,c2,c3):
            self.frame = frame
            self.step = step
            self.sin = sin
            self.c2=c2
            self.c3=c3
            forward(-step*3)
            right(90)
            pendown()
            pensize(step/4)
            tcolor(c1)
            begin_fill()
            forward(step*8)
            left(90)
            forward(step*9)#height
            left(90)
            forward(step*16)#length
            left(90)
            forward(step*9)#height
            left(90)
            forward(step*8)
            end_fill()
            penup()
            left(90)
            pensize(0)

        def HR_Lesson1(self):
            tcolor(self.c2)
            forward(-self.step*2)
            right(90)
            pendown()
            begin_fill()
            forward(self.step*4)
            left(90)
            forward(self.step*13)
            left(90)
            forward(self.step*8)
            left(90)
            forward(self.step*13)
            left(90)
            forward(self.step*4)
            end_fill()
            penup()
            left(90)
            forward(self.step*2)
        
        def ptable(self):
            tcolor(self.c3)
            forward(self.step*2.25)
            right(90)
            pendown()
            begin_fill()
            forward(self.step*5)
            left(90)
            forward(self.step*5)
            left(90)
            forward(self.step*10)
            left(90)
            forward(self.step*5)
            left(90)
            forward(self.step*5)
            end_fill()
            penup()
            left(90)
            forward(-self.step*2.25)

        def __del__(self):
            forward(self.step*6)
            areas().SSVEU_reset(self.frame,self.step,sin)

class dictionary():None

def GAMESEQUENCE():
    while True:
        try:frame = round(float(input(f"{effect(22)}{effect(23)}{OS}PLEASE CHOOSE THE SIZE OF THE OVERALL TURTLE. {C}16{OS} BEST. You wont be able to see image on very high or very low values.{C}")),6) * 60
        except:print(f"{OS}{effect(3)}Pleae input a integer/decimal number.")
        else:
            if frame < 0:print(f"{OS}{effect(22)}{effect(3)}Please input a positive number.")
            else:break
    step = frame/30
    left(90)
    
    tracer(0)
    outofbounds = ['#000','#4d6','#090','#fff','#fff','#667','#112','#445','#334','#765','#555','#00e','#444']#easteregg+helpful collection colors used, #fff are title colors
    for _ in range(len(outofbounds)):clearscreen(outofbounds[_],frame*(-_+len(outofbounds)))
    tracer(1)

    areas().SSVEU(frame,step,sin)
    input()

if __name__ == "__main__":Program_run()

"""
personal comment example:
※A creative title and explaination🥰
※Text effects, time module, and os module for emphasis and style
※May have been used for reference: https://github.com/Ejirth/CS3/blob/main/Q1/q1_sg7_Pinatubo_Espiritu.py because plagiarizing without crediting is bad, also sampleInheristance and sampleComposition notes.
※I regret this but it would be difficult but also uses chatgpt to make dynamic variables. ...and a little bit more for understanding ...
※#some comments
※Title for program kasi i am muon themed.


lovely symbols:※【】「」『』※／•—
Tentative Ideas and stuff

ending: the full picture and digital card revealed, showing a heartfelt message
type of project: Game development, art attack, picture person
※guidelines:
※art attack:
hand-made or digital card serving as artistic appreciation
of person for one's self-giving, i.e. to honor the values
of that person in your life or others'.
card should contain an artistic design and a message of
recognition and appreciation
identify THAT PERSON
※picture person
complex/abstract idea of self-awereness, self-possession,
or self-giving can be conveyed with single still image,
wholesome, positive, inspiring


themes: carbon oxygen phosphorus hydrogen fluorine,
muon, spiders, clc, goddess of peace shrine, alot more

use classes to make objects in turtle python
use functions
half turtle, half terminal

digital cards and picture persons scattered around



This is no longer affiliated with the red turtle ...yeah legit

Gameplay:THIS IS DEMO ONLY, ONLY VALED UNIT WILL BE PRESENT

"""