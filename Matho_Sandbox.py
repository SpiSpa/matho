import numpy as np
import matplotlib.pyplot as plt

board = np.arange(1, 26)
print(board)

for i in range(30):
    np.random.shuffle(board)
    shuffledBoard = board.reshape(5, 5)
    print(shuffledBoard)
    print()