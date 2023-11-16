import tkinter
from tkinter import *
from tkinter import ttk
import pyperclip

root = Tk()
root.title("Disappearing Text Writing App")
root.geometry("503x450")

# Set the text field
text_field = Text(root, width=50, height=25)
text_field.grid(column=0, row=0, padx=10, pady=10, rowspan=2)

# Set time value and IntVar for displaying the time
time_value = 5
time_left = IntVar(root)
time_left.set(time_value)

# set variable for the countdown timer that avoids starting more than 1 timer
current_countdown = None


def countdown(count):
    """Performs countdown for given time (seconds)"""
    global current_countdown
    if count > -1:
        time_left.set(count)
        current_countdown = root.after(1000, countdown, count-1)
    # Delete the text from the text field or change the colour of the background
    if count == 0:
        text_field.delete("1.0", END)
    elif count <= 1:
        text_field.config(background="red")
    elif count <= 2:
        text_field.config(background="yellow")


def start_by_typing(event):
    """Starts countdown by typing."""
    text_field.config(background="white")
    # Starts timer
    if current_countdown is not None:
        root.after_cancel(current_countdown)

    time_left.set(time_value)
    countdown(time_left.get())


def copy_text():
    pyperclip.copy(text_field.get("1.0", END))


# set label for displaying time left
ttk.Label(root, textvariable=time_left).grid(column=1, row=0, sticky=N, pady=15)

# set copy button for copying the text
copy_button = tkinter.Button(root, width=3, height=20, text="COPY", command=copy_text)
copy_button.grid(column=1, row=1, padx=10)

# Bind events to the text_field
text_field.bind("<KeyRelease>", start_by_typing)

root.mainloop()
