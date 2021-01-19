from cubies import Corner, Edge
from re import sub


class Cube:

    def __init__(self):
        self.corners = []
        self.edges = []
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

    def __rotate(self, type, a, b, c, d, direction):
        if type == 'c':
            target = self.corners
        else:
            target = self.edges
        temp = target[a]
        target[a] = target[b]
        target[b] = target[c]
        target[c] = target[d]
        target[d] = temp
        target[a].rotate(direction)
        target[b].rotate(direction)
        target[c].rotate(direction)
        target[d].rotate(direction)

    def u(self):
        self.__rotate('e', 0, 3, 2, 1, 'y')
        self.__rotate('c', 0, 3, 2, 1, 'y')

    def r(self):
        self.__rotate('e', 1, 6, 9, 5, 'x')
        self.__rotate('c', 2, 6, 5, 1, 'x')

    def f(self):
        self.__rotate('e', 2, 7, 10, 6, 'z')
        self.__rotate('c', 3, 7, 6, 2, 'z')

    def di(self):
        self.__rotate('e', 8, 11, 10, 9, 'y')
        self.__rotate('c', 4, 7, 6, 5, 'y')

    def li(self):
        self.__rotate('e', 3, 7, 11, 4, 'x')
        self.__rotate('c', 3, 7, 4, 0, 'x')

    def bi(self):
        self.__rotate('e', 0, 4, 8, 5, 'z')
        self.__rotate('c', 0, 4, 5, 1, 'z')

    def ui(self):
        for x in range(3):
            self.u()

    def ri(self):
        for x in range(3):
            self.r()

    def fi(self):
        for x in range(3):
            self.f()

    def d(self):
        for x in range(3):
            self.di()

    def l(self):
        for x in range(3):
            self.li()

    def b(self):
        for x in range(3):
            self.bi()

    def u2(self):
        for x in range(2):
            self.u()

    def r2(self):
        for x in range(2):
            self.r()

    def f2(self):
        for x in range(2):
            self.f()

    def d2(self):
        for x in range(2):
            self.di()

    def l2(self):
        for x in range(2):
            self.li()

    def b2(self):
        for x in range(2):
            self.bi()

    def print(self, colored=False):
        c = self.corners
        e = self.edges
        cubestring = ''
        cubestring += '      {} {} {}\n'.format(c[0].faces['U'], e[0].faces['U'], c[1].faces['U'])
        cubestring += '      {}   {}\n'.format(e[3].faces['U'], e[1].faces['U'])
        cubestring += '      {} {} {}\n'.format(c[3].faces['U'], e[2].faces['U'], c[2].faces['U'])
        cubestring += '{} {} {} {} {} {} {} {} {} {} {} {}\n'.format(c[0].faces['L'], e[3].faces['L'], c[3].faces['L'],
                                                                     c[3].faces['F'], e[2].faces['F'], c[2].faces['F'],
                                                                     c[2].faces['R'], e[1].faces['R'], c[1].faces['R'],
                                                                     c[1].faces['B'], e[0].faces['B'], c[0].faces['B'])
        cubestring += '{}   {} {}   {} {}   {} {}   {}\n'.format(e[4].faces['L'], e[7].faces['L'],
                                                                 e[7].faces['F'], e[6].faces['F'],
                                                                 e[6].faces['R'], e[5].faces['R'],
                                                                 e[5].faces['B'], e[4].faces['B'])
        cubestring += '{} {} {} {} {} {} {} {} {} {} {} {}\n'.format(c[4].faces['L'], e[11].faces['L'], c[7].faces['L'],
                                                                     c[7].faces['F'], e[10].faces['F'], c[6].faces['F'],
                                                                     c[6].faces['R'], e[9].faces['R'], c[5].faces['R'],
                                                                     c[5].faces['B'], e[8].faces['B'], c[4].faces['B'])
        cubestring += '      {} {} {}\n'.format(c[7].faces['D'], e[10].faces['D'], c[6].faces['D'])
        cubestring += '      {}   {}\n'.format(e[11].faces['D'], e[9].faces['D'])
        cubestring += '      {} {} {}\n'.format(c[4].faces['D'], e[8].faces['D'], c[5].faces['D'])
        if colored:
            cubestring = sub('([A-D])', '\033[97m\u2588', cubestring)
            cubestring = sub('([E-H])', '\033[33m\u2588', cubestring)
            cubestring = sub('([I-L])', '\033[92m\u2588', cubestring)
            cubestring = sub('([M-P])', '\033[91m\u2588', cubestring)
            cubestring = sub('([Q-T])', '\033[94m\u2588', cubestring)
            cubestring = sub('([U-X])', '\033[93m\u2588', cubestring)
        print(cubestring)
        print('\033[37m')

    def perform_algo(self, algo):
        moves = algo.split(' ')
        switcher = {
            'L': self.l,
            'R': self.r,
            'F': self.f,
            'B': self.b,
            'U': self.u,
            'D': self.d,
            'L\'': self.li,
            'R\'': self.ri,
            'F\'': self.fi,
            'B\'': self.bi,
            'U\'': self.ui,
            'D\'': self.di,
            'L2': self.l2,
            'R2': self.r2,
            'F2': self.f2,
            'B2': self.b2,
            'U2': self.u2,
            'D2': self.d2
        }
        for move in moves:
            func = switcher.get(move, lambda: "Invalid move")
            func()
