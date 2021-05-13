from main import roll_d6
import tkinter

window = tkinter.Tk()
window.title('Greedy Pig')
window.geometry('420x420')
window.resizable(False, False)


def computer():
    roll = roll_d6()
    label.config(text=roll)

def player():
    roll = roll_d6()
    label_2.config(text=roll)

label = tkinter.Label(window)
label.grid(row=0, column=1)

label_2 = tkinter.Label(window)
label_2.grid(row=2, column=1)

play = tkinter.Button(window, text = 'roll', command = player)
play.grid(row=1, column=1)

computer()

window.mainloop()