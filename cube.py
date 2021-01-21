from cubies import Corner, Edge, Center
from functools import partial
from re import sub


class Colors:
    def __init__(self):
        pass

    WHITE = '\033[97m'
    ORANGE = '\033[33m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'


CornerSetupMoves = {
    "A": "",
    "B": "R2",
    "C": "F2 D",
    "D": "F2",
    "E": "",
    "F": "F' D",
    "G": "F'",
    "H": "D' R",
    "I": "F R'",
    "J": "R'",
    "K": "F' R'",
    "L": "F2 R'",
    "M": "F",
    "N": "R' F",
    "O": "R2 F",
    "P": "R F",
    "Q": "R D'",
    "R": "",
    "S": "D F'",
    "T": "R",
    "U": "D",
    "V": "",
    "W": "D'",
    "X": "D2"
}

EdgeSetupMoves = {
    'A': "l2 D' l2",
    'B': "",
    'C': "l2 D l2",
    'D': "",
    'E': "L d' L",
    'F': "d' L",
    'G': "L' d' L",
    'H': "d L'",
    'I': "l D' L2",
    'J': "d2 L",
    'K': "l D L2",
    'L': "L'",
    'M': "",
    'N': "d L",
    'O': "D' l D L2",
    'P': "d' L'",
    'Q': "l' D L2",
    'R': "L",
    'S': "l' D' L2",
    'T': "d2 L'",
    'U': "D' l2",
    'V': "D2 L2",
    'W': "D L2",
    'X': "L2"
}


