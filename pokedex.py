from tkinter import Grid, font
import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

from urllib3 import response

window = tk.Tk()

menu = tk.Menu(window)
menu.config(font=("Arial", 10), bg="black" , activebackground="black", activeforeground="white")

window.geometry("800x700")
window.title("Jonalbert's Pokedex")
window.config(padx=10, pady=10,bg= "black", menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label= "File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

help_menu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Bueno socio...")
help_menu.add_command(label="Esto no se ha programado aun...")

info_menu = tk.Menu(menu)
menu.add_cascade(label="Info...", menu=info_menu)
info_menu.add_command(label="Beta: 0.2v")

title_label = tk.Label(window, text= "Jonalbert's Pokedex",bg= "black", fg="white")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window, bg= "black")
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(window, bg= "black", fg="white")
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window, bg= "black", fg="white")
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

error_id_name =tk.Label(window)


def load_pokemon():
        
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text=" - ".join([ t for t in pokemon.types]).title())

    

label_id_name = tk.Label(window, text="ID or Name", bg="black",fg="white")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name =tk.Text(window, height=1,bg="white", fg="black")
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)


btn_load = tk.Button(window, text="Load Pokemon", command=load_pokemon, bg="black", fg="white", activebackground="white", activeforeground="gray")
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)

check_btn = tk.Checkbutton(window, text= "Type")
check_btn.config(font=("Arial", 10))
check_btn.pack(padx=10, pady=10)


window.mainloop()