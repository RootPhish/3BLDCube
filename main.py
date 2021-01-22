from cube import Cube, EdgeSetupMoves, CornerSetupMoves

if __name__ == '__main__':
    cube = Cube()
    cube.perform_algo("B F2 L R2 D U F' U L2 B")
    cube.print(True)

    letterSequence = ''


    def move_piece(cubie_type, letter):
        if cubie_type == 'e':
            setup_moves = EdgeSetupMoves
            algo = "R U R' U' R' F R2 U' R' U' R U R' F'"
        else:
            setup_moves = CornerSetupMoves
            algo = "R U' R' U' R U R' F' R U R' U' R' F R"
        cube.perform_algo(setup_moves[letter])
        cube.perform_algo(algo)
        cube.perform_reverse(setup_moves[letter])


    while not cube.edges_solved():
        buffer = cube.edges[1].faces['U']
        while (buffer != 'B') and (buffer != 'M'):
            letterSequence += buffer
            move_piece('e', buffer)
            buffer = cube.edges[1].faces['U']

        edge = cube.find_first_unsolved_edge()
        if edge != '' and edge is not None:
            letterSequence += ' '
            letterSequence += edge
            move_piece('e', edge)

    print(letterSequence)

    letterSequence = ''
    while not cube.corners_solved():
        buffer = cube.corners[0].faces['L']
        while (buffer != 'A') and (buffer != 'E') and (buffer != 'R'):
            letterSequence += buffer
            move_piece('c', buffer)
            buffer = cube.corners[0].faces['L']

        corner = cube.find_first_unsolved_corner()
        if corner != '' and corner is not None:
            letterSequence += ' '
            letterSequence += corner
            move_piece('c', corner)

    print(letterSequence)
    cube.print(True)
