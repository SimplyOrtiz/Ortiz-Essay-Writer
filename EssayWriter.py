import tkinter as tk
from tkinter import ttk, messagebox
import keyboard as key
import threading

## Variables ##
version = "0.0.2"
ResizeableWindow = [False, True]

EssayText = str
delayTime = 0 # Works like a Ctrl + V #

## Functions ##
def setResizeability(Resize):
    root.wm_resizable(Resize[0], Resize[1])

def start_writing():
    global delayTime
    text = entry_essay.get("1.0", "end-1c") # Get text, removing the trailing newline

    output_label.config(text="Press '1' to start writing the text...")
    key.wait("1")
    output_label.config(text="Writing...")
    key.send("backspace", True, True)
    key.write(text, delayTime)
    output_label.config(text="Finished")
    
    # Re-enable the button after writing is finished
    # Use root.after to safely update the GUI from the main thread
    root.after(0, lambda: write_button.config(state=tk.NORMAL))


def writeEssay_threaded():
    # Disable the button to prevent multiple clicks
    write_button.config(state=tk.DISABLED)
    # Start the writing process in a separate thread
    threading.Thread(target=start_writing).start()

def closeWindow(Window, Name, ArgValue=1):
    global delayTime
    Window.destroy()
    Arg1 = Name.lower()
    if Arg1 == "speed_window":
        print("Saving Speed")
        delayTime = float(ArgValue)
        pass
    if Arg1 == ("none" or "" or " "):
        print("No Value for Arg1 [closeWindow]")
        pass

def only_numbers(char):
    return char.isdigit() or char == "."

def changeSpeedWindow():
    speed_window = tk.Toplevel(root)  # Pass the root window as the parent
    speed_window.title("Speed - Settings")
    speed_window.geometry("350x250")

    tk.Label(speed_window, text="At What speed Would you like to Write?\n(You can use decimals Ex: 0.25,0.5,etc.)").pack(pady=20)
    
    validation = speed_window.register(only_numbers)
    entry = tk.Entry(speed_window, validate="key", validatecommand=(validation, '%S'))
    entry.pack(padx=20, pady=20)


    ## Buttons ##
    tk.Label(speed_window, text="(This Won't be saved for the next time you open the app.)", underline=1).pack(pady=0)
    tk.Button(speed_window, text="Save and Go back", command= lambda: closeWindow(speed_window, "speed_window", entry.get())).pack(padx=10)
    tk.Button(speed_window, text="Go back", command= lambda: closeWindow(speed_window, "none")).pack(padx=10)


## Main Window ##
root = tk.Tk()
root.geometry("500x300")  # Increased height to accommodate the new label
setResizeability(ResizeableWindow)
root.wm_title(f"Ortiz Essay Writer (Version {version})")

## Window Menu ##
menubar = tk.Menu(root)
root.config(menu=menubar)
file_menu = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Write Text", command=writeEssay_threaded)
file_menu.add_command(label="Speed", command=changeSpeedWindow)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)


# MainFrame: Text + Write
frame_write = tk.LabelFrame(root, text="Text")
tk.Label(frame_write, text="Insert Text:").pack(anchor="w")
frame_write.pack(padx=10, pady=5, fill="x")
entry_essay = tk.Text(frame_write, height=10)  # Increased height for better text input
entry_essay.pack(side="top", padx=5, fill="x", expand=True)
write_button = tk.Button(frame_write, text="Write", command=writeEssay_threaded)
write_button.pack(padx=5)



# Output Label
output_label = tk.Label(root, text="")
output_label.pack(pady=5)

## Starts 'root' Main Loop ##
root.mainloop()