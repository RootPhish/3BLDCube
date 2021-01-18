from cube import Cube

if __name__ == '__main__':
    cube = Cube()
    for x in range(0, 6):
        cube.r()
        cube.u()
        cube.ri()
        cube.ui()
    cube.print(True)
