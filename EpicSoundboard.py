# Import tkinter library and give it the shorter name 'tk'
import tkinter as tk
import pygame  # For playing sound

#SOUND LIBRARY
# Initialize pygame mixer for sound
pygame.mixer.init()
# Load the sound file - replace with your sound file path
# Make sure to use a .wav or .mp3 file

sound_bruh = pygame.mixer.Sound("BRUH.mp3")
sound_horn = pygame.mixer.Sound("HORN.mp3")
sound_sus = pygame.mixer.Sound("SUS.mp3")

# Define what happens when button is clicked
# This is called a 'callback function'
def bruh_clicked():
   # Play the sound when button is clicked
    sound_bruh.play()
    print("Button was clicked!")

def horn_clicked():
   # Play the sound when button is clicked
    sound_horn.play()
    print("Button was clicked!")

def sus_clicked():
   # Play the sound when button is clicked
    sound_sus.play()
    print("Button was clicked!")

# Create the main application window
window = tk.Tk()
# Set the title that appears at the top of the window
window.title("My First App")

# Create a button widget
# Parameters are:
#   - window: where to put the button (our main window)
#   - text: what to display on the button
#   - command: which function to run when clicked
button_bruh = tk.Button(window, 
                 text="Bruh!",
                 command=bruh_clicked)
button_horn = tk.Button(window, 
                 text="Horn",
                 command=horn_clicked)
button_sus = tk.Button(window, 
                 text="sus...",
                 command=sus_clicked)
# Add the button to the window
# 'pack()' is a simple way to add widgets to the window
button_bruh.pack()
button_horn.pack()
button_sus.pack()
# Start the event loop that keeps the window running
# This needs to be the last line
window.mainloop()