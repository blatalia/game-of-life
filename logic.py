import numpy as np

width_random = 100
height_random = 100
random_drawing = np.random.choice([0, 1], size = (height_random, width_random))

with open("sample_patterns\\glider.txt") as glide:
    
    glider = glide.read()
    glider = glider.replace("", " ")[1: -1]
    glider = glider.replace(".", "0")
    glider = glider.replace("X", "1")

    glider_matrix = np.matrix(glider)
    glider_matrix = np.reshape(glider_matrix, (31, 100))
    height_glider = glider_matrix.shape[0]
    width_glider = glider_matrix.shape[1]

with open("sample_patterns\\pulsar.txt") as pulse:
    
    pulsar = pulse.read()
    pulsar = pulsar.replace("", " ")[1: -1]
    pulsar = pulsar.replace(".", "0")
    pulsar = pulsar.replace("X", "1")

    pulsar_matrix = np.matrix(pulsar)
    pulsar_matrix = np.reshape(pulsar_matrix, (30, 100))
    height_pulsar = pulsar_matrix.shape[0]
    width_pulsar = pulsar_matrix.shape[1]

with open("sample_patterns\\gosper-glider-gun.txt") as gosp:
    gosper = gosp.read()
    gosper = gosper.replace("", " ")[1: -1]
    gosper = gosper.replace(".", "0")
    gosper = gosper.replace("X", "1")

    gosper_matrix = np.matrix(gosper)
    gosper_matrix = np.reshape(gosper_matrix, (31, 100))
    height_gosper = gosper_matrix.shape[0]
    width_gosper = gosper_matrix.shape[1]

def gameoflife(board, height, width):
    update = np.zeros((board.shape[0]+2, board.shape[1]+2), dtype=int)
    board_expanded = np.pad(board, 1, mode='constant', constant_values=0)
    roll = [-1, 0, 1]

    for x in roll:
        for y in roll:
            if x != 0 or y != 0:
                update += np.roll(board_expanded, (x, y), (0, 1))

    update = np.delete(update, (0, height+1), axis = 0) 
    update = np.delete(update, (0, width+1), axis = 1) 

    board[(update != 2) & (update != 3)] = 0 
    board[update == 3] = 1 
    return board