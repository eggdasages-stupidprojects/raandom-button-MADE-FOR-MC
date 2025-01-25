import time
import random
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController, Button
import tkinter as tk

# Initialize controllers
keyboard = KeyboardController()
mouse = MouseController()

# Create a Tkinter window for displaying the last clicked key
root = tk.Tk()
root.title("Last Action in Minecraft Simulation")
root.geometry("300x100+1600+900")  # Adjust position to bottom-right corner of the screen
root.attributes("-topmost", True)  # Keep the window on top
label = tk.Label(root, text="", font=("Arial", 24))
label.pack(expand=True)

# Function to update the label with the last pressed key or action
def update_label(text):
    label.config(text=text)
    root.update()

# Function to press keys or perform mouse actions based on input (Minecraft actions)
def perform_action(digit):
    if digit == "1":  # Move forward (W)
        keyboard.press("w")
        keyboard.release("w")
        update_label("Move Forward (W)")
    elif digit == "2":  # Move backward (S)
        keyboard.press("s")
        keyboard.release("s")
        update_label("Move Backward (S)")
    elif digit == "3":  # Strafe left (A)
        keyboard.press("a")
        keyboard.release("a")
        update_label("Strafe Left (A)")
    elif digit == "4":  # Strafe right (D)
        keyboard.press("d")
        keyboard.release("d")
        update_label("Strafe Right (D)")
    elif digit == "5":  # Jump (Space)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        update_label("Jump (Space)")
    elif digit == "6":  # Left click to attack (mouse)
        mouse.press(Button.left)
        mouse.release(Button.left)
        update_label("Attack (Left Click)")
    elif digit == "7":  # Right click to interact (mouse)
        mouse.press(Button.right)
        mouse.release(Button.right)
        update_label("Interact (Right Click)")
    elif digit == "8":  # Sprint (Shift)
        keyboard.press(Key.shift)
        keyboard.release(Key.shift)
        update_label("Sprint (Shift)")
    elif digit == "9":  # Open inventory (E)
        keyboard.press("e")
        keyboard.release("e")
        update_label("Open Inventory (E)")
    elif digit == "0":  # Drop item (Q)
        keyboard.press("q")
        keyboard.release("q")
        update_label("Drop Item (Q)")

# Function to trigger random actions indefinitely (simulate Minecraft play)
def main():
    while True:
        # Perform an action every time
        digit = str(random.randint(0, 9))
        perform_action(digit)
        
        time.sleep(1.2)  # 1.2 seconds delay between attempts
        root.after(0, main)  # Schedule the next run in the Tkinter loop to keep it non-blocking

if __name__ == "__main__":
    root.after(100, main)  # Start the main function after 100ms
    root.mainloop()  # Start Tkinter event loop
