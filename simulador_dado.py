from re import S
from secrets import choice
from matplotlib import container
import pyautogui as pg
import random
from tkinter import *
from Functions import *
from PIL import Image

# Config window
root = Tk()
root.title('Game Mater Play Dices')
root.config(bg='#880015')
root.iconbitmap(
    r"img\bitmap_dice.ico")
root.geometry(center(root, 500, 350))
root.resizable(False, False)
# //////////////////////////////////////////////////////////END
# Functions


def play_dice():
    drawn = random.choice(lista_numeros)

    if drawn == '1':
        lb_dice01.grid()
        lb_dice02.grid_forget()
        lb_dice03.grid_forget()
        lb_dice04.grid_forget()
        lb_dice05.grid_forget()
        lb_dice06.grid_forget()
        lb_dice_init.grid_forget()
    elif drawn == '2':
        lb_dice02.grid()
        lb_dice01.grid_forget()
        lb_dice03.grid_forget()
        lb_dice04.grid_forget()
        lb_dice05.grid_forget()
        lb_dice06.grid_forget()
        lb_dice_init.grid_forget()
    elif drawn == '3':
        lb_dice03.grid()
        lb_dice01.grid_forget()
        lb_dice02.grid_forget()
        lb_dice04.grid_forget()
        lb_dice05.grid_forget()
        lb_dice06.grid_forget()
        lb_dice_init.grid_forget()
    elif drawn == '4':
        lb_dice04.grid()
        lb_dice01.grid_forget()
        lb_dice03.grid_forget()
        lb_dice02.grid_forget()
        lb_dice05.grid_forget()
        lb_dice06.grid_forget()
        lb_dice_init.grid_forget()
    elif drawn == '5':
        lb_dice05.grid()
        lb_dice01.grid_forget()
        lb_dice03.grid_forget()
        lb_dice04.grid_forget()
        lb_dice02.grid_forget()
        lb_dice06.grid_forget()
        lb_dice_init.grid_forget()
    elif drawn == '6':
        lb_dice06.grid()
        lb_dice01.grid_forget()
        lb_dice03.grid_forget()
        lb_dice04.grid_forget()
        lb_dice05.grid_forget()
        lb_dice02.grid_forget()
        lb_dice_init.grid_forget()


# Variables
lista_numeros = ['1', '2', '3', '4', '5', '6']
img_dice_init = PhotoImage(
    file='img\dice_init.png')
img_dice01 = PhotoImage(
    file='img\dice_01.png')
img_dice02 = PhotoImage(
    file='img\dice_02.png')
img_dice03 = PhotoImage(
    file='img\dice_03.png')
img_dice04 = PhotoImage(
    file='img\dice_04.png')
img_dice05 = PhotoImage(
    file='img\dice_05.png')
img_dice06 = PhotoImage(
    file='img\dice_06.png')
# //////////////////////////////////////////////////////////END
# Container
fr_container01 = Frame(
    root
)
fr_container02 = Frame(
    root,
    height=250,
    bg='#880015'
)
fr_container03 = Frame(
    root
)
fr_container01.pack()
fr_container02.pack()
fr_container03.pack()
# //////////////////////////////////////////////////////////END
# Labels container 01
lb_title = Label(
    fr_container01,
    text='Welcome the dice game',
    font='Verdana 20 bold',
    bg='#880015',
    fg='white'

)
lb_title.pack()
# //////////////////////////////////////////////////////////END
# Labels container 02
lb_dice_init = Label(
    fr_container02,
    image=img_dice_init,
    border=0
)
lb_dice01 = Label(
    fr_container02,
    image=img_dice01,
    border=0
)
lb_dice02 = Label(
    fr_container02,
    image=img_dice02,
    border=0,
)
lb_dice03 = Label(
    fr_container02,
    image=img_dice03,
    border=0
)
lb_dice04 = Label(
    fr_container02,
    image=img_dice04,
    border=0
)
lb_dice05 = Label(
    fr_container02,
    image=img_dice05,
    border=0
)
lb_dice06 = Label(
    fr_container02,
    image=img_dice06,
    border=0
)
lb_dice_init.grid()
# //////////////////////////////////////////////////////////END
# Labels container 02
bt_buttonPlay = Button(
    fr_container03,
    text='Play dice',
    font='Verdana 11 bold',
    fg='black',
    bg='yellow',
    activebackground='#DFAD00',
    activeforeground='grey',
    width=20,
    height=2,
    border=0,
    command=play_dice
)
bt_buttonPlay.pack()
# //////////////////////////////////////////////////////////END
root.mainloop()
