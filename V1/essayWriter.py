import keyboard
import os

DelayTime = 0 

try:
    user_input = input("Enter delay time between each character\n(0 for no delay, or higher to slow typing)\nDelay : ")
    DelayTime = float(user_input) if user_input else 0
except ValueError:
    print("Invalid input. Delay time will be set to 0.")

print("Press '1' to start writing the text from 'essaytext.txt'.\n")
keyboard.wait("1")

keyboard.send("backspace", True, True)

file_path = 'essaytext.txt'

# Check if the file exists before attempting to open it
if os.path.exists(file_path):
    try:
        # Opens "essaytext.txt" with UTF-8 encoding to handle all types of characters
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            # Writes the text from the file with the specified delay
            keyboard.write(text, DelayTime)
    except Exception as e:
        print(f"An error occurred while writing the text: {e}")
else:
    print(f"Error: '{file_path}' not found. Make sure the file exists in the same directory as the script.")
