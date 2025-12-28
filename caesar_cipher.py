import tkinter as tk
from tkinter import messagebox

LOWER_TR = "abcçdefgğhıijklmnoöprsştuüvyz"
UPPER_TR = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

def caesar_transform(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char in LOWER_TR:
            idx = LOWER_TR.index(char)
            result += LOWER_TR[(idx + shift) % len(LOWER_TR)]
        elif char in UPPER_TR:
            idx = UPPER_TR.index(char)
            result += UPPER_TR[(idx + shift) % len(UPPER_TR)]
        else:
            result += char
    return result

def encrypt_action():
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Shift value must be an integer.")
        return

    input_data = input_text.get("1.0", tk.END).strip()
    output_data = caesar_transform(input_data, shift)

    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output_data)
    output_text.config(state="disabled")

def decrypt_action():
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Shift value must be an integer.")
        return

    input_data = input_text.get("1.0", tk.END).strip()
    output_data = caesar_transform(input_data, -shift)

    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output_data)
    output_text.config(state="disabled")

# Main window
root = tk.Tk()
root.title("Caesar Cipher Tool (Extended Latin)")
root.resizable(False, False)

# Input
tk.Label(root, text="Input Text:").grid(row=0, column=0, padx=10, pady=5, sticky="nw")
input_text = tk.Text(root, width=45, height=5)
input_text.grid(row=0, column=1, padx=10, pady=5)

# Shift
tk.Label(root, text="Shift Value:").grid(row=1, column=0, padx=10, sticky="w")
shift_entry = tk.Entry(root, width=10)
shift_entry.grid(row=1, column=1, sticky="w")
shift_entry.insert(0, "3")

# Buttons
tk.Button(root, text="Encrypt", command=encrypt_action).grid(row=2, column=0, pady=10)
tk.Button(root, text="Decrypt", command=decrypt_action).grid(row=2, column=1, pady=10, sticky="w")

# Output
tk.Label(root, text="Output Text:").grid(row=3, column=0, padx=10, sticky="nw")
output_text = tk.Text(root, width=45, height=5, state="disabled")
output_text.grid(row=3, column=1, padx=10, pady=5)

root.mainloop()
