import random
from tkinter import *

# Function to determine the winner
def play_game(user_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    
    # Updating the computer's choice label
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    
    # Determining the winner
    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="You Win!")
    else:
        result_label.config(text="Computer Wins!")

# Creating the main window
root = Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x400")

# Heading Label
heading_label = Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 16))
heading_label.pack(pady=20)

# Buttons for user choices
rock_button = Button(root, text="Rock", width=15, command=lambda: play_game("Rock"))
rock_button.pack(pady=10)

paper_button = Button(root, text="Paper", width=15, command=lambda: play_game("Paper"))
paper_button.pack(pady=10)

scissors_button = Button(root, text="Scissors", width=15, command=lambda: play_game("Scissors"))
scissors_button.pack(pady=10)

# Label to display computer's choice
computer_choice_label = Label(root, text="", font=("Arial", 12))
computer_choice_label.pack(pady=20)

# Label to display the result of the game
result_label = Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=20)

# Main loop to run the GUI
root.mainloop()



















