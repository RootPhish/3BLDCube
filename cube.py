from cubies import Corner, Edge


class Cube:

    def __init__(self):
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
        elif type == 'e':
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
        c = self.corners
        e = self.edges
        self.__rotate('e', 0, 3, 2, 1, 'z')
        self.__rotate('c', 0, 3, 2, 1, 'z')

    def ui(self):
        self.u()
        self.u()
        self.u()

    def print(self):
        c = self.corners
        e = self.edges
        print('      {} {} {}'.format(c[0].faces['U'], e[0].faces['U'], c[1].faces['U']))
        print('      {}   {}'.format(e[3].faces['U'], e[1].faces['U']))
        print('      {} {} {}'.format(c[3].faces['U'], e[2].faces['U'], c[2].faces['U']))
        print('{} {} {} {} {} {} {} {} {} {} {} {}'.format(c[0].faces['L'], e[3].faces['L'], c[3].faces['L'],
                                                           c[3].faces['F'], e[2].faces['F'], c[2].faces['F'],
                                                           c[2].faces['R'], e[1].faces['R'], c[1].faces['R'],
                                                           c[1].faces['B'], e[0].faces['B'], c[0].faces['B']))
        print('{}   {} {}   {} {}   {} {}   {}'.format(e[4].faces['L'], e[7].faces['L'],
                                                       e[7].faces['F'], e[6].faces['F'],
                                                       e[6].faces['R'], e[5].faces['R'],
                                                       e[5].faces['B'], e[4].faces['B']))
        print('{} {} {} {} {} {} {} {} {} {} {} {}'.format(c[4].faces['L'], e[11].faces['L'], c[7].faces['L'],
                                                           c[7].faces['F'], e[10].faces['F'], c[6].faces['F'],
                                                           c[6].faces['R'], e[9].faces['R'], c[5].faces['R'],
                                                           c[5].faces['B'], e[8].faces['B'], c[4].faces['B']))
        print('      {} {} {}'.format(c[7].faces['D'], e[10].faces['D'], c[6].faces['D']))
        print('      {}   {}'.format(e[11].faces['D'], e[9].faces['D']))
        print('      {} {} {}'.format(c[4].faces['D'], e[8].faces['D'], c[5].faces['D']))
