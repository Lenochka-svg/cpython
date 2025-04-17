import tkinter as tk
from tkinter import messagebox

def start_scene():
    text.set("Теплий вечір. Ти сидиш у парку, читаєш. До тебе підходить хлопець з усмішкою.\n\n\"Привіт. Можна до тебе приєднатися?\"")
    button1.config(text="Так", command=scene_talk)
    button2.config(text="Вибач", command=scene_alone)

def scene_talk():
    text.set("Ви говорите годинами. Він цікавий, теплий... Ти хочеш запросити його на каву?")
    button1.config(text="Запросити на каву", command=scene_cafe)
    button2.config(text="Прощатись", command=scene_farewell)

def scene_alone():
    text.set("Ти залишаєшся сам. Можливо, ти ще зустрінеш його знову...\n\nКінець гри.")
    button1.config(text="Спробувати знову", command=start_scene)
    button2.config(text="Вийти", command=root.quit)

def scene_cafe():
    text.set("Ви сидите в кафе. Його рука торкається твоєї. Що зробиш?")
    button1.config(text="Взяти за руку", command=scene_love)
    button2.config(text="Відсторонитись", command=scene_maybe)

def scene_love():
    text.set("Він усміхається. Ви мовчите, але це мовчання — тепле.\n\nЦе початок чогось справжнього. 💖")
    button1.config(text="Спробувати знову", command=start_scene)
    button2.config(text="Вийти", command=root.quit)

def scene_maybe():
    text.set("Він розуміє. Ви прощаєтесь. Можливо, ви ще зустрінетесь...\n\nКінець гри.")
    button1.config(text="Спробувати знову", command=start_scene)
    button2.config(text="Вийти", command=root.quit)

def scene_farewell():
    text.set("Ви попрощались. Але щось лишилось у душі... \n\nКінець гри.")
    button1.config(text="Спробувати знову", command=start_scene)
    button2.config(text="Вийти", command=root.quit)

# GUI
root = tk.Tk()
root.title("💘 Перше побачення")
root.geometry("500x300")

text = tk.StringVar()
label = tk.Label(root, textvariable=text, wraplength=480, justify="left", font=("Arial", 12))
label.pack(pady=20)

button1 = tk.Button(root, text="", width=25, command=None)
button1.pack(pady=5)
button2 = tk.Button(root, text="", width=25, command=None)
button2.pack(pady=5)

start_scene()
root.mainloop()
