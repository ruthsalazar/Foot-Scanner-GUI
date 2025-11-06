import tkinter as tk
import serial
import time

# --- Connect to Arduino ---
try:
    arduino = serial.Serial('COM4', 57600, timeout=1)  # Update COM port if needed
    time.sleep(2)
except serial.SerialException:
    arduino = None
    print("Arduino not connected.")

# --- Simulated Begin Scan Logic ---
def begin_scan():
    name = patient_name.get().strip()
    size = shoe_size.get().strip()
    g = gender.get()

    if not name:
        status_label.config(text="Please enter a patient name.", fg="red")
        return
    if not size.isdigit():
        status_label.config(text="Please enter a valid shoe size.", fg="red")
        return

    if arduino:
        arduino.write(b'G')  # Start scan
        status_label.config(text=f"Scanning {name} ({g}, size {size})...", fg="blue")
        root.update()

        while True:
            if arduino.in_waiting:
                response = arduino.read().decode('utf-8')
                if response == 'D':
                    status_label.config(text=f"Scan complete for {name}! Returning to origin...", fg="green")
                    root.update()
                    time.sleep(0.5)
                    arduino.write(b'Z')  # Reset to origin
                    break
            time.sleep(0.1)
    else:
        status_label.config(text="Arduino not connected.", fg="red")


# --- Second Screen Layout ---
def show_weight_screen():
    intake_frame.pack_forget()
    weight_frame.pack()

# --- Main Window ---
root = tk.Tk()
root.title("Foot Scanner")
root.geometry("400x300")

# --- Intake Screen ---
patient_name = tk.StringVar()
shoe_size = tk.StringVar()
gender = tk.StringVar(value="None")

intake_frame = tk.Frame(root)
tk.Label(intake_frame, text="Patient Name:").pack()
tk.Entry(intake_frame, textvariable=patient_name).pack()
tk.Label(intake_frame, text="Shoe Size:").pack()
tk.Entry(intake_frame, textvariable=shoe_size).pack()
tk.Label(intake_frame, text="Gender:").pack()
gender_frame = tk.Frame(intake_frame)
gender_frame.pack()
tk.Radiobutton(gender_frame, text="Women's", variable=gender, value="Women").pack(side="left")
tk.Radiobutton(gender_frame, text="Men's", variable=gender, value="Men").pack(side="left")
tk.Button(intake_frame, text="Continue", command=show_weight_screen).pack(pady=10)
intake_frame.pack()

# --- Weight Screen ---
weight_frame = tk.Frame(root)
tk.Label(weight_frame, text="Weight Distribution", font=("Arial", 14)).pack(pady=10)
tk.Label(weight_frame, text="0.5", font=("Arial", 24), fg="blue").pack(pady=10)
tk.Button(weight_frame, text="Begin Scan", command=begin_scan).pack(pady=10)
status_label = tk.Label(weight_frame, text="", font=("Arial", 12), fg="green")
status_label.pack()

# Run GUI
root.mainloop()
