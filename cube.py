class Cube:

    def __init__(self):
        self.edges = {}
        self.corners = {}
        for x in range(1, 25):
            self.edges[chr(x + 64)] = chr(x + 64)
            self.corners[chr(x + 64)] = chr(x + 64)

    def __rotate_edges(self, a, b, c, d):
        temp = self.edges[a]
        self.edges[a] = self.edges[b]
        self.edges[b] = self.edges[c]
        self.edges[c] = self.edges[d]
        self.edges[d] = temp

    def __rotate_corners(self, a, b, c, d):
        temp = self.corners[a]
        self.corners[a] = self.corners[b]
        self.corners[b] = self.corners[c]
        self.corners[c] = self.corners[d]
        self.corners[d] = temp

    def print(self):
        c = self.corners
        e = self.edges
        print('      {} {} {}'.format(c['A'], e['A'], c['B']))
        print('      {} {} {}'.format(e['D'], ' ', e['B']))
        print('      {} {} {}'.format(c['D'], e['C'], c['C']))
        print('{} {} {} {} {} {} {} {} {} {} {} {}'.format(c['E'], e['E'], c['F'], c['I'], e['I'], c['J'], c['M'], e['M'], c['N'], c['Q'], e['Q'], c['R']))
        print('{} {} {} {} {} {} {} {} {} {} {} {}'.format(e['H'], ' ', e['F'], e['L'], ' ', e['J'], e['P'], ' ', e['N'], e['T'], ' ', e['R']))
        print('{} {} {} {} {} {} {} {} {} {} {} {}'.format(c['H'], e['G'], c['G'], c['L'], e['K'], c['K'], c['P'], e['O'], c['O'], c['T'], e['S'], c['S']))
        print('      {} {} {}'.format(c['U'], e['U'], c['V']))
        print('      {} {} {}'.format(e['X'], ' ', e['V']))
        print('      {} {} {}'.format(c['X'], e['W'], c['W']))

    def u(self):
        self.__rotate_edges('D', 'C', 'B', 'A')
        self.__rotate_corners('D', 'C', 'B', 'A')
