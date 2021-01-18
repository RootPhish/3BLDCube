class Cube:
    edges = []

    def __init__(self):
        for x in range(1, 25):
            self.edges.append(chr(x + 64))
