from tkinter import *
from PIL import Image,ImageTk
from random import randint
#main window and title
# name=str(input())
root=Tk()
root.title("SNAKE WATER GUN")
root.configure(background="pink")
#picture 
snake_img=ImageTk.PhotoImage(Image.open("snake-user.png"))
water_img=ImageTk.PhotoImage(Image.open("water-user.png"))
gun_img=ImageTk.PhotoImage(Image.open("gun-user.png"))
snake_comp_img=ImageTk.PhotoImage(Image.open("snake.png"))
water_comp_img=ImageTk.PhotoImage(Image.open("water.png"))
gun_comp_img=ImageTk.PhotoImage(Image.open("gun.png"))
#inserting images
user_label=Label(root,image=snake_img,bg="black")
comp_label=Label(root,image=snake_comp_img,bg="black")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)
#scores -> p_score = playerscore
p_score=Label(root,text=0,font=100,bg="#FFC0CB",fg="#3D76E0")
c_score=Label(root,text=0,font=100,bg="#FFC0CB",fg="#3D76E0")
c_score.grid(row=1,column=1)
p_score.grid(row=1,column=3)
#indicators--> user side and comp side
user_indicator=Label(root,font=50,text="USER",bg="#FFC0CB",fg="#0000FF").grid(row=0,column=3)
comp_indicator=Label(root,font=50,text="COMPUTER",bg="#FFC0CB",fg="#3D76E0").grid(row=0,column=1)
#buttons
snake=Button(root,width=20,height=2,text="SNAKE",bg="#adff2f",fg="#00FF00",command=lambda:updatepic("SNAKE")).grid(row=2,column=1)
gun=Button(root,width=20,height=2,text="GUN",bg="#FFC0CB",fg="#3D76E0",command=lambda:updatepic("GUN")).grid(row=2,column=2)
water=Button(root,width=20,height=2,text="WATER",bg="#FFC0CB",fg="#3D76E0",command=lambda:updatepic("WATER")).grid(row=2,column=3)
quit=Button(root,width=20,height=2,text="QUIT",bg="#FFC0CB",fg="#3D76E0",command=root.destroy).grid(row=4,column=2)
#MESSAGES
msg=Label(root,font=50,bg="#FFC0CB",fg="#3D76E0")
msg.grid(row=3,column=2)
#update winner:
def updatemsg(x):
    msg['text']=x
#update user code
def updateuserscore():
    score=int(p_score['text'])
    score+=1
    p_score['text']=str(score)
#update comp score
def updatecompscore():
    score=int(c_score['text'])
    score+=1
    c_score['text']=str(score)
#picture update when clicked
choices=["SNAKE","GUN","WATER"]
def updatepic(x):
    #comuter
    comp_chioce=choices[randint(0,2)]
    if comp_chioce=="SNAKE":
        comp_label.configure(image=snake_comp_img)
    elif comp_chioce=="GUN":
        comp_label.configure(image=gun_comp_img)
    else:
        comp_label.configure(image=water_comp_img)
    #user
    if x=="SNAKE":
        user_label.configure(image=snake_img)
    elif x=="GUN":
        user_label.configure(image=gun_img)
    else:
        user_label.configure(image=water_img)
    checkwin(x,comp_chioce)
#WINNER
def checkwin(player,comp):
    if player==comp:
        updatemsg("Its a tie!!!")
    elif player=="SNAKE":
        if comp=="GUN":
            updatemsg("YOU LOOSE")
            updatecompscore()
        else:
            updatemsg("YOU WIN")
            updateuserscore()
    elif player=="WATER":
        if comp=="SNAKE":
            updatemsg("YOU LOOSE")
            updatecompscore()
        else:
            updatemsg("YOU WIN")
            updateuserscore()
    elif player=="GUN":
        if comp=="WATER":
            updatemsg("YOU LOOSE")
            updatecompscore()
        else:
            updatemsg("YOU WIN")
            updateuserscore()
    else:
        pass
root.mainloop()