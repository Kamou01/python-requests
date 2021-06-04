import requests
from tkinter import Tk, Message, Button, messagebox


def get_chucks_joke():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        data = response.json()
        return data["value"]
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Error", "no internet connection")


def get_new_joke():
    chuck_joke.configure(text=get_chucks_joke())


gui = Tk()
gui.geometry("400x400")
chuck_joke = Message(gui, text=get_chucks_joke())
chuck_joke.pack()


recall_btn = Button(gui, text="These jokes kinda suck doe", command=get_new_joke)
recall_btn.pack(side="bottom")

gui.mainloop()
