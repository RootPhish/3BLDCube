from cube import Cube, EdgeSetupMoves, CornerSetupMoves

if __name__ == '__main__':
    cube = Cube()
    cube.perform_algo("F' L2 D2 U F' U B2 F2 L2 R'")
    cube.print(True)

    letterSequence = ''

    while not cube.edges_solved():
        buffer = cube.edges[1].faces['U']
        while (buffer != 'B') and (buffer != 'M'):
            letterSequence += buffer
            cube.perform_algo(EdgeSetupMoves[buffer])
            cube.perform_algo("R U R' U' R' F R2 U' R' U' R U R' F'")
            cube.perform_reverse(EdgeSetupMoves[buffer])
            buffer = cube.edges[1].faces['U']

        edge = cube.find_first_unsolved_edge()
        if edge != '' and edge is not None:
            letterSequence += edge
            cube.perform_algo(EdgeSetupMoves[edge])
            cube.perform_algo("R U R' U' R' F R2 U' R' U' R U R' F'")
            cube.perform_reverse(EdgeSetupMoves[edge])

    print(letterSequence)

    letterSequence = ''
    while not cube.corners_solved():
        buffer = cube.corners[0].faces['L']
        while (buffer != 'A') and (buffer != 'E') and (buffer != 'R'):
            letterSequence += buffer
            cube.perform_algo(CornerSetupMoves[buffer])
            cube.perform_algo("R U' R' U' R U R' F' R U R' U' R' F R")
            cube.perform_reverse(CornerSetupMoves[buffer])
            buffer = cube.corners[0].faces['L']

        corner = cube.find_first_unsolved_corner()
        if corner != '' and corner is not None:
            letterSequence += corner
            cube.perform_algo(CornerSetupMoves[corner])
            cube.perform_algo("R U' R' U' R U R' F' R U R' U' R' F R")
            cube.perform_reverse(CornerSetupMoves[corner])

    print(letterSequence)
    cube.print(True)