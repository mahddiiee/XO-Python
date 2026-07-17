import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("XO Game")

turn = "X"

btns = []

wins = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]


def restart():
    global turn

    for b in btns:
        b["text"] = ""

    turn = "X"


def check():

    for w in wins:

        a = btns[w[0]]["text"]
        b = btns[w[1]]["text"]
        c = btns[w[2]]["text"]

        if a != "" and a == b and b == c:
            messagebox.showinfo("Game", a + " Wins")
            restart()
            return True

    full = True

    for x in btns:
        if x["text"] == "":
            full = False

    if full:
        messagebox.showinfo("Game", "Draw")
        restart()
        return True

    return False


def click(i):

    global turn

    if btns[i]["text"] != "":
        return

    btns[i]["text"] = turn

    if check():
        return

    if turn == "X":
        turn = "O"
    else:
        turn = "X"


for i in range(9):

    b = tk.Button(
        window,
        text="",
        width=5,
        height=2,
        font=("Arial",20),
        command=lambda i=i: click(i)
    )

    b.grid(row=i//3, column=i%3)

    btns.append(b)


r = tk.Button(
    window,
    text="Reset",
    command=restart
)

r.grid(row=3, column=0, columnspan=3, pady=10)

window.mainloop()