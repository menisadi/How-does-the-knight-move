import sys

import chess
import matplotlib.pyplot as plt
import numpy as np


def how_the_knight_move(square1):
    distances = np.zeros((8, 8))
    for square2 in chess.SQUARES:
        distances[
            chess.square_rank(square2), chess.square_file(square2)
        ] = chess.square_knight_distance(square1, square2)
    return distances


def draw_board_with_distances(distances):
    """create an image of the chessboard with the distances"""
    fig, ax = plt.subplots()
    # make sure distances are integers
    distances = distances.astype(int)
    ax.imshow(distances, cmap=plt.cm.Blues)
    ax.set_xticks(np.arange(8))
    ax.set_yticks(np.arange(8))
    ax.set_xticklabels(chess.FILE_NAMES)
    ax.set_yticklabels(chess.RANK_NAMES)
    ax.set_xlim(-0.5, 7.5)
    ax.set_ylim(7.5, -0.5)
    ax.set_title("Knight's Distance")
    for i in range(8):
        for j in range(8):
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
    print(square)

    square_parsed = chess.parse_square(square)
    print(square_parsed)
    distances_from_square = how_the_knight_move(square_parsed)
    print(distances_from_square)
    draw_board_with_distances(distances_from_square)
