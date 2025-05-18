import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# Create the games subfolder if it doesn't exist
GAMES_FOLDER = "games"
if not os.path.exists(GAMES_FOLDER):
    os.makedirs(GAMES_FOLDER)

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Game Loader")
root.geometry("400x500")
root.configure(bg="#2e2e2e")

# Title label
title_label = tk.Label(root, text="Custom Game Loader", font=("Arial", 16, "bold"), bg="#2e2e2e", fg="#ffffff")
title_label.pack(pady=10)

# Frame to hold game list with a canvas for scrolling
canvas = tk.Canvas(root, bg="#2e2e2e", highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
game_frame = tk.Frame(canvas, bg="#2e2e2e")

# Configure the canvas and scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0, 0), window=game_frame, anchor="nw")

# Update the scroll region when the frame size changes
game_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# List to store game labels and their names
game_labels = []
game_files = []
selected_index = 0  # Track the currently selected game

# Function to run a game
def run_game(game_file):
    try:
        subprocess.run(["python3", f"{GAMES_FOLDER}/{game_file}"])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run {game_file}: {str(e)}")

# Function to update the highlighted selection
def update_selection():
    global selected_index
    for i, label in enumerate(game_labels):
        if i == selected_index:
            label.config(bg="#666666", fg="#ffffff")
        else:
            label.config(bg="#4a4a4a", fg="#ffffff")

# Function to handle key presses
def on_key_press(event):
    global selected_index
    if event.keysym == "Up" and selected_index > 0:
        selected_index -= 1
    elif event.keysym == "Down" and selected_index < len(game_labels) - 1:
        selected_index += 1
    elif event.keysym == "Return":
        if selected_index == len(game_labels) - 1:  # Exit option
            root.quit()
        else:
            run_game(game_files[selected_index])
    update_selection()
    # Scroll to keep the selected item in view
    canvas.yview_moveto(selected_index / len(game_labels))

# Function to load game files and create the list
def load_games():
    global game_labels, game_files, selected_index
    # Clear existing laebls
    for label in game_labels:
        label.destroy()
    game_labels.clear()
    game_files.clear()
    selected_index = 0

    # Scan the games folder for .py files
    found_files = [f for f in os.listdir(GAMES_FOLDER) if f.endswith(".py")]
    game_files.extend(found_files)

    # Add labels for each game
    for game_file in game_files:
        game_name = game_file.replace(".py", "").capitalize()
        label = tk.Label(
            game_frame,
            text=game_name,
            font=("Arial", 12),
            bg="#4a4a4a",
            fg="#ffffff",
            anchor="w",
            padx=20,
            pady=5
        )
        label.pack(fill="x", padx=20, pady=2)
        game_labels.append(label)

    # Add the Exit option
    exit_label = tk.Label(
        game_frame,
        text="Exit",
        font=("Arial", 12),
        bg="#4a4a4a",
        fg="#ffffff",
        anchor="w",
        padx=20,
        pady=5
    )
    exit_label.pack(fill="x", padx=20, pady=2)
    game_labels.append(exit_label)

    # Update the selection highlight
    update_selection()

# Bind arrow keys and Enter to the root window
root.bind("<Up>", on_key_press)
root.bind("<Down>", on_key_press)
root.bind("<Return>", on_key_press)

# Initial load of games
load_games()

# Start the Tkinter main loop
root.mainloop()
