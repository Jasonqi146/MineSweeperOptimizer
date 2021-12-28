# CS 3510 Minesweeper Project Starter Code

### By: Pranay Agrawal

## NOTE

* **We do not require you to use this starter code!!** However, we believe that it provides a good way for you to focus on only developing/debugging/testing your algorithm. **This should be used as tool for analyzing how well your algorithm works**.
* You are free to edit all files. 
* we do **NOT** require you to use Python, but it is recommended.
* If you find bugs in the given code, PLEASE report the bug so that we can look into it. 

## Files

* `minesweeperAI1.py` - The code for the first AI algorithm you will write in `performAI()`. the `boardState` is what a person playing the game (your AI) would see, where `-1` are squares that have yet to be opened. `0-8` indicates a square that has been opened and the number of bombs adjacent to the square.
* `minesweeperAI2.py` - The code for the second AI algorithm you will write. Similar to `minesweeperAI1.py`. Note that both AIs come with a naïve algorithm that performs random guessing. 
* `minesweeperGameEngine.py` - A GUI game engine for the Minesweeper game.
  * It takes one argument, `-f`, to indicate the json config file to use for the game. The interface has two buttons (AI1 and AI2), and clicking the button once will execute `performAI` once in the respective AI file. You can also play the game manually by clicking on the buttons, but switching between manual play and AI for the same game can lead to errors. 
  * The blue square is the NEXT square your AI will open based on the current board layout, which was determined in the previous iteration of pressing the button. In other words, whenever you press an AI button, the blue square will first open, then the board with the opened blue square is passed to `performAI()`, and then your AI algorithm will determine the next best square to open.
* `minesweeperPerformanceTest.py` - A script where you can specify the board size, number of bombs, safe starting square, the type of AI to use (1 or 2), and the number of games to play. This script will generate a random game board with your configuration and use the AI specified to run the game and determine the number of games you played. Please look at the bottom of the file to understand this in more detail.
* `deterministic_board.json` - An (example) json config file that can be passed to `minesweeperGameEngine.py`.



## How to run

* Make sure all files are in the same directory
* Make sure you have `python3` installed (`python2` will most likely not work). Make sure you have common libraries installed, including `numpy` and `tk`. If you run the program and receive some import error, you are most likely missing a library, which can be downloaded fairly simply through a quick google search. Please let us know if you are unable to run the files on Piazza.
* On command prompt/anaconda/terminal, type and enter `python3 minesweeperGameEngine.py`. Depending on how you installed python, if that does not work, try `python minesweeperGameEngine.py`. A GUI should appear, and clicking either button will run through the algorithm. 
  *  You can also run, for example, `python3 minesweeperGameEngine.py -f deterministic_board.json`, which will use that json file. The default is `test_board.json`
* On command prompt/anaconda/terminal, type and enter `python3 minesweeperPerformanceTest.py`. Depending on how you installed python, if that does not work, try `python minesweeperPerformanceTest.py`. No GUI will appear, but some games will be automatically ran, and you will get a quick summary of how many were won and lost.
  * You can also run, for example, `python3 minesweeperPerformanceTest.py -g 15 16 17 0 3 1 10 `, which indicates 10 randomly generated gameboard of size $15 \times 16$ with 17 bombs and a safe square of (0, 3). Each gameboard will be solved independently using your first (1) algorithm.
  * You run also run, for example, `python3 minesweeperPerformanceTest.py -f deterministic_board.json 2`, which will use the given board json and your second (2) algorithm.  

## AI code specifications

* Please use the comments, the sample AI, and print statements to help understand the format, but briefly, you will be given the current state of the game board and must decide whether to:
  * 1) open up another square
  * 2) submit your answer (the locations of all bombs) 
* The game can end in 2 ways:
  * you returned a list of bomb locations, but the set of bombs did not match the real locations of the bombs (incorrect)
  * you returned a list of bomb locations, and the list matched the real locations of the bombs (correct)