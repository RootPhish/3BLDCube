from cube import Cube

SetupMoves = {
    'H': "d L'",
    'J': "d2 L",
    'L': "L'",
    'S': "l' D' L2",
    'U': "D' l2"
}

UndoMoves = {
    'H': "L d'",
    'J': "L' d2",
    'L': "L",
    'S': "L2 D l",
    'U': "l2 D"
}

if __name__ == '__main__':
    cube = Cube()
    cube.perform_algo("D' U2 B F' U D B' L' D R2")
    cube.print(True)

    buffer = cube.edges[1].faces['U']
    while (buffer != 'B') and (buffer != 'M'):
        cube.perform_algo(SetupMoves[buffer])
        cube.perform_algo("R U R' U' R' F R2 U' R' U' R U R' F'")
        cube.perform_algo(UndoMoves[buffer])
        cube.print(True)
        buffer = cube.edges[1].faces['U']
