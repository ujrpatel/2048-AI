import math
import time
import numpy as np

UP, DOWN, LEFT, RIGHT = range(4)

class AI():

    #returns the best move depending on the values
    #   can be maximised.
    def get_move(self, board):
        best_move, _ = self.maximize(board)
        return best_move

    #smoothness function, best way of keeping the grid in ascending order
    def eval_board(self, board, n_empty): 
        grid = board.grid

        utility = 0
        smoothness = 0

        big_t = np.sum(np.power(grid, 2))
        s_grid = np.sqrt(grid)

        #calculating the smoothness for every tile on the board and its corresponing tiles
        smoothness -= np.sum(np.abs(s_grid[::,0] - s_grid[::,1]))
        smoothness -= np.sum(np.abs(s_grid[::,1] - s_grid[::,2]))
        smoothness -= np.sum(np.abs(s_grid[::,2] - s_grid[::,3]))
        smoothness -= np.sum(np.abs(s_grid[0,::] - s_grid[1,::]))
        smoothness -= np.sum(np.abs(s_grid[1,::] - s_grid[2,::]))
        smoothness -= np.sum(np.abs(s_grid[2,::] - s_grid[3,::]))
        
        #predefined values
        empty_w = 100000
        smoothness_w = 3

        #this calulates the tile utility which are functions of the
        #   smoothness of the board
        empty_u = n_empty * empty_w
        smooth_u = smoothness ** smoothness_w
        big_t_u = big_t

        utility += big_t
        utility += empty_u
        utility += smooth_u

        #this returns the utilities
        return (utility, empty_u, smooth_u, big_t_u)


    #this is function that returns the best move direction along with the highest utility
    def maximize(self, board, depth = 0):
        moves = board.get_available_moves()
        moves_boards = []

        #gets all possible moves
        for m in moves:
            m_board = board.clone()
            m_board.move(m)
            moves_boards.append((m, m_board))

        max_utility = (float('-inf'),0,0,0)
        best_direction = None

        #calculating the max utility
        for mb in moves_boards:
            utility = self.chance(mb[1], depth + 1)

            if utility[0] >= max_utility[0]:
                max_utility = utility
                best_direction = mb[0]

        return best_direction, max_utility

    #resposible for calulating the best utility given
    #   the number of empty spaces
    def chance(self, board, depth = 0):
        empty_cells = board.get_available_cells()
        n_empty = len(empty_cells)

#//     depth calculation for the board
        if n_empty >= 6 and depth >= 3:
            return self.eval_board(board, n_empty)

        if n_empty >= 0 and depth >= 5:
            return self.eval_board(board, n_empty)

        if n_empty == 0:
            _, utility = self.maximize(board, depth + 1)
            return utility

        possible_tiles = []

        #chance of the 2 and 4 tile being produced
        chance_2 = (.9 * (1 / n_empty))
        chance_4 = (.1 * (1 / n_empty))
        
        #spawing a tile 10% for 4 and 90% for 2 
        for empty_cell in empty_cells:
            possible_tiles.append((empty_cell, 2, chance_2))
            possible_tiles.append((empty_cell, 4, chance_4))

        utility_sum = [0, 0, 0, 0]

        #for every possilbe cell and all the possible spawns 
        #   this calulates the best utility on a clone 
        #   of the board
        for t in possible_tiles:
            t_board = board.clone()
            t_board.insert_tile(t[0], t[1])
            _, utility = self.maximize(t_board, depth + 1)

            for i in range(4):
                utility_sum[i] += utility[i] * t[2]

        return tuple(utility_sum)



#//        #if n_empty >= 7 and depth >= 5:
        #    return self.eval_board(board, n_empty)