class Cube:

    def __init__(self):
        self.corners = []
        self.edges = []
        self.centers = []
        self.reset()

    def reset(self):
        self.corners = []
        self.corners.append(Corner('U', 'A', 'L', 'E', 'B', 'R'))
        self.corners.append(Corner('U', 'B', 'R', 'N', 'B', 'Q'))
        self.corners.append(Corner('U', 'C', 'R', 'M', 'F', 'J'))
        self.corners.append(Corner('U', 'D', 'L', 'F', 'F', 'I'))
        self.corners.append(Corner('D', 'X', 'L', 'H', 'B', 'S'))
        self.corners.append(Corner('D', 'W', 'R', 'O', 'B', 'T'))
        self.corners.append(Corner('D', 'V', 'R', 'P', 'F', 'K'))
        self.corners.append(Corner('D', 'U', 'L', 'G', 'F', 'L'))

        self.edges = []
        self.edges.append(Edge('U', 'A', 'B', 'Q'))
        self.edges.append(Edge('U', 'B', 'R', 'M'))
        self.edges.append(Edge('U', 'C', 'F', 'I'))
        self.edges.append(Edge('U', 'D', 'L', 'E'))
        self.edges.append(Edge('L', 'H', 'B', 'R'))
        self.edges.append(Edge('R', 'N', 'B', 'T'))
        self.edges.append(Edge('R', 'P', 'F', 'J'))
        self.edges.append(Edge('L', 'F', 'F', 'L'))
        self.edges.append(Edge('D', 'W', 'B', 'S'))
        self.edges.append(Edge('D', 'V', 'R', 'O'))
        self.edges.append(Edge('D', 'U', 'F', 'K'))
        self.edges.append(Edge('D', 'X', 'L', 'G'))

        self.centers = []
        self.centers.append(Center('U', 'A'))
        self.centers.append(Center('L', 'E'))
        self.centers.append(Center('F', 'I'))
        self.centers.append(Center('R', 'M'))
        self.centers.append(Center('B', 'Q'))
        self.centers.append(Center('D', 'U'))

    def __rotate(self, cubie_type, a, b, c, d, direction):
        if cubie_type == 'c':
            target = self.corners
        elif cubie_type == 'e':
            target = self.edges
        elif cubie_type == 'ce':
            target = self.centers
        else:
            return
        temp = target[a]
        target[a] = target[b]
        target[b] = target[c]
        target[c] = target[d]
        target[d] = temp
        target[a].rotate(direction)
        target[b].rotate(direction)
        target[c].rotate(direction)
        target[d].rotate(direction)

    def u(self, count=1):
        for _ in range(count):
            self.__rotate('e', 0, 3, 2, 1, 'y')
            self.__rotate('c', 0, 3, 2, 1, 'y')

    def r(self, count=1):
        for _ in range(count):
            self.__rotate('e', 1, 6, 9, 5, 'x')
            self.__rotate('c', 2, 6, 5, 1, 'x')

    def f(self, count=1):
        for _ in range(count):
            self.__rotate('e', 2, 7, 10, 6, 'z')
            self.__rotate('c', 3, 7, 6, 2, 'z')

    def d(self, count=3):
        for _ in range(count):
            self.__rotate('e', 8, 11, 10, 9, 'y')
            self.__rotate('c', 4, 7, 6, 5, 'y')

    def l(self, count=3):
        for _ in range(count):
            self.__rotate('e', 3, 7, 11, 4, 'x')
            self.__rotate('c', 3, 7, 4, 0, 'x')

    def b(self, count=3):
        for _ in range(count):
            self.__rotate('e', 0, 4, 8, 5, 'z')
            self.__rotate('c', 0, 4, 5, 1, 'z')

    def m(self, count=1):
        for _ in range(count):
            self.__rotate('e', 0, 2, 10, 8, 'x')
            self.__rotate('ce', 0, 2, 5, 4, 'x')

    def e(self, count=3):
        for _ in range(count):
            self.__rotate('e', 4, 7, 6, 5, 'y')
            self.__rotate('ce', 1, 2, 3, 4, 'y')

    def s(self, count=1):
        for _ in range(count):
            self.__rotate('e', 3, 11, 9, 1, 'z')
            self.__rotate('ce', 0, 1, 5, 3, 'z')

    def dw(self, count=3):
        self.d(count)
        self.e(count)

    def lw(self, count=3):
        self.l(count)
        self.m(count)

    def print(self, colored=False):
        c = self.corners
        e = self.edges
        ce = self.centers
        block = '\u2588'
        cubestring = ''
        cubestring += '      {} {} {}\n'.format(c[0].faces['U'], e[0].faces['U'], c[1].faces['U'])
        cubestring += '      {} {} {}\n'.format(e[3].faces['U'], ce[0].faces['U'], e[1].faces['U'])
        cubestring += '      {} {} {}\n'.format(c[3].faces['U'], e[2].faces['U'], c[2].faces['U'])
        cubestring += '{} {} {} {} {} {} {} {} {} {} {} {}\n'.format(c[0].faces['L'], e[3].faces['L'], c[3].faces['L'],
                                                                     c[3].faces['F'], e[2].faces['F'], c[2].faces['F'],
                                                                     c[2].faces['R'], e[1].faces['R'], c[1].faces['R'],
                                                                     c[1].faces['B'], e[0].faces['B'], c[0].faces['B'])
        cubestring += '{} {} {} {} {} {} {} {} {} {} {} {}\n'.format(e[4].faces['L'],
                                                                     ce[1].faces['L'],
                                                                     e[7].faces['L'], e[7].faces['F'],
                                                                     ce[2].faces['F'],
                                                                     e[6].faces['F'], e[6].faces['R'],
                                                                     ce[3].faces['R'], e[5].faces['R'],
                                                                     e[5].faces['B'],
                                                                     ce[4].faces['B'],
                                                                     e[4].faces['B'])
        cubestring += '{} {} {} {} {} {} {} {} {} {} {} {}\n'.format(c[4].faces['L'], e[11].faces['L'], c[7].faces['L'],
                                                                     c[7].faces['F'], e[10].faces['F'], c[6].faces['F'],
                                                                     c[6].faces['R'], e[9].faces['R'], c[5].faces['R'],
                                                                     c[5].faces['B'], e[8].faces['B'], c[4].faces['B'])
        cubestring += '      {} {} {}\n'.format(c[7].faces['D'], e[10].faces['D'], c[6].faces['D'])
        cubestring += '      {} {} {}\n'.format(e[11].faces['D'], ce[5].faces['D'], e[9].faces['D'])
        cubestring += '      {} {} {}\n'.format(c[4].faces['D'], e[8].faces['D'], c[5].faces['D'])
        if colored:
            cubestring = sub('([A-D])', Colors.WHITE + block + Colors.RESET, cubestring)
            cubestring = sub('([E-H])', Colors.ORANGE + block + Colors.RESET, cubestring)
            cubestring = sub('([I-L])', Colors.GREEN + block + Colors.RESET, cubestring)
            cubestring = sub('([M-P])', Colors.RED + block + Colors.RESET, cubestring)
            cubestring = sub('([Q-T])', Colors.BLUE + block + Colors.RESET, cubestring)
            cubestring = sub('([U-X])', Colors.YELLOW + block + Colors.RESET, cubestring)
            cubestring += '\033[0m'
        print(cubestring)

    def perform_algo(self, algo):
        moves = algo.split(' ')
        switcher = {
            'R': partial(self.r, 1),
            'F': partial(self.f, 1),
            'U': partial(self.u, 1),
            'D': partial(self.d, 3),
            'L': partial(self.l, 3),
            'B': partial(self.b, 3),
            'R\'': partial(self.r, 3),
            'F\'': partial(self.f, 3),
            'U\'': partial(self.u, 3),
            'D\'': partial(self.d, 1),
            'L\'': partial(self.l, 1),
            'B\'': partial(self.b, 1),
            'L2': partial(self.l, 2),
            'R2': partial(self.r, 2),
            'F2': partial(self.f, 2),
            'B2': partial(self.b, 2),
            'U2': partial(self.u, 2),
            'D2': partial(self.d, 2),
            'M': partial(self.m, 3),
            'M\'': partial(self.m, 1),
            'M2': partial(self.m, 2),
            'E': partial(self.e, 3),
            'E\'': partial(self.e, 1),
            'E2': partial(self.e, 2),
            'S': partial(self.s, 1),
            'S\'': partial(self.s, 3),
            'S2': partial(self.s, 2),
            'd': partial(self.dw, 3),
            'd\'': partial(self.dw, 1),
            'd2': partial(self.dw, 2),
            'l': partial(self.lw, 3),
            'l\'': partial(self.lw, 1),
            'l2': partial(self.lw, 2)
        }
        for move in moves:
            func = switcher.get(move, lambda: "Invalid move")
            func()

    @staticmethod
    def reverse_algo(algo):
        if algo == '':
            return ''
        moves = algo.split(' ')
        moves.reverse()
        new_moves = []
        for move in moves:
            if move[-1] == '2':
                new_moves.append(move)
            elif move[-1] == "'":
                new_moves.append(move[0])
            else:
                new_moves.append(move[0] + "'")
        return " ".join(new_moves)

    def perform_reverse(self, algo):
        self.perform_algo(self.reverse_algo(algo))

    def find_first_unsolved_edge(self):
        solved_cube = Cube()
        for x in range(0, 24):
            for counter in range(len(self.edges)):
                if chr(x + 65) in self.edges[counter].faces.values():
                    if (not self.edges[counter].compare(solved_cube.edges[counter])) and (chr(x + 65) != 'B') and (
                            chr(x + 65) != 'M'):
                        return chr(x + 65)

    def find_first_unsolved_corner(self):
        solved_cube = Cube()
        for x in range(0, 24):
            for counter in range(len(self.corners)):
                if chr(x + 65) in self.corners[counter].faces.values():
                    if (not self.corners[counter].compare(solved_cube.corners[counter])) and (chr(x + 65) != 'A') and (
                            chr(x + 65) != 'E') and (chr(x + 65) != 'R'):
                        return chr(x + 65)

    def edges_solved(self):
        solved_cube = Cube()
        for x in range(len(self.edges)):
            if not self.edges[x].compare(solved_cube.edges[x]):
                return False
        return True

    def corners_solved(self):
        solved_cube = Cube()
        for x in range(len(self.corners)):
            if not self.corners[x].compare(solved_cube.corners[x]):
                return False
        return True
