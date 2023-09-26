# Chess Knight's Distance Visualization
> "How does the knight move?" - Alexandra Botez

![License](https://img.shields.io/badge/license-MIT-blue.svg) 
[![GitHub Release](https://img.shields.io/github/v/release/menisadi/How-does-the-knight-move.svg)](https://github.com/menisadi/How-does-the-knight-move /releases) 
[![Python Version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://www.python.org/downloads/)

This Python program uses the Tkinter library to create a simple chessboard where you can explore the distances a chess knight can move from a selected square. It visualizes these distances by coloring the squares on the board based on the number of knight's moves required to reach them.

![Chess Knight's Distance Visualization](screenshot.png)

## Usage

### Executable Release (UNIX)

If you prefer running the program as an executable on UNIX systems, follow these steps:

1. Download the latest release from the [Releases](link-to-releases-page) page.

2. Open a terminal and navigate to the directory where you downloaded the file.

4. Make the executable file (`regui`) executable by running:

   `chmod +x regui`

5. Run the program by executing:

   `./regui`

### Usage (Running from Source)

If you want to run the program from the source code, follow these steps:

1. Clone this repository to your local machine using `git clone`.
2. Make sure you have Python 3.x installed.
3. Install the required libraries using pip or any other package menager of you choice :

   `pip install numpy python-chess`

4. Run the program by executing:

   `python regui.py`

### Web Version

I've also developed a web-based version. You can access it online by visiting [http://menitm.pythonanywhere.com/](http://menitm.pythonanywhere.com/).
Please note that while the web version is functional, it may benefit from some design enhancements, primarily for mobile browsers. It's not currently responsive for smaller screens, and there's room for styling improvements. Your feedback on potential design improvements is always welcome!

## How it Works

The program calculates the knight's distance for each square on the chessboard using a 2D NumPy array. It then maps these distances to colors to create a visual representation of the knight's movement range.

## Acknowledgments

This program was created by me as a simple visualization tool for understanding how chess knights move on a chessboard.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: Contributions are welcome! If you'd like to improve the program or add new features, please open an issue or create a pull request.
