import tkinter as tk
from tkinter import messagebox
import json


def load_data():
    try:
        with open('data_negara.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "File data_negara.json tidak ditemukan.")
        return {}

data_negara = load_data()


def cari_negara():
    negara = entry_negara.get().strip()
    info = data_negara.get(negara)

    if info:
        hasil.set(f"Ibukota: {info['ibukota']}\n"
                  f"Benua: {info['benua']}\n"
                  f"Populasi: {info['populasi']}\n"
                  f"Mata Uang: {info['mata_uang']}")
    else:
        hasil.set("Negara tidak ditemukan di database.")


root = tk.Tk()
root.title("Peta Interaktif: Negara dan Ibukotanya")
root.geometry("400x300")
root.resizable(False, False)

judul = tk.Label(root, text="Peta Interaktif Dunia", font=("Arial", 16, "bold"))
judul.pack(pady=10)

label_input = tk.Label(root, text="Masukkan nama negara:")
label_input.pack()

entry_negara = tk.Entry(root, width=40)
entry_negara.pack(pady=5)

btn_cari = tk.Button(root, text="Cari", command=cari_negara)
btn_cari.pack(pady=5)

hasil = tk.StringVar()
label_hasil = tk.Label(root, textvariable=hasil, justify="left", font=("Arial", 12))
label_hasil.pack(pady=10)

root.mainloop()
