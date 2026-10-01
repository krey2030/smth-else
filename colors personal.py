"""
Tau Comlines Extras

[Group N／A]
Kurt Ashe R. Intal
Non-school
Extra Activity
"""
"""
Lines 1 ~ 8 - Class Format 【kahit hindi naman class】
Lines 9 ~ 20 - Table of Contents and important message
Lines 22 ~ 53 - Imports, Utility Functions and Variables
Function at line 55 - Running of Program
Function at line 73 - Run in Terminal
Function at line 112 - Run in Turtle
Lines 189 ~ 205 - Unimportant message 【ignore it】

※The grid may be imperfect and uncentered, we do not care.
※Turtle may not work with onlinegdb. VSCode is recommended to be used, copy all of this and paste to VSCode.
"""

from os import system as sys #makes it simple
from turtle import * #turtle program
from turtle import color as tcolor #color is already used so replaced
import time
sys("cls")#"cls" for VSCode, "clear" for onlinegdb

def color(Hex,BG): #color UPDATED
    if Hex[0] == "#":#makes it realistic and raises error
        try:Hex[7]#should only be 3 or 6 digits
        except:
            try:Hex[6]
            except IndexError:
                try:Hex[4]#should only be 3 or 6 digits
                except IndexError:
                    r = int(Hex[1], 16)
                    g = int(Hex[2], 16)
                    b = int(Hex[3], 16)
                    return f"\x1b[{BG};2;{r*17};{g*17};{b*17}m"#default used personally
                else:raise IndexError("string index out of range")#fake error
            else:
                r = int(f"{Hex[1]}{Hex[2]}",16)
                g = int(f"{Hex[3]}{Hex[4]}",16)
                b = int(f"{Hex[5]}{Hex[6]}",16)
                return f"\x1b[{BG};2;{r};{g};{b}m"
        else:raise IndexError("string index out of range")#fake error
    else:raise ValueError(f"bad color string: '{Hex[0]}'")#should be in color string format
    #   color('#rgb',ON／OFF)
    #   color('#rrggbb',ON／OFF)
OFF = "38" #Text color
ON = "48" #Highlight
def effect(Effect: int): #text style for bold, italic, underlines, etc.
    return f"\x1b[{Effect}m" #1 = bold, #3 = italic, #4 = underline, #22 removed bold, #23 removes italic, #24 = removes underline

def Program_run(): #starts program, choice for terminal／turtle
    title_color = [color('#f00',OFF),color('#f50',OFF),color('#fa0',OFF),color('#ff0',OFF),color('#af0',OFF),color('#5f0',OFF),color('#0f0',OFF),color('#0f5',OFF),color('#0fa',OFF),color('#0ff',OFF),color('#0af',OFF),color('#05f',OFF),color('#00f',OFF),color('#50f',OFF),color('#a0f',OFF),color('#f0f',OFF),color('#f0a',OFF),color('#f05',OFF)]
    title_text = f"『Color Generataur』"
    title = ""#name of program with colors!
    for i in range(len(title_color)):title = title + title_color[i] + title_text[i]
    print(f"{effect(0)}{color('#090',OFF)}{color('#000',ON)}You opened the {title}{color('#090',OFF)} Program.")
    print(f"This program can produce all the colors depending on the color depth. Terminal can let you scroll back,")
    print(f"But a low color precision value may make it unable to scroll back far enough. Turtle would be animated.")
    while True:#program can run again
        output = input(f"{effect(22)}{effect(23)}{color('#090',OFF)}Input {color('#4d6',OFF)}{effect(1)}{effect(3)}terminal{effect(22)}{effect(23)}{color('#090',OFF)} or {color('#4d6',OFF)}{effect(1)}{effect(3)}turtle{effect(22)}{effect(23)}{color('#090',OFF)}. Inputting anything else will close the program.{color('#4d6',OFF)}{effect(1)}{effect(3)}\n").lower()
        if output == "terminal":terminal()
        elif output == "turtle":turtle()
        else:#program ends
            print(f"{color('#090',OFF)}{effect(22)}{effect(23)}The program was terminated.")
            time.sleep(1.2)
            sys("cls")#"cls" for VSCode, "clear" for onlinegdb
            break

