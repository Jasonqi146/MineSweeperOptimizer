import numpy as np
import random
import sys
sys.setrecursionlimit(1500)

class AI1():

    # Define settings upon initialization. Here you can specify
    def __init__(self, numRows, numCols, numBombs, safeSquare):   

        # game variables that can be accessed in any method in the class. For example, to access the number of rows, use "self.numRows" 
        self.numRows = numRows
        self.numCols = numCols
        self.numBombs = numBombs
        self.safeSquare = safeSquare
        self.bombsFoundByAlgo = set()

    def open_square_format(self, squareToOpen):
        return ("open_square", squareToOpen)

    def submit_final_answer_format(self, listOfBombs):
        return ("final_answer", listOfBombs)

    # return the square (r, c) you want to open based on the given boardState
    # the boardState will contain the value (0-8 inclusive) of the square, or -1 if that square is unopened
    # an AI example that returns a random square (r, c) that you want to open
    # TODO: implement a better algorithm
    def performAI(self, boardState):
        print(boardState)

        # find all the unopened squares
        unopenedSquares = []
        bombsFoundSoFar = set()
        bombsFoundSoFar = bombsFoundSoFar.union(self.bombsFoundByAlgo)
        for row in range(self.numRows):
            for col in range(self.numCols):
                if boardState[row][col] == -1:
                    unopenedSquares.append((row, col))
                elif boardState[row][col] == 9:
                    bombsFoundSoFar.add((row, col))
        print(f"List of bombs is {bombsFoundSoFar}")
        if len(list(bombsFoundSoFar)) == self.numBombs:
            # If the number of unopened squares is equal to the number of bombs, all squares must be bombs, and we can submit our answer
            print(f"List of bombs is {bombsFoundSoFar}")
            return self.submit_final_answer_format(list(bombsFoundSoFar))
        else:
            # Otherwise, pick a random square and open it 
            frontier = set()
            for row in range(self.numRows):
                for col in range(self.numCols):
                    is_frontier = False
                    if boardState[row][col] == -1:
                        pass
                    else:
                        neighbors = self.get_uopened_neighbors(row, col, boardState)
                        if len(neighbors) != 0:
                            is_frontier = True
                        if is_frontier:
                            frontier.add((row, col, boardState[row][col]))
            is_certain = False
            for f in frontier:
                neighbors = self.get_uopened_neighbors(f[0], f[1], boardState)
                #print(neighbors)
                count_unopened_neighbors = len(neighbors)
                count_visible_bomb = self.get_num_of_visible_bombs_around(f[0], f[1], boardState)
                count_known_bombs_around = self.get_num_of_bombs_around(row, col, bombsFoundSoFar)
                count_unvisible_bomb = count_known_bombs_around - count_visible_bomb
                if f[2] - count_known_bombs_around == count_unopened_neighbors - count_unvisible_bomb:
                    for r, c in neighbors:
                        bombsFoundSoFar.add((r,c))
                        self.bombsFoundByAlgo.add((r,c))
                '''
                if f[2] == 0 or f[2] - count_known_bombs_around == 0:
                    for r, c in neighbors:
                        if (r,c) not in bombsFoundSoFar:
                            squareToOpen = (r, c)
                            is_certain = True
                '''
            if is_certain == False:
                for i in bombsFoundSoFar:
                    if i in unopenedSquares and len(unopenedSquares) != 1:
                        unopenedSquares.remove(i)
                print(unopenedSquares)
                squareToOpen = random.choice(unopenedSquares)
            print(f"Square to open is {squareToOpen}")
            return self.open_square_format(squareToOpen)
            
        
    def get_uopened_neighbors(self, row, col, boardState):
        candidates = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                      (row    , col - 1),                 (row    , col + 1),
                      (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        result = []
        for i in candidates:
            if i[0] >= 0 and i[0] < self.numRows and i[1] >= 0 and i[1] < self.numCols and boardState[i[0]][i[1]] == -1:
                result.append((i[0], i[1]))
        return result

    def get_num_of_bombs_around(self, row, col, bombsFoundSoFar):
        candidates = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                      (row    , col - 1),                 (row    , col + 1),
                      (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        result = 0
        for i in candidates:
            if i[0] >= 0 and i[0] < self.numRows and i[1] >= 0 and i[1] < self.numCols and (i[0],i[1]) in bombsFoundSoFar:
                result += 1
        return result
        
    def get_num_of_visible_bombs_around(self, row, col, boardState):
        candidates = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                      (row    , col - 1),                 (row    , col + 1),
                      (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        result = 0
        for i in candidates:
            if i[0] >= 0 and i[0] < self.numRows and i[1] >= 0 and i[1] < self.numCols and boardState[i[0]][i[1]] == 9:
                result += 1
        return result