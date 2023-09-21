import tkinter as tk
from tkinter import messagebox

import chess
import numpy as np


def how_the_knight_move(square1):
    distances = np.zeros((8, 8))
    for square2 in chess.SQUARES:
        distances[
            7 - chess.square_rank(square2), chess.square_file(square2)
        ] = chess.square_knight_distance(square1, square2)
    return distances


def color_chessboard(canvas, distances):
    square_size = 400 // 8
    max_distance = np.max(distances)
    for row in range(8):
        for col in range(8):
            distance = distances[row, col]
            color = calculate_color(distance, max_distance)
            canvas.create_rectangle(
                col * square_size,
                row * square_size,
                (col + 1) * square_size,
                (row + 1) * square_size,
                fill=color,
            )
            canvas.create_text(
                col * square_size + square_size // 2,
                row * square_size + square_size // 2,
                text=str(int(distance)),
                fill="black" if color == "white" else "black",
                font=("Arial", 12),
            )


def calculate_color(distance, max_distance):
    # Calculate the color based on distance
    normalized_distance = min(distance / max_distance, 1.0)
    r = int(normalized_distance * 255)
    color = "#{:02X}{:02X}{:02X}".format(r, r, 255)
    return color


def on_square_click(event):
    col = event.x // square_size
    row = 7 - (event.y // square_size)
    square = chess.square(col, row)

    if 0 <= col < 8 and 0 <= row < 8:
        distances_from_square = how_the_knight_move(square)
        color_chessboard(canvas, distances_from_square)
    else:
        messagebox.showinfo(
            "Invalid Square", "Please click inside the chessboard."
        )


# Create a Tkinter window
root = tk.Tk()
root.title("Chess Knight's Distance")

# Create a canvas for the chessboard
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Draw the initial chessboard (start with black and white squares)
square_size = 400 // 8
for row in range(8):
    for col in range(8):
        color = "white" if (row + col) % 2 == 0 else "black"
        canvas.create_rectangle(
            col * square_size,
            row * square_size,
            (col + 1) * square_size,
            (row + 1) * square_size,
            fill=color,
        )

# Bind the click event to the canvas
canvas.bind("<Button-1>", on_square_click)

# Start the Tkinter main loop
root.mainloop()
