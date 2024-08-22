from tkinter import *
from tkinter import ttk
import requests

API_KEY = "37ad2de8c3b542ed98a100234242008"
URL = "https://api.weatherapi.com/v1/current.json?"

win = Tk()
win.title("Weather App")
win.geometry("400x300")
win.configure(bg="#f0f0f0")


def get_value():
    e_text = entry.get()
    params = {
        "key": API_KEY,
        "q": e_text,
        "aqi": "no"
    }
    response = requests.get(URL, params=params)
    response.raise_for_status()
    temp_c = response.json()['current']['temp_c']
    temp_f = response.json()['current']['temp_f']
    condition = response.json()['current']['condition']['text']

    for widget in result_frame.winfo_children():
        widget.destroy()

    Label(result_frame, text=f"Temperature in C: {temp_c}°C", font=('Helvetica', 12), bg="#f0f0f0").pack(pady=5)
    Label(result_frame, text=f"Temperature in F: {temp_f}°F", font=('Helvetica', 12), bg="#f0f0f0").pack(pady=5)
    Label(result_frame, text=f"Weather Condition: {condition}", font=('Helvetica', 12), bg="#f0f0f0").pack(pady=5)


entry = ttk.Entry(win, font=('Helvetica', 12), width=25)
entry.pack(pady=20)

button = ttk.Button(win, text="Get Weather", command=get_value)
button.pack(pady=10)

result_frame = Frame(win, bg="#f0f0f0")
result_frame.pack(pady=20)

win.mainloop()
