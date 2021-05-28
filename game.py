from main import roll_d6
from tkinter import *
import time

window = Tk()
window.title('Greedy Pig')
window.geometry('420x420')
# window.resizable(False, False)



player_score = 0
holdings = 0
comp_score = 0
comp_holdings = 0
num_turns = 10

def reset():
    global player_score
    global holdings
    global comp_score
    global comp_holdings
    global num_turns

    player_score = 0
    holdings = 0
    comp_score = 0
    comp_holdings = 0
    num_turns = 10
    window.update()

    trns_left_label.config(text=num_turns)

    comp_roll.config(text=0)
    comp_turn.config(text=0)
    comp_hold.config(text=0)

    player_roll.config(text=0)
    player_turn.config(text=0)
    player_hold.config(text=0)

    hold_button['state'] = 'normal'
    play_button['state'] = 'normal'


def check_finish():
    trns_left_label.config(text=num_turns)
    if num_turns == 0:
        if comp_holdings > holdings:
            print('ai won')
        else:
            print('you won')

def roll():
    play_button['state'] = 'disabled'
    hold_button['state'] = 'normal'
    global player_score
    comp_roll.config(text=0)
    roll = roll_d6()
    player_roll.config(text=roll)
    if roll == 1:
        hold_button['state'] = 'disabled'
        player_score = 0
        player_turn.config(text=player_score)



        comp_ai_turn()
        player_roll.config(text=0)
        return
    player_score += roll
    player_turn.config(text=player_score)

    play_button['state'] = 'normal'


def holder():
    hold_button['state'] = 'disabled'
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
    reset_button['state'] = 'disabled'
    global comp_score
    global num_turns
    for i in range(5):
        roll = comp_ai_roll()
        comp_roll.config(text=roll)
        window.update()
        time.sleep(1)
        if roll == 1:
            comp_score = 0
            comp_turn.config(text=0)

            time.sleep(1)
            window.update()
            comp_roll.config(text=0)
            num_turns -= 1
            check_finish()
            play_button['state'] = 'normal'
            reset_button['state'] = 'normal'

            return
        else:
            # comp_roll.config(text=roll)
            comp_score += roll



            comp_turn.config(text=comp_score)
            window.update()
            time.sleep(1)
            if comp_score >= 21:

                comp_ai_holder()
                play_button['state'] = 'normal'
                reset_button['state'] = 'normal'
                return

    comp_ai_holder()
    play_button['state'] = 'normal'
    reset_button['state'] = 'normal'


def comp_ai_holder():
    global comp_holdings
    global comp_score
    global num_turns
    comp_holdings += comp_score
    comp_hold.config(text=comp_holdings)
    comp_score = 0
    comp_turn.config(text=comp_score)

    comp_roll.config(text=0)
    window.update()
    num_turns -= 1
    check_finish()

curr_roll = Label(text='Rolled').grid(row=0, column=2)
turn = Label(text='Turn').grid(row=0, column=3)
hold = Label(text='Holdings').grid(row=0, column=4)
turns_left = Label(text='Turns Left').grid(row=0, column=5)

trns_left_label = Label()
trns_left_label.grid(row=1, column=5)
trns_left_label.config(text=num_turns)

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
reset_button = Button(text='Reset', command=reset)
reset_button.grid(row=4, column=6)

window.mainloop()

