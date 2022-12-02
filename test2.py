from fifteen_puzzle_solvers.puzzle import Puzzle
from fifteen_puzzle_solvers.algorithms import AStar, BreadthFirst
from fifteen_puzzle_solvers.solver import PuzzleSolver

puzzle = Puzzle([[14,1,0,15], [11,8,9,3], [5,10,7,12], [4,2,6,13]])

for strategy in [AStar]:
    puzzle_solver = PuzzleSolver(strategy(puzzle))
    puzzle_solver.run()
    puzzle_solver.print_performance()
    puzzle_solver.print_solution()