def terminal():
    confirm = False
    while True:#Amount of colors
        print(f"\n{effect(22)}{effect(23)}{color('#090',OFF)}Input the {color('#4d6',OFF)}Color precision{color('#090',OFF)}. The lower the value, the higher the bit depth and the more colors. ")
        print(f"If the value is too small, it may make it unable to scroll back far enough to see all the colors.")
        print(f"A {color('#4d6',OFF)}factor of {effect(1)}255{color('#090',OFF)}{effect(22)} is recommended. A value of 3 has 86³【636056】 colors; 17 has 16³【4096】.")
        try:color_depth = int(input(f"Other factors: 5, 15, 51, 85, 255. Using a non-factor of 255 will result in {color('#fff',ON)}white 【#ffffff】{color('#000',ON)} absent.\n{effect(1)}{color('#4d6',OFF)}"))#error handling
        except ValueError:print(f"{effect(22)}{effect(3)}{color('#090',OFF)}Please input a natural number only.{effect(23)}")
        else:
            if color_depth <= 0:print(f"{effect(3)}Please input a natural 【postive】number only.{effect(23)}")#error handling
            if color_depth < 3:
                if confirm:#putting low number once will just try again
                    time.sleep(1.2)
                    confirm_ = input(f"{effect(22)}{effect(3)}{color('#090',OFF)}Are you sure about having that many colors? input {color('#4d6',OFF)}{effect(1)}y{effect(22)}{color('#090',OFF)}, otherwise you will input a larger number again.{color('#4d6',OFF)}")
                    if confirm_.lower() == "y":break#careful
                print(f"{effect(22)}{effect(3)}{color('#090',OFF)}Please input a larger number, since there would be too many to produce.{effect(23)}")
                confirm = True #wont repeat anymore
            else:break
    names=None
    if color_depth >= 15:names = input(f"{effect(22)}{color('#090',OFF)}Show hex value of color? input {effect(1)}{effect(3)}{color('#4d6',OFF)}y{effect(22)}{effect(23)}{color('#090',OFF)}, otherwise, it will show just the color.\n{effect(1)}{effect(3)}{color('#4d6',OFF)}")
    print(f"{effect(1)}{effect(23)}{color('#000',OFF)}")
    time.sleep(0.8)
    total_color = 0 #Color counter
    for r in range(0,256,color_depth):#red new square
        r2 = f"{hex(r)}"[2:4]
        if len(r2)==1:r2 = f"0{r2}"#forces 2 digits
        for g in range(0,256,color_depth):#green column
            g2 = f"{hex(g)}"[2:4]
            if len(g2)==1:g2 = f"0{g2}"#forces 2 digits
            for b in range(0,256,color_depth):#blue row
                b2 = f"{hex(b)}"[2:4]
                if len(b2)==1:b2 = f"0{b2}"#forces 2 digits
                if color_depth == 3:
                    print(f"{color(f'#{r2}{g2}{b2}',ON)} ",end=color(f'#000',ON))#thinner to fit
                elif names == "y" and color_depth == 15:print(f"{color(f'#{r2}{g2}{b2}',ON)}#{r2}{g2}{b2}",end=color(f'#000',ON))#namesshort
                elif names == "y" and color_depth <= 17:print(f"{color(f'#{r2}{g2}{b2}',ON)}#{r2}{g2}{b2}|",end=color(f'#000',ON))#namesshort
                elif names == "y":print(f"{color(f'#{r2}{g2}{b2}',ON)}[#{r2}{g2}{b2}]",end=color(f'#000',ON))#nameslong
                else:print(f"{color(f'#{r2}{g2}{b2}',ON)}  ",end=color(f'#000',ON))#more square shaped
                total_color +=1 #Color counter increase
            print()
        time.sleep((color_depth/255))
        print()
    print(f"Total colors: {total_color} 【{round(total_color**(1/3))}³】") #Shows total number of colors generated

