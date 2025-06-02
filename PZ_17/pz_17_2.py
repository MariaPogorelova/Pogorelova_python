import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("PythonExamples.org")
window.geometry("300x200")

# Function to handle the Entry widget focus events
def on_entry_focus_in(event):
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)
        entry.configure(show="")
        entry.configure(fg="black")

def on_entry_focus_out(event):
    if entry.get() == "":
        entry.insert(0, placeholder_text)
        entry.configure(show="*")
        entry.configure(fg="gray")

# Create an Entry widget with placeholder text
placeholder_text = "Enter your input.."
entry = tk.Entry(window, fg="gray")
entry.insert(0, placeholder_text)
entry.bind("<FocusIn>", on_entry_focus_in)
entry.bind("<FocusOut>", on_entry_focus_out)
entry.pack()

# Run the application
window.mainloop()