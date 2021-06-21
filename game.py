from functions import roll_d6
from tkinter import *
import time

grey = '#74b9ff'
white = '#2d3436'
green = '#00b894'
red = '#d63031'

window = Tk()
window.config(bg=grey)
window.title('Greedy_Pig')
window.geometry('586x192')
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

    hold_button['state'] = 'disabled'
    play_button['state'] = 'normal'

    comp_win.config(text='')
    player_win.config(text='')


def check_finish():
    trns_left_label.config(text=num_turns)
    if num_turns == 0:
        if comp_holdings > holdings:
            comp_win.config(text='Winner!')
            play_button['state'] = 'disabled'
            hold_button['state'] = 'disabled'
        else:
            player_win.config(text='Winner!')
            play_button['state'] = 'disabled'
            hold_button['state'] = 'disabled'


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
        time.sleep(1)
        return
    player_score += roll
    player_turn.config(text=player_score)

    play_button['state'] = 'normal'


def holder():
    hold_button['state'] = 'disabled'
    play_button['state'] = 'disabled'
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
            play_button['state'] = 'normal'
            reset_button['state'] = 'normal'
            check_finish()


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
    play_button['state'] = 'normal'
    reset_button['state'] = 'normal'
    check_finish()


font = ('Sans Serif',18)

curr_roll = Label(text='Rolled', bg=grey, fg=white, font=font, relief='groove', width=6).grid(row=0, column=2)
turn = Label(text='Turn', bg=grey, fg=white, font=font, relief='groove', width=6).grid(row=0, column=3)
hold = Label(text='Holdings', bg=grey, fg=white, font=font, relief='groove', width=7).grid(row=0, column=4)
turns_left = Label(text='Turns Left', bg=grey, fg=white, font=font, relief='groove', width=8).grid(row=0, column=5)

trns_left_label = Label()
trns_left_label.grid(row=1, column=5)
trns_left_label.config(text=num_turns, bg=grey, fg=white, font=font, relief='sunken', width=8)

comp = Label(text='AI', bg=grey, fg=white, font=font, relief='groove', width=6).grid(row=1, column=1)
comp_roll = Label()
comp_roll.grid(row=1, column=2)
comp_roll.config(text=0, bg=grey, fg=white, font=font, relief='sunken', width=6)
comp_turn = Label()
comp_turn.grid(row=1, column=3)
comp_turn.config(text=0, bg=grey, fg=white, font=font, relief='sunken', width=6)
comp_hold = Label()
comp_hold.grid(row=1, column=4)
comp_hold.config(text=0, bg=grey, fg=white, font=font, relief='sunken', width=7)
comp_win = Label()
comp_win.config(font=font, bg=grey, fg=white)
comp_win.grid(row=1, column=6)

player = Label(text='Pl4yer', bg=grey, fg=white, font=font, relief='groove', width=6).grid(row=2, column=1)
player_roll = Label()
player_roll.grid(row=2, column=2)
player_roll.config(text=0, bg=grey, fg=white, font=font, relief='sunken', width=6)
player_turn = Label()
player_turn.grid(row=2, column=3)
player_turn.config(text=0, bg=grey, fg=white, font=font, relief='sunken', width=6)
player_hold = Label()
player_hold.grid(row=2, column=4)
player_hold.config(text=0, bg=grey, fg=white, font=font, relief='sunken', width=7)
player_win = Label()
player_win.config(font=font, bg=grey, fg=white)
player_win.grid(row=2, column=6)

play_button = Button(text='Roll', bg=green, fg=white, font = font, command=roll)
play_button.grid(row=3, column=2)
hold_button = Button(text='Hold', bg=red, fg=white, font=font, command=holder)
hold_button.grid(row=3, column=4)
hold_button['state'] = 'disabled'
reset_button = Button(text='Reset', bg=grey, fg=white, font=font, command=reset, width=6)
reset_button.grid(row=4, column=6)

window.iconbitmap('nose.ico')
window.mainloop()

