import sys

import chess
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


def how_the_knight_move(square1):
    distances = np.zeros((8, 8))
    for square2 in chess.SQUARES:
        distances[
            7 - chess.square_rank(square2), chess.square_file(square2)
        ] = chess.square_knight_distance(square1, square2)
    return distances


def draw_board_with_distances(distances, square):
    """create an image of the chessboard with the distances and overlay a knight image"""
    fig, ax = plt.subplots()
    # make sure distances are integers
    distances = distances.astype(int)
    ax.imshow(distances, cmap=plt.cm.Blues)
    ax.set_xticks(np.arange(8))
    ax.set_yticks(np.arange(8))
    ax.set_xticklabels(chess.FILE_NAMES)
    ax.set_yticklabels(reversed(chess.RANK_NAMES))  # Reverse the rank labels
    ax.set_xlim(-0.5, 7.5)
    ax.set_ylim(7.5, -0.5)
    ax.set_title("Knight's Distance")

    # Load the image of a knight and flip it vertically
    knight_img = mpimg.imread("knight.png")
    knight_img = np.flipud(knight_img)

    # Calculate the position of the input square
    row, col = 7 - chess.square_rank(square), chess.square_file(square)

    # Display the knight image on the board (adjust scaling factor)
    scaling_factor = (
        0.8  # Adjust this factor to make the knight smaller or larger
    )
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


if __name__ == "__main__":
    # parse square from command line
    if len(sys.argv) != 2:
        print("Usage: python algo.py <square>")
        sys.exit(1)
    square = sys.argv[1]
    square_parsed = chess.parse_square(square)
    distances_from_square = how_the_knight_move(square_parsed)
    draw_board_with_distances(distances_from_square, square_parsed)
