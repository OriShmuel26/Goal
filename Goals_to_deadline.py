import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from PIL import Image, ImageTk

def update_timer():
    today_date = datetime.now()
    time_remaining = deadline_date - today_date

    if time_remaining.total_seconds() <= 0:
        message_label.config(text="Time's up! Goal achieved.")
        progress_bar.stop()
        countdown_label.config(text="Time's up!")
        return

    seconds_remaining = int(time_remaining.total_seconds())
    minutes_remaining, seconds_remaining = divmod(seconds_remaining, 60)
    hours_remaining, minutes_remaining = divmod(minutes_remaining, 60)
    days_remaining, hours_remaining = divmod(hours_remaining, 24)

    remaining_text = f"{days_remaining} days, {hours_remaining:02d}:{minutes_remaining:02d}:{seconds_remaining:02d}"

    if days_remaining <= 7:
        message_label.config(text=f"Hurry up!", fg="yellow")
    elif days_remaining <= 365:
        message_label.config(text=f"Time remaining: {days_remaining} days, good luck", fg="white")
    else:
        message_label.config(text="Time remaining: more than a year!, have time", fg="green")

    progress_bar["value"] = 100 - (time_remaining.total_seconds() / total_seconds * 100)

    # Update the countdown label
    countdown_label.config(text=remaining_text)
    root.after(1000, update_timer)

#start tk
root = tk.Tk()
root.title("Goal Countdown Timer")
#background
root.configure(bg="#313335")
#lebel
label = tk.Label(root, text="Enter your goal and deadline (dd.mm.yyyy)",bg="#313335",fg="white")
label.pack()

image = Image.open("C:/Users/Ori Shmuel/PycharmProjects/Python project/My_Project/Converter_App/Goals.jpg")
image = image.resize((150, 150))  # size setting
photo = ImageTk.PhotoImage(image)

# set image
image_label = tk.Label(root, image=photo,bg="#313335")
image_label.pack()
image_label.photo = photo# for image dont stack/delete on run

input_frame = tk.Frame(root)
input_frame.pack()

goal_label = tk.Label(input_frame, text="Goal:",fg="white",bg="#313335")
goal_label.pack(side="left")
goal_entry = tk.Entry(input_frame)
goal_entry.pack(side="left")

deadline_label = tk.Label(input_frame, text="Deadline:",fg="white",bg="#313335")
deadline_label.pack(side="left")
deadline_entry = tk.Entry(input_frame)
deadline_entry.pack(side="left")

start_button = tk.Button(root, text="Start", command=update_timer)
start_button.pack()

# Label for display message
message_label = tk.Label(root, text="", bg="#313335")
message_label.pack()

# Progress Bar
progress_bar = ttk.Progressbar(root, mode="determinate", length=300)
progress_bar.pack()

# Label for display countdown
countdown_label = tk.Label(root, text="",fg="white",bg="#313335")
countdown_label.pack()

# value initial time for Progress Bar
total_seconds = 0

def start_countdown():
    global deadline_date, total_seconds
    deadline_date = datetime.strptime(deadline_entry.get(), "%d.%m.%Y")
    today_date = datetime.now()
    time_remaining = deadline_date - today_date
    total_seconds = int(time_remaining.total_seconds())
    update_timer()
    progress_bar.start()

start_button.config(command=start_countdown)
#close soft ware
root.mainloop()