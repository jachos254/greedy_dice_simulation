from main import roll_d6
from tkinter import *
import time

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
holdings = 0
comp_score = 0
comp_holdings = 0

def roll():
    global player_score
    comp_roll.config(text=0)
    roll = roll_d6()
    player_roll.config(text=roll)
    if roll == 1:
        player_score = 0
        player_turn.config(text=player_score)



        comp_ai_turn()
        player_roll.config(text=0)
        return
    player_score += roll
    player_turn.config(text=player_score)

# #setting 0s between actions
# def reset_player():
#     player_score = 0
#
#     player_roll.config(text=player_score)
#
#
# #setting 0s between actions
# def reset_comp():
#     comp_score = 0
#
#     comp_roll.config(text=comp_score)


def holder():
    global holdings
    global player_score
    player_roll.config(text=0)
    holdings += player_score
    player_hold.config(text=holdings)
    player_score = 0
    player_turn.config(text=player_score)
    comp_ai_turn()

def comp_ai_roll():
    roll = roll_d6()
    comp_roll.config(text=roll)
    return roll

def comp_ai_turn():
    global comp_score

    roll = comp_ai_roll()
    comp_roll.config(text=roll)
    window.update()
    time.sleep(1)
    if roll == 1:
        comp_turn.config(text=0)
        time.sleep(1)
        comp_roll.config(text=0)
        return
    else:
        comp_roll.config(text=roll)
        comp_score += roll
        comp_turn.config(text=comp_score)



    roll = comp_ai_roll()
    comp_roll.config(text=roll)
    window.update()
    time.sleep(1)
    if roll == 1:
        comp_turn.config(text=0)
        time.sleep(1)
        comp_roll.config(text=0)
        return
    else:
        comp_roll.config(text=roll)
        comp_score += roll
        comp_turn.config(text=comp_score)



    roll = comp_ai_roll()
    comp_roll.config(text=roll)
    window.update()
    time.sleep(1)
    if roll == 1:

        comp_turn.config(text=0)
        time.sleep(1)
        comp_roll.config(text=0)
        return
    else:
        comp_roll.config(text=roll)
        comp_score += roll
        comp_turn.config(text=comp_score)

    comp_ai_holder()

def comp_ai_holder():
    global comp_holdings
    global comp_score
    comp_holdings += comp_score
    comp_hold.config(text=comp_holdings)
    comp_score = 0
    comp_turn.config(text=comp_score)

    comp_roll.config(text=0)

curr_roll = Label(text='Rolled').grid(row=0, column=2)

turn = Label(text='turn').grid(row=0, column=3)
hold = Label(text='Holdings').grid(row=0, column=4)

comp = Label(text='AI').grid(row=1, column=1)
comp_roll = Label()
comp_roll.grid(row=1, column=2)
comp_roll.config(text=0)
comp_turn = Label()
comp_turn.grid(row=1, column=3)
comp_turn.config(text=0)
comp_hold = Label()
comp_hold.grid(row=1, column=4)
comp_hold.config(text=0)

player = Label(text='Pl4yer').grid(row=2, column=1)
player_roll = Label()
player_roll.grid(row=2, column=2)
player_roll.config(text=0)
player_turn = Label()
player_turn.grid(row=2, column=3)
player_turn.config(text=0)
player_hold = Label()
player_hold.grid(row=2, column=4)
player_hold.config(text=0)

play_button = Button(text='Roll', bg='green', command=roll)
play_button.grid(row=3, column=2)
hold_button = Button(text='Hold', bg='red', command=holder)
hold_button.grid(row=3, column=4)


window.mainloop()

