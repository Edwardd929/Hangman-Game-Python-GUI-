import tkinter as tk
from tkinter import messagebox
import random
from collections import Counter

# Hangman game setup
someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split(' ')
word = random.choice(someWords)
letterGuessed = ''
chances = len(word) + 2
correct = 0
flag = 0

# GUI Setup
root = tk.Tk()
root.title("Hangman Game - Guess the Fruit!")

# Display Word Function
def display_word():
    display = ''
    for char in word:
        if char in letterGuessed:
            display += char + ' '
        else:
            display += '_ '
    word_label.config(text=display)

# Guess Function
def guess():
    global chances, letterGuessed, correct, flag
    guess = letter_entry.get().lower()
    letter_entry.delete(0, tk.END)

    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning('Invalid', 'Enter only a SINGLE letter')
        return
    if guess in letterGuessed:
        messagebox.showinfo('Duplicate', 'You have already guessed that letter')
        return

    if guess in word:
        k = word.count(guess)
        letterGuessed += guess * k
        correct += k
        display_word()
        if Counter(letterGuessed) == Counter(word):
            messagebox.showinfo('Hangman', 'Congratulations, You won!')
            flag = 1
    else:
        chances -= 1
        chances_label.config(text=f"Chances left: {chances}")

    if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
        messagebox.showinfo('Hangman', f'You lost! The word was {word}')
        flag = 1

    if flag:
        play_again = messagebox.askyesno('Hangman', 'Play Again?')
        if play_again:
            restart_game()
        else:
            root.quit()

# Restart Game Function
def restart_game():
    global word, letterGuessed, chances, correct, flag
    word = random.choice(someWords)
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    display_word()
    chances_label.config(text=f"Chances left: {chances}")

# GUI Components
root.configure(bg='lightblue')  # Setting a background color

# Main Frame for Game Display
main_frame = tk.Frame(root, bg='lightblue', padx=10, pady=10)
main_frame.pack(pady=20)

# Display Word in a separate frame for better control
display_frame = tk.Frame(main_frame, bg='lightblue')
display_frame.pack(pady=10)

word_label = tk.Label(display_frame, text='', font=('Helvetica', 24, 'bold'), bg='lightblue')
word_label.pack()

# Chances and Entry in their own frame
input_frame = tk.Frame(main_frame, bg='lightblue')
input_frame.pack(pady=10)

chances_label = tk.Label(input_frame, text=f"Chances left: {chances}", font=('Helvetica', 16), bg='lightblue')
chances_label.grid(row=0, column=0, padx=10)

letter_entry = tk.Entry(input_frame, justify='center', width=5, font=('Helvetica', 24))
letter_entry.grid(row=0, column=1, padx=10)

# Buttons in their own frame
button_frame = tk.Frame(main_frame, bg='lightblue')
button_frame.pack(pady=10)

guess_button = tk.Button(button_frame, text='Guess', command=guess, font=('Helvetica', 18), width=20)
guess_button.grid(row=0, column=0, padx=10)

restart_button = tk.Button(button_frame, text='Restart', command=restart_game, font=('Helvetica', 18), width=20)
restart_button.grid(row=0, column=1, padx=10)

display_word()  # Initial display

root.mainloop()
