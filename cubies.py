class Cubie:

    def __init__(self):
        self.faces = {}

    def rotate(self, direction):
        if direction == 'y':
            temp = self.faces['B']
            self.faces['B'] = self.faces['L']
            self.faces['L'] = self.faces['F']
            self.faces['F'] = self.faces['R']
            self.faces['R'] = temp
        elif direction == 'x':
            temp = self.faces['F']
            self.faces['F'] = self.faces['D']
            self.faces['D'] = self.faces['B']
            self.faces['B'] = self.faces['U']
            self.faces['U'] = temp
        elif direction == 'z':
            temp = self.faces['U']
            self.faces['U'] = self.faces['L']
            self.faces['L'] = self.faces['D']
            self.faces['D'] = self.faces['R']
            self.faces['R'] = temp


class Corner(Cubie):
    def __init__(self, side1, label1, side2, label2, side3, label3):
        super().__init__()
        self.faces = {'U': '', 'D': '', 'F': '', 'B': '', 'L': '', 'R': '', side1: label1, side2: label2, side3: label3}


class Edge(Cubie):
    def __init__(self, side1, label1, side2, label2):
        super().__init__()
        self.faces = {'U': '', 'D': '', 'F': '', 'B': '', 'L': '', 'R': '', side1: label1, side2: label2}


class Center(Cubie):
    def __init__(self, side1, label1):
        super().__init__()
        self.faces = {'U': '', 'D': '', 'F': '', 'B': '', 'L': '', 'R': '', side1: label1}
