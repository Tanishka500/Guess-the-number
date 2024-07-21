import tkinter as tk
import random

num = str(random.randrange(1000, 10000))
ctr = 0

def check_guess():
    global ctr, num
    guess = entry_guess.get()

    if not guess.isdigit() or len(guess) != 4:
        display_message("Error", "Please enter a valid 4 digit number.", "#800080")
        return

    ctr += 1
    count = sum(1 for i in range(4) if guess[i] == num[i])
    correct = ''.join(guess[i] if guess[i] == num[i] else 'X' for i in range(4))

    if guess == num:
        display_message("Congratulations", f"Correct! You guessed the number {num} in {ctr} tries.", "#800080")
        reset_game()
    else:
        display_message("Incorrect", f"Not quite. You got {count} digit(s) correct.\nCorrect digits: {correct}", "#800080")

def reset_game():
    global num, ctr
    num = str(random.randrange(1000, 10000))
    ctr = 0
    entry_guess.delete(0, tk.END)
    display_message("Game Reset", "Guess again!", "black")

def display_message(title, message, color):
    message_label.config(text=message, fg=color)

root = tk.Tk()
root.title("Guess the number")
root.geometry("500x400")
root.configure(bg='#D8BFD8')

label_heading = tk.Label(root, text="Guess the number", font=("Times", 20, "bold"), bg='#D8BFD8', fg='black')
label_heading.pack(pady=10)

label_instruction = tk.Label(root, text="Enter your guess (4 digits):", bg='#D8BFD8', font=("Times", 12))
label_instruction.pack()

entry_guess = tk.Entry(root, width=10)
entry_guess.pack(pady=5)

btn_guess = tk.Button(root, text="Guess", command=check_guess)
btn_guess.pack(pady=10)

message_label = tk.Label(root, text="", font=("Times", 12), bg='#D8BFD8')
message_label.pack()

root.mainloop()
