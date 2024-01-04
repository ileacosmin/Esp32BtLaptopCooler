import bluetooth
import customtkinter as ctk
import tkinter as tk
import re
from tkinter import messagebox
from bluetooth import *
import time

esp32_address=''
def print_devices_to_console():
    print ("performing inquiry...")

    nearby_devices = discover_devices(lookup_names = True)

    print ("found %d devices" % len(nearby_devices))

    for name, addr in nearby_devices:
        print (" %s - %s" % (addr, name))

    # ESP32 Bluetooth address (replace with your ESP32's address)
    print ("enter the code of the device you want to connect to")

    esp32_address = input()


def discover_bt():
    nearby_devices = discover_devices(lookup_names=True)

    for addr, name in nearby_devices:
        device_listbox.insert(ctk.END, f"{name} ({addr})")

def send_command(command):
    try:
        label.configure(text=f"Slider Value: {command}")
        slider.set(int(command))
        print('Sending command: '+command+' to: '+esp32_address)
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((esp32_address, 1))
        sock.send(command)
        sock.close()

    except Exception as e:
        messagebox.showerror("Error", f"Error sending command: {e}")

def on_select(event):
    # Get the selected index
    selected_index = device_listbox.curselection()

    # Check if an item is selected
    if selected_index:
        selected_item = device_listbox.get(selected_index[0])
        print(f"Selected item: {selected_item}")

        # Use a regular expression to find the string between parentheses
        match = re.search(r'\((.*?)\)', selected_item)

        # Check if a match is found
        if match:
            result = match.group(1)  # Get the content between parentheses
            global esp32_address  # Update the global variable
            esp32_address=result
            print("Address:", result)
        else:
            print("No match found.")
def update_slider_value(value):
    label.config(text=f"Slider Value: {value}")

def debounce(func, delay=0.5):
    def wrapper(*args, **kwargs):
        current_time = time.time()
        if not hasattr(wrapper, 'last_time') or (current_time - wrapper.last_time) > delay:
            func(*args, **kwargs)
            wrapper.last_time = current_time

    return wrapper

# GUI Setup
app = ctk.CTk()
app.geometry('720x480')
app.title("Bluetooth Control App")

# Button to discover nearby devices
discover_button = ctk.CTkButton(app, text="Discover Devices", command=discover_bt)
discover_button.pack(pady=10)

# Listbox to display nearby devices
device_listbox = tk.Listbox(app, selectmode=tk.SINGLE, width=40, height=6)
device_listbox.pack(pady=10)
device_listbox.bind("<<ListboxSelect>>", on_select)

# Buttons to control the LED
on_button = ctk.CTkButton(app, text="Turn ON FAN", command=lambda: send_command('255'))
on_button.pack(pady=5)

off_button = ctk.CTkButton(app, text="Turn OFF FAN", command=lambda: send_command('0'))
off_button.pack(pady=5)

# Create a label to display the slider value
label = ctk.CTkLabel(app, text="Slider Value: 0")
label.pack(pady=10)

# Create a slider
slider = ctk.CTkSlider(app, from_=0, to=255,  command=lambda pos: send_command(str(round(pos))))
slider.set(0)
slider.pack(pady=10)
# Run the GUI
app.mainloop()