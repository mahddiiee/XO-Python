import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in winning_combinations:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            winner = buttons[combo[0]]["text"]
            messagebox.showinfo("game over", f"player {winner} win")
            reset_game()
            return True
    if all(buttons[i]["text"] != "" for i in range(9)):
        messagebox.showinfo("game over", "mosaavi")
        reset_game()
        return True
    return False

def button_click(index):
    if buttons[index]["text"] == "" and not check_winner():
        buttons[index]["text"] = current_player.get()
        if not check_winner():
            if current_player.get() == "X":
                current_player.set("O")
            else:
                current_player.set("X")

def reset_game():
    for button in buttons:
        button["text"] = ""
    current_player.set("X")

root = tk.Tk()
root.title("پروژه برنامه نویسی")

current_player = tk.StringVar()
current_player.set("X")

buttons = []
winning_combinations = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
]

for i in range(9):
    button = tk.Button(root, text="", font=('Arial', 20), width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=('Arial', 12))
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()