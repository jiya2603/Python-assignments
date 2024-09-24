import tkinter as tk
from file_organizer import organize_files
# Create the main window
root = tk.Tk()
root.title("File organizer")
root.geometry("300x150")  # Set the window size

# Function to be called when the button is clicked
def show_input():
    address = entry.get()  # Get text from the entry box
    organize_files(address)

# Label for entry
label = tk.Label(root, text="Enter URL:")
label.pack(pady=10)  # Add padding around the label

# Entry (input block) where user can type text
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Button to trigger the function show_input
button = tk.Button(root, text="Submit", command=show_input)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
