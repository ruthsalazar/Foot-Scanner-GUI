import tkinter as tk

# --- First Screen: Patient Intake ---
def open_weight_screen():
    # Save patient data (you can use these later to name files, etc.)
    print("Patient Name:", patient_name.get())
    print("Shoe Size:", shoe_size.get())
    print("Gender:", gender.get())

    # Hide first screen
    intake_frame.pack_forget()

    # Show second screen
    weight_frame.pack()

# --- Second Screen: Mock Weight Display ---
def begin_scan():
    print("Scan started!")  # Placeholder for motor/image logic

# Main window
root = tk.Tk()
root.title("Foot Scanner")
root.geometry("400x300")

# --- Variables ---
patient_name = tk.StringVar()
shoe_size = tk.StringVar()
gender = tk.StringVar(value="None")  # Default selection

# --- Intake Screen Layout ---
intake_frame = tk.Frame(root)

tk.Label(intake_frame, text="Patient Name:").pack(pady=5)
tk.Entry(intake_frame, textvariable=patient_name).pack()

tk.Label(intake_frame, text="Shoe Size:").pack(pady=5)
tk.Entry(intake_frame, textvariable=shoe_size).pack()

tk.Label(intake_frame, text="Gender:").pack(pady=5)
gender_frame = tk.Frame(intake_frame)
gender_frame.pack()
tk.Radiobutton(gender_frame, text="Women's", variable=gender, value="Women").pack(side="left", padx=10)
tk.Radiobutton(gender_frame, text="Men's", variable=gender, value="Men").pack(side="left", padx=10)

tk.Button(intake_frame, text="Continue", command=open_weight_screen).pack(pady=20)
intake_frame.pack()

# --- Weight Screen Layout ---
weight_frame = tk.Frame(root)

tk.Label(weight_frame, text="Weight Distribution", font=("Arial", 14)).pack(pady=10)
tk.Label(weight_frame, text="0.5", font=("Arial", 24), fg="blue").pack(pady=10)

tk.Button(weight_frame, text="Begin Scan", command=begin_scan).pack(pady=20)

# Start GUI
root.mainloop()