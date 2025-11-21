import tkinter as tk
from tkinter import messagebox

# Encode function
def encode_code128(data):
    start_char = "Ì"  # Start Code B
    stop_char = "Î"   # Stop
    start_code_b = 104
    checksum = start_code_b
    for i, ch in enumerate(data, start=1):
        value = ord(ch) - 32
        checksum += value * i
    checksum %= 103
    checksum_char = chr(checksum + 32) if 32 <= checksum + 32 <= 126 else "?"
    return f"{start_char}{data}{checksum_char}{stop_char}"

# Actions
def encode_and_display():
    user_input = entry.get().strip()
    if user_input:
        encoded = encode_code128(user_input)
        result_var.set(encoded)
        history.append((user_input, encoded))
        update_history_display()
    else:
        messagebox.showwarning("Input Error", "Please enter valid data.")

def copy_to_clipboard():
    encoded_text = result_var.get()
    if encoded_text:
        root.clipboard_clear()
        root.clipboard_append(encoded_text)
        messagebox.showinfo("Copied", "Encoded text copied to clipboard!")
    else:
        messagebox.showwarning("No Data", "Nothing to copy. Please encode first.")

def clear_history():
    history.clear()
    update_history_display()

def update_history_display():
    history_text.delete("1.0", tk.END)
    for original, encoded in history:
        history_text.insert(tk.END, f"{original} -> {encoded}\n")

# GUI Setup
root = tk.Tk()
root.title("Code 128 Encoder for Libre Barcode")
root.geometry("600x400")
root.resizable(False, False)

history = []

title_label = tk.Label(root, text="Libre Barcode 128 Encoder", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

entry_label = tk.Label(root, text="Enter data to encode:", font=("Arial", 12))
entry_label.pack()

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

encode_button = tk.Button(root, text="Encode", command=encode_and_display, font=("Arial", 12), bg="#4CAF50", fg="white")
encode_button.pack(pady=5)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="#2196F3", fg="white")
copy_button.pack(pady=5)

history_label = tk.Label(root, text="History:", font=("Arial", 12))
history_label.pack()

history_text = tk.Text(root, height=8, width=70)
history_text.pack(pady=5)

clear_button = tk.Button(root, text="Clear History", command=clear_history, font=("Arial", 12), bg="#f44336", fg="white")
clear_button.pack(pady=5)

root.mainloop()