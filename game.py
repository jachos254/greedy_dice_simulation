from main import roll_d6
from tkinter import *

window = Tk()
window.title('Greedy Pig')
window.geometry('420x420')
# window.resizable(False, False)


# def computer():
#     roll = roll_d6()
#     label.config(text=roll)
#
# def player():
#     roll = roll_d6()
#     label_2.config(text=roll)


player_score = 0
def roll():
    global player_score
    roll = roll_d6()
    player_score += roll
    player_roll.config(text=roll)
    player_turn.config(text=player_score)
    print(roll)

curr_roll = Label(text='Rolled').grid(row=0, column=2)

turn = Label(text='turn').grid(row=0, column=3)
hold = Label(text='Holdings').grid(row=0, column=4)

comp = Label(text='AI').grid(row=1, column=1)
comp_roll = Label().grid(row=1, column=2)
comp_turn = Label().grid(row=1, column=3)
comp_hold = Label().grid(row=1, column=4)

player = Label(text='Pl4yer').grid(row=2, column=1)
player_roll = Label()
player_roll.grid(row=2, column=2)
player_turn = Label()
player_turn.grid(row=2, column=3)
player_hold = Label().grid(row=2, column=4)

play = Button(text='Roll', bg='green', command=roll)
play.grid(row=3, column=2)
hold = Button(text='Hold', bg='red').grid(row=3, column=4)

window.mainloop()