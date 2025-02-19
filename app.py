import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

box = ttk.Window("Formulário de inscrição")
box.geometry("600x600")
Style = Style(theme=("darkly"))

label = ttk.Label(box, text=("Formulário de inscrição"))
label.pack(pady=60)
label.config(font=("Arial", 20, "bold"))

name = ttk.Frame(box)
name.pack(pady=0)
ttk.Label(name, text="Nome").pack(side=LEFT, padx=0)
ttk.Entry(name).pack(side=LEFT, fill="x", expand=True, padx=40)

email = ttk.Frame(box)
email.pack(pady=30)
ttk.Label(email, text="Email").pack(side=LEFT, padx=2)
ttk.Entry(email).pack(side=LEFT, fill="x", expand=True, padx=40)

age = ttk.Frame(box)
age.pack(pady=0)
ttk.Label(age, text="Idade").pack(side=LEFT, padx=2)
ttk.Entry(age).pack(side=LEFT, fill="x", expand=True, padx=40)

checkboox = ttk.Frame(box)
checkboox.pack()



box.mainloop()
