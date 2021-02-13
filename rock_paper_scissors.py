from tkinter import *
import random
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.iconbitmap('rps.ico')
root.title("Rock-Paper-Scissors")
root.config(bg="white")
root.geometry("500x700")

rock = ImageTk.PhotoImage(Image.open("rock (1).png"))
paper = ImageTk.PhotoImage(Image.open("paper (1).png"))
scissors = ImageTk.PhotoImage(Image.open("scissors (1).png"))

# dodaje obrazki do listy
image_list = random.choice([rock, paper, scissors])

# pokazuje obraz po uruchomieniu programu
image_label = Label(root, image=image_list, bd=0)
image_label.pack(pady=20)


# Funkcja spin
def spin():
    # wybiera losowo obrazek
    image_list = random.choice([rock, paper, scissors])

    image_label.config(image=image_list)

    if user_choice.get() == "rock":
        user_choice_value = "rock"
    elif user_choice.get() == "paper":
        user_choice_value = "paper"
    elif user_choice.get() == "scissors":
        user_choice_value = "scissors"

    # okresla ktowygral kto nie
    if user_choice_value == "rock":
        if image_list == rock:
            win_lose_label.config(text="It's a tie! Spin Again...")
        elif image_list == paper:
            win_lose_label.config(text="Paper beats rock, you lose")
        elif image_list == scissors:
            win_lose_label.config(text="Rock smashes scissors! You win")

    if user_choice_value == "paper":
        if image_list == paper:
            win_lose_label.config(text="It's a tie! Spin Again...")
        elif image_list == rock:
            win_lose_label.config(text="Paper beats rock, you win")
        elif image_list == scissors:
            win_lose_label.config(text="Scissors cut paper! You lose")

    if user_choice_value == "scissors":
        if image_list == rock:
            win_lose_label.config(text="Rock smashes scissors! you lose...")
        elif image_list == paper:
            win_lose_label.config(text="Scissors cut paper, you won")
        elif image_list == scissors:
            win_lose_label.config(text="It's a tie! Spin Again...")


# Twoj wybor
user_choice = ttk.Combobox(root, value=("rock", "paper", "scissors"))
user_choice.current(0)
user_choice.pack(pady=20)

# Zagraj = Spin Button
spin_button = Button(root, text="Spin", command=spin)
spin_button.pack(pady=10)

# Przycisk do zamkniecia programu
wyjdz_button = Button(root, text="Quit", command=root.destroy)
wyjdz_button.pack()

# Etykieta pokazujaca czy wygrales czy nie
win_lose_label = Label(root, text="", font=("Helvetica", 18), bg="white")
win_lose_label.pack(pady=50)


root.mainloop()