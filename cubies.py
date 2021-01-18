class Corner:
    def __init__(self, side1, label1, side2, label2, side3, label3):
        self.faces = {'U': '', 'D': '', 'F': '', 'B': '', 'L': '', 'R': ''}
        self.faces[side1] = label1
        self.faces[side2] = label2
        self.faces[side3] = label3

    def rotate(self, direction):
        if direction == 'z':
            temp = self.faces['B']
            self.faces['B'] = self.faces['L']
            self.faces['L'] = self.faces['F']
            self.faces['F'] = self.faces['R']
            self.faces['R'] = temp


class Edge:
    def __init__(self, side1, label1, side2, label2):
        self.faces = {'U': '', 'D': '', 'F': '', 'B': '', 'L': '', 'R': ''}
        self.faces[side1] = label1
        self.faces[side2] = label2

    def rotate(self, direction):
        if direction == 'z':
            temp = self.faces['B']
            self.faces['B'] = self.faces['L']
            self.faces['L'] = self.faces['F']
            self.faces['F'] = self.faces['R']
            self.faces['R'] = temp
