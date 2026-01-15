import tkinter as tk

APP_VERSION = "v2.0.0"

def calculate_sr_ratio():
    try:
        sf_input = sf_entry.get()
        sf_int_value = int(sf_input)
        sr_input = sr_entry.get()
        sr_int_value = int(sr_input)
        total_store_inv = sf_int_value + sr_int_value
        sr_ratio = sr_int_value / total_store_inv * 100
        result = f"Your stockroom ratio is: {sr_ratio:.2f}"
        result_label.config(text=f"{result}")
    except:
        result_label.config(text="Error")



window = tk.Tk()
window.geometry("320x200")
sf_entry_label = tk.Label(text="How many pieces do you have on the sales floor?", font=("Helvetica", 8))
sf_entry = tk.Entry(bg="white", fg="blue")
sr_entry_label = tk.Label(text="How many pieces do you have in the stockroom?", font=("Helvetica", 8))
sr_entry = tk.Entry(bg="white", fg="blue")
btn = tk.Button(
    text="Calculate",
    command=calculate_sr_ratio
)
sf_entry_label.pack(anchor=tk.W)
sf_entry.pack(anchor=tk.W)
sr_entry_label.pack(anchor=tk.W)
sr_entry.pack(anchor=tk.W)
btn.pack(anchor=tk.W)
result_label = tk.Label(window)
result_label.pack()
version_label = tk.Label(
    window,
    text=f"Version: {APP_VERSION}",
    font=(4),
    anchor="e",
)

version_label.pack()
window.mainloop()