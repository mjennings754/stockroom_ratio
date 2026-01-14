import tkinter as tk
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
        result.config(text="Error")



window = tk.Tk()
sf_entry_label = tk.Label(text="How many pieces do you have on the sales floor?")
sf_entry = tk.Entry(bg="white", fg="blue")
sr_entry_label = tk.Label(text="How many pieces do you have in the stockroom?")
sr_entry = tk.Entry(bg="white", fg="blue")
btn = tk.Button(
    text="Calculate",
    command=calculate_sr_ratio
)

sf_entry_label.pack()
sf_entry.pack()
sr_entry_label.pack()
sr_entry.pack()
btn.pack()
result_label = tk.Label(window)
result_label.pack()
window.mainloop()