def turtle():
    clearscreen() #resets the screen
    confirm = False
    oddconstant = 51/8 #top left
    while True:#Amount of colors
        print(f"\n{effect(22)}{effect(23)}{color('#090',OFF)}Input the {color('#4d6',OFF)}Color precision{color('#090',OFF)}. The lower the value, the higher the bit depth")
        print(f"and the more colors. A {color('#4d6',OFF)}factor of {effect(1)}255{color('#090',OFF)}{effect(22)} is recommended.")
        print(f"A value of 3 has 86³【636056】 colors;")
        print(f"17 has 16³【4096】. Other factors: 5, 15, 51, 85, 255.")
        try:color_depth = int(input(f" Using a non-factor of 255 will result in white 【#ffffff】absent.\n{effect(1)}{color('#4d6',OFF)}"))#not divisible
        except ValueError:print(f"{effect(22)}{color('#090',OFF)}{effect(3)}Please input a natural number only.{effect(23)}")
        else:
            if color_depth <= 0:print(f"{effect(3)}Please input a natural 【postive】number only.{effect(23)}")#error handling
            if color_depth < 7:
                if confirm:#putting low number once will just try again
                    time.sleep(1.2)
                    confirm_ = input(f"{effect(22)}{effect(3)}{color('#090',OFF)}Are you sure about having that many colors? input {color('#4d6',OFF)}{effect(1)}y{effect(22)}{color('#090',OFF)}, otherwise you will input a larger number again.{color('#4d6',OFF)}")
                    if confirm_.lower() == "y":break
                print(f"{effect(22)}{effect(3)}{color('#090',OFF)}Please input a larger number, since it would take too long to produce.{effect(23)}")
                confirm = True#wont repeat anymore
            else:break
            
    while True:#size of program
        print(f"\n{effect(22)}{effect(23)}{color('#090',OFF)}Please choose the size of the overall turtle program.")
        print(f"Some colors may be hidden on values too high. Grid may get crooked below 8.")
        print(f"The optimal value depends on the color precision.")
        try:frame = float(input(f"50-70% of the color precision is recommended.\n{effect(1)}{color('#4d6',OFF)}")) * 100#error handling
        except ValueError:print(f"{effect(22)}{color('#090',OFF)}Please input a decimal number.{effect(23)}")
        else:
            if frame <= 0:print(f"{effect(22)}{color('#090',OFF)}Please input a positive number.{effect(23)}")
            else:break
    step = frame/20
    pensize(frame*20)#large
    tcolor('#000')#         black
    forward(0)#                   background is generated
    pensize(0)#ewan it feels right
    penup()#even if it won't leave a mark
    right(90)#makes it face bottom
    goto(-frame*oddconstant*(int(255/color_depth)/255),frame*oddconstant*(int(255/color_depth)/255))#top left
    total_color = 0 #Color counter
    Screen().tracer(0) #screen will not update
    speed(0) #fastest
    for r in range(0,256,color_depth):#red new frame
        r2 = f"{hex(r)}"[2:4]
        if len(r2)==1:r2 = f"0{r2}"#forces 2 digits
        for g in range(0,256,color_depth):#green column
            g2 = f"{hex(g)}"[2:4]
            if len(g2)==1:g2 = f"0{g2}"#forces 2 digits
            for b in range(0,256,color_depth):#blue row
                b2 = f"{hex(b)}"[2:4]
                if len(b2)==1:b2 = f"0{b2}"#forces 2 digits
                fillcolor(f'#{r2}{g2}{b2}')
                begin_fill()
                for square in range(4):#square cell
                    forward(step)
                    left(90)
                end_fill()
                total_color +=1 #Color counter increase
                for i in range(3):
                    forward(step)
                    left(90)
                left(90)
            right(90)
            forward(step*(int(255/color_depth+1)))
            left(90)
            forward(step)
        left(135)#turtle cursor will not block the colors
        tcolor('#000')#turtle cursor will be invisible
        Screen().update()#new frame
        right(135)
        time.sleep((color_depth/255))
        goto(-frame*oddconstant*(int(255/color_depth)/255),frame*oddconstant*(int(255/color_depth)/255))#top left
    print(f"Total colors: {total_color} 【{round(total_color**(1/3))}³】")#Shows total number of colors generated
    input()#lets user stop program
    
Program_run()

"""This is unimportant since this is not a school activity
I wanted to make this program because i was reading stuff about "Color Depth" and I was inspired.

#personal use ignore this if someone else reads this
Colors used for the rgb that varies isn't canon, it is only used specifically for this program.
Colors used for title_color is canon and is now in the color set.
The new color function with 6 digits will be implemented in future activities but may be unused. It may also be deleted if so.
"""