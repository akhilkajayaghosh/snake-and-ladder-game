import tkinter as tk
from PIL import ImageTk,Image 
import random

root=tk.Tk()
root.geometry("1000x675")
root.title("Snake and Ladder")
root.configure(bg="#BFBFEF")
F1=tk.Frame(root,width=1200,height=800,relief='raised',bg='#BFBFEF')
F1.place(x=0,y=0)

img1=ImageTk.PhotoImage(Image.open("images\snake-ladder.jpg"))
Lab=tk.Label(F1,image=img1)
Lab.place(x=0,y=0)

player_1=tk.Canvas(root,height=40,width=40)
player_1.create_oval(10,10,40,40,fill='blue')

player_2=tk.Canvas(root,height=40,width=40)
player_2.create_oval(10,10,40,40,fill='red')
turn=1
Dice=[]
index={}
pos1=None
pos2=None
ladder={1:38,4:14,9:31,21:42,28:84,51:67,71:91,80:100}
snake={98:79,95:75,93:73,87:24,64:60,62:19,54:34,17:7}

def start():
    global img2
    global b1,b2
    b1.place(x=800,y=400)
    b2.place(x=800,y=500)
    b1.configure(state='normal')
    b2.configure(state='disabled')  
    b3=tk.Button(root,text="EXIT",height=3,width=12,fg='white',bg='darkred',activebackground='lightgrey',font=('cursive',14,'bold'),command=exit)
    b3.place(x=800,y=20)
    b5=tk.Button(root,text="RESTART",height=3,width=12,fg='white',bg='green',activebackground='lightgrey',font=('cursive',14,'bold'),command=restart)
    b5.place(x=800,y=120)
    img2=Image.open("images\dice1.jpeg")
    img2=img2.resize((82,82))
    img2=ImageTk.PhotoImage(img2)
    b4=tk.Button(root,image=img2,height=80,width=80)
    b4.place(x=800,y=300)
def exit():
    root.destroy()

def reset():
    global player_1,player_2
    global pos1,pos2
    player_1.place(x=20,y=630)
    player_2.place(x=70,y=630)
    pos1=0
    pos2=0

def load_dice():
    global Dice
    names=["1.png","2.png","3.png","4.png","5.png","6.png"]
    for i in names:
        img=Image.open('images/'+i)
        img=img.resize((65,65))
        img=ImageTk.PhotoImage(img)
        Dice.append(img)

def ladder_check(turn):
    global pos1,pos2
    f=0
    if turn==1:
        if pos1 in ladder:
            pos1=ladder[pos1]
            f=1
    else:
        if pos2 in ladder:
            pos2=ladder[pos2]
            f=1
    return f

def snake_check(turn):
    global pos1,pos2
    if turn==1:
        if pos1 in snake:
            pos1=snake[pos1]
    else:
        if pos2 in snake:
            pos2=snake[pos2]
def roll_dice():
    global Dice
    global turn
    global b1,b2
    global pos1,pos2
    r=random.randint(1,6)
    b4=tk.Button(root,image=Dice[r-1],height=80,width=80)
    b4.place(x=800,y=300)
    lad=0
    if(turn==1):
        if(pos1+r)<=100:
            pos1=pos1+r
        lad=ladder_check(turn)
        snake_check(turn)
        move_dice(turn,pos1)
        if(r!=6 and lad!=1):
            turn=2
            b1.configure(state='disabled')
            b2.configure(state='normal')
    else:
        if(pos2+r)<=100:
            pos2=pos2+r
        lad=ladder_check(turn)
        snake_check(turn)
        move_dice(turn,pos2)
        if(r!=6 and lad!=1):
            turn=1
            b1.configure(state='normal')
            b2.configure(state='disabled')
    is_winner()
def restart():
    global turn
    turn=1
    reset()
    start()
def is_winner():
    global pos1,pos2
    if pos1==100:
        msg="Player-1 is winner"
        Labb=tk.Label(root,text=msg,height=2,width=20,bg='green',font=('cursive',30,'bold'))
        Labb.place(x=300,y=300)
        reset()
    elif pos2==100:
        msg="Player-2 is winner"
        Labb=tk.Label(root,text=msg,height=2,width=20,bg='red',font=('cursive',30,'bold'))
        Labb.place(x=300,y=300)
        reset()

    
def move_dice(turn,r):
    global player_1,player_2
    global index
    if(turn==1):
        player_1.place(x=index[r][0],y=index[r][1])
    else:
        player_2.place(x=index[r][0],y=index[r][1])

def get_index():
    num=[100,99,98,97,96,95,94,93,92,91,81,82,83,84,85,86,87,88,89,90,80,79,78,77,76,75,74,73,72,71,61,62,63,64,65,66,67,68,69,70,60,59,58,57,56,55,54,53,52,51,41,42,43,44,45,46,47,48,49,50,40,39,38,37,36,35,34,33,32,31,21,22,23,24,25,26,27,28,29,30,20,19,18,17,16,15,14,13,12,11,1,2,3,4,5,6,7,8,9,10]
    row=12
    i=0
    for x in range(1,11):
        col=12
        for y in range(1,11):
            index[num[i]]=(col,row)
            i=i+1
            col=col+60
        row=row+60
b1=tk.Button(root,text="Player-1",height=3,width=8,fg='blue',bg='cyan',font=('cursive',14,'bold'),activebackground='lightgrey',command=roll_dice)
b2=tk.Button(root,text="Player-2",height=3,width=8,fg='red',bg='orange',font=('cursive',14,'bold'),activebackground='lightgrey',command=roll_dice) 
reset()
load_dice()
get_index()
start()
root.mainloop()