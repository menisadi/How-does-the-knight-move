import chess
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox


def how_the_knight_move(square1):
    distances = np.zeros((8, 8))
    for square2 in chess.SQUARES:
        distances[
            7 - chess.square_rank(square2), chess.square_file(square2)
        ] = chess.square_knight_distance(square1, square2)
    return distances


def draw_board_with_distances(distances, square):
    fig, ax = plt.subplots()
    distances = distances.astype(int)
    ax.imshow(distances, cmap=plt.cm.Blues)
    ax.set_xticks(np.arange(8))
    ax.set_yticks(np.arange(8))
    ax.set_xticklabels(chess.FILE_NAMES)
    ax.set_yticklabels(reversed(chess.RANK_NAMES))
    ax.set_xlim(-0.5, 7.5)
    ax.set_ylim(7.5, -0.5)
    ax.set_title("Knight's Distance")

    knight_img = mpimg.imread("knight.png")
    knight_img = np.flipud(knight_img)

    row, col = 7 - chess.square_rank(square), chess.square_file(square)

    scaling_factor = 0.8
    ax.imshow(
        knight_img,
        extent=(
            col - 0.5 + (1 - scaling_factor) / 2,
            col + 0.5 - (1 - scaling_factor) / 2,
            row - 0.5 + (1 - scaling_factor) / 2,
            row + 0.5 - (1 - scaling_factor) / 2,
        ),
        alpha=0.5,
        aspect="auto",
    )
    for i in range(8):
        for j in range(8):
            if distances[i, j] > 0:
                text = ax.text(
                    j,
                    i,
                    distances[i, j],
                    ha="center",
                    va="center",
                    color="w",
                    fontsize=20,
                )

    plt.show()


def on_square_click(event):
    col = event.x // square_size
    row = 7 - (event.y // square_size)
    square = chess.square(col, row)

    if 0 <= col < 8 and 0 <= row < 8:
        distances_from_square = how_the_knight_move(square)
        draw_board_with_distances(distances_from_square, square)
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

# Draw the chessboard
square_size = 400 // 8
for i in range(8):
    for j in range(8):
        color = "white" if (i + j) % 2 == 0 else "black"
        canvas.create_rectangle(
            j * square_size,
            i * square_size,
            (j + 1) * square_size,
            (i + 1) * square_size,
            fill=color,
        )

# Bind the click event to the canvas
canvas.bind("<Button-1>", on_square_click)

# Start the Tkinter main loop
root.mainloop()
