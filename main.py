

import numpy as np










def solvedState():
    state=np.empty((6,3,3), dtype='<U1')
    faceColors=['Y', 'R', 'W', 'O', 'B', 'G']
    for i, color in enumerate(faceColors):
        state[i, :, :] = color

    return state










class Cube:
    def __init__(self, stateData) -> None:
        self.state=np.array(stateData)

    def reset(self):
        faceColors = ['Y','R', 'W', 'O', 'B', 'G']

        for i, color in enumerate(faceColors):
            self.state[i, :, :] = color

    def printState(self):
        face_names = ["Top (Yellow)", "Front (Red)", "Bottom (White)", "Back (Orange)", "Left (Blue)", "Right (Green)"]
        print("printing the current state of the cube: ")
        print()
        for i, face in enumerate(self.state):
            print(f"--- {face_names[i]} (Index {i}) ---")
            print(face)
            print()

    def isValidState(self):
        allStickers=np.array(self.state).flatten()
        unique, counts = np.unique(allStickers, return_counts=True)
        countDict=dict(zip(unique, counts))

        if len(unique)==6 and all(c==9 for c in counts):
            return True
        
        print(f"Invalid State: {countDict}")
        return False

    def moveRed(self, clockWise=True):
        temp = np.array([self.state[0][2][0], self.state[0][2][1], self.state[0][2][2]])

        if clockWise:
            self.state[1] = np.rot90(self.state[1], k=-1)
            self.state[0][2][0], self.state[0][2][1], self.state[0][2][2] = self.state[4][2][2], self.state[4][1][2], self.state[4][0][2]
            self.state[4][2][2], self.state[4][1][2], self.state[4][0][2] = self.state[2][0][2], self.state[2][0][1], self.state[2][0][0]
            self.state[2][0][2], self.state[2][0][1], self.state[2][0][0] = self.state[5][0][0], self.state[5][1][0], self.state[5][2][0]
            self.state[5][0][0], self.state[5][1][0], self.state[5][2][0] = temp[2], temp[1], temp[0]
        else:
            self.state[1] = np.rot90(self.state[1], k=1)
            self.state[0][2][0], self.state[0][2][1], self.state[0][2][2] = self.state[5][0][0], self.state[5][1][0], self.state[5][2][0]
            self.state[5][0][0], self.state[5][1][0], self.state[5][2][0] = self.state[2][0][2], self.state[2][0][1], self.state[2][0][0]
            self.state[2][0][2], self.state[2][0][1], self.state[2][0][0] = self.state[4][2][2], self.state[4][1][2], self.state[4][0][2]
            self.state[4][2][2], self.state[4][1][2], self.state[4][0][2] = temp[0], temp[1], temp[2]

    def moveYellow(self, clockWise=True):
        temp = np.array([self.state[3][2][0], self.state[3][2][1], self.state[3][2][2]])

        if clockWise:
            self.state[0] = np.rot90(self.state[0], k=-1)
            self.state[3][2][0], self.state[3][2][1], self.state[3][2][2] = self.state[4][0][2], self.state[4][0][1], self.state[4][0][0]
            self.state[4][0][2], self.state[4][0][1], self.state[4][0][0] = self.state[1][0][2], self.state[1][0][1], self.state[1][0][0]
            self.state[1][0][2], self.state[1][0][1], self.state[1][0][0] = self.state[5][0][2], self.state[5][0][1], self.state[5][0][0]
            self.state[5][0][2], self.state[5][0][1], self.state[5][0][0] = temp[0], temp[1], temp[2]
        else:
            self.state[0] = np.rot90(self.state[0], k=1)
            self.state[3][2][0], self.state[3][2][1], self.state[3][2][2] = self.state[5][0][2], self.state[5][0][1], self.state[5][0][0]
            self.state[5][0][2], self.state[5][0][1], self.state[5][0][0] = self.state[1][0][2], self.state[1][0][1], self.state[1][0][0]
            self.state[1][0][2], self.state[1][0][1], self.state[1][0][0] = self.state[4][0][2], self.state[4][0][1], self.state[4][0][0]
            self.state[4][0][2], self.state[4][0][1], self.state[4][0][0] = temp[0], temp[1], temp[2]

    def moveWhite(self, clockWise=True):
        temp = np.array([self.state[1][2][0], self.state[1][2][1], self.state[1][2][2]])

        if clockWise:
            self.state[2] = np.rot90(self.state[2], k=-1)
            self.state[1][2][0], self.state[1][2][1], self.state[1][2][2] = self.state[4][2][0], self.state[4][2][1], self.state[4][2][2]
            self.state[4][2][0], self.state[4][2][1], self.state[4][2][2] = self.state[3][0][2], self.state[3][0][1], self.state[3][0][0]
            self.state[3][0][0], self.state[3][0][1], self.state[3][0][2] = self.state[5][2][2], self.state[5][2][1], self.state[5][2][0]
            self.state[5][2][0], self.state[5][2][1], self.state[5][2][2] = temp[0], temp[1], temp[2]
        else:
            self.state[2] = np.rot90(self.state[2], k=1)
            self.state[1][2][0], self.state[1][2][1], self.state[1][2][2] = self.state[5][2][0], self.state[5][2][1], self.state[5][2][2]
            self.state[5][2][0], self.state[5][2][1], self.state[5][2][2] = self.state[3][0][2], self.state[3][0][1], self.state[3][0][0]
            self.state[3][0][0], self.state[3][0][1], self.state[3][0][2] = self.state[4][2][2], self.state[4][2][1], self.state[4][2][0]
            self.state[4][2][0], self.state[4][2][1], self.state[4][2][2] = temp[0], temp[1], temp[2]
    def moveOrange(self, clockWise=True):
        temp = np.array([self.state[0][0][0], self.state[0][0][1], self.state[0][0][2]])

        if clockWise:
            self.state[3] = np.rot90(self.state[3], k=-1)
            self.state[0][0][0], self.state[0][0][1], self.state[0][0][2] = self.state[5][0][2], self.state[5][1][2], self.state[5][2][2]
            self.state[5][0][2], self.state[5][1][2], self.state[5][2][2] = self.state[2][2][2], self.state[2][2][1], self.state[2][2][0]
            self.state[2][2][0], self.state[2][2][1], self.state[2][2][2] = self.state[4][0][0], self.state[4][1][0], self.state[4][2][0]
            self.state[4][0][0], self.state[4][1][0], self.state[4][2][0] = temp[2], temp[1], temp[0]
        else:
            self.state[3] = np.rot90(self.state[3], k=1)
            self.state[0][0][0], self.state[0][0][1], self.state[0][0][2] = self.state[4][2][0], self.state[4][1][0], self.state[4][0][0]
            self.state[4][0][0], self.state[4][1][0], self.state[4][2][0] = self.state[2][2][0], self.state[2][2][1], self.state[2][2][2]
            self.state[2][2][0], self.state[2][2][1], self.state[2][2][2] = self.state[5][2][2], self.state[5][1][2], self.state[5][0][2]
            self.state[5][0][2], self.state[5][1][2], self.state[5][2][2] = temp[0], temp[1], temp[2]



    def moveGreen(self, clockWise=True):
        temp = np.array([self.state[0][0][2], self.state[0][1][2], self.state[0][2][2]])

        if clockWise:
            self.state[5] = np.rot90(self.state[5], k=-1)
            self.state[0][0][2], self.state[0][1][2], self.state[0][2][2] = self.state[1][0][2], self.state[1][1][2], self.state[1][2][2]
            self.state[1][0][2], self.state[1][1][2], self.state[1][2][2] = self.state[2][0][2], self.state[2][1][2], self.state[2][2][2]
            self.state[2][0][2], self.state[2][1][2], self.state[2][2][2] = self.state[3][2][0], self.state[3][1][0], self.state[3][0][0]
            self.state[3][0][2], self.state[3][1][2], self.state[3][2][2] = temp[2], temp[1], temp[0]
        else:
            self.state[5] = np.rot90(self.state[5], k=1)
            self.state[0][0][2], self.state[0][1][2], self.state[0][2][2] = self.state[3][2][0], self.state[3][1][0], self.state[3][0][0]
            self.state[3][0][2], self.state[3][1][2], self.state[3][2][2] = self.state[2][2][2], self.state[2][1][2], self.state[2][0][2]
            self.state[2][0][2], self.state[2][1][2], self.state[2][2][2] = self.state[1][0][2], self.state[1][1][2], self.state[1][2][2]
            self.state[1][0][2], self.state[1][1][2], self.state[1][2][2] = temp[0], temp[1], temp[2]


    def moveBlue(self, clockWise=True):
        temp = np.array([self.state[0][0][0], self.state[0][1][0], self.state[0][2][0]])

        if clockWise:
            self.state[4] = np.rot90(self.state[4], k=-1)
            self.state[0][0][0], self.state[0][1][0], self.state[0][2][0] = self.state[3][0][0], self.state[3][1][0], self.state[3][2][0]
            self.state[3][0][0], self.state[3][1][0], self.state[3][2][0] = self.state[2][0][0], self.state[2][1][0], self.state[2][2][0]
            self.state[2][0][0], self.state[2][1][0], self.state[2][2][0] = self.state[1][0][0], self.state[1][1][0], self.state[1][2][0]
            self.state[1][0][0], self.state[1][1][0], self.state[1][2][0] = temp[0], temp[1], temp[2]
        else:
            self.state[4] = np.rot90(self.state[4], k=1)
            self.state[0][0][0], self.state[0][1][0], self.state[0][2][0] = self.state[1][0][0], self.state[1][1][0], self.state[1][2][0]
            self.state[1][0][0], self.state[1][1][0], self.state[1][2][0] = self.state[2][0][0], self.state[2][1][0], self.state[2][2][0]
            self.state[2][0][0], self.state[2][1][0], self.state[2][2][0] = self.state[3][2][2], self.state[3][1][2], self.state[3][0][2]
            self.state[3][0][0], self.state[3][1][0], self.state[3][2][0] = temp[2], temp[1], temp[0]






class Solver:
    def __init__(self) -> None:
        self.myCube=Cube(inputState())
        self.orientationMap = {
            # --- Standard Side Faces ---
            'r': {'R': 'g', 'U': 'y', 'L': 'b', 'D': 'w'}, 
            'o': {'R': 'b', 'U': 'y', 'L': 'g', 'D': 'w'},
            'g': {'R': 'o', 'U': 'y', 'L': 'r', 'D': 'w'},
            'b': {'R': 'r', 'U': 'y', 'L': 'o', 'D': 'w'},
            # --- Yellow Faces (Top) ---
            'yo': {'R': 'g', 'U': 'o', 'L': 'b', 'D': 'r'},
            'yb': {'R': 'o', 'U': 'b', 'L': 'r', 'D': 'g'},
            'yr': {'R': 'b', 'U': 'r', 'L': 'g', 'D': 'o'},
            'yg': {'R': 'r', 'U': 'g', 'L': 'o', 'D': 'b'},
            # --- White Faces (Bottom) ---
            'wr': {'R': 'g', 'U': 'r', 'L': 'b', 'D': 'o'}, 
            'wb': {'R': 'r', 'U': 'b', 'L': 'o', 'D': 'g'},
            'wo': {'R': 'b', 'U': 'o', 'L': 'g', 'D': 'r'},
            'wg': {'R': 'o', 'U': 'g', 'L': 'r', 'D': 'b'}
        }       
        self.formula={
                "baseR":[('R',True),('U',True),('R',False),('U',False)],
                "baseL":[('L',False),('U',False),('L',True),('U',True)],
                "midR":[('U',True),('R',True),('U',True),('R',False),('U',False)],
                "midL":[('U',False),('L',False),('U',False),('L',True),('U',True)],
                "cross":[('R',True),('U',True),('R',False),('U',True),('R',True),('U',False),('U',False),('R',False)],
                "corn":[('U',True),('R',True),('U',False),('L',False),('U',True),('R',False),('U',False),('L',True)],
                "top":[('U',True),('R',False),('U',False),('R',True)],
            } 




    def runFacingMove(self,facing,move,clockWise=True):
        moves=self.orientationMap[facing]
        self.moveCube(moves[move],clockWise)
        

    def runFormula(self,facing,formula):
        algorithm=self.formula[formula]
        for step in algorithm:
            self.runFacingMove(facing,step[0],step[1])

    def moveCube(self,face='r',clockWise=True):
        match face:
            case 'y':
                self.myCube.moveYellow(clockWise)
            case 'r':
                self.myCube.moveRed(clockWise)
            case 'w':
                self.myCube.moveWhite(clockWise)
            case 'o':
                self.myCube.moveOrange(clockWise)
            case 'b':
                self.myCube.moveBlue(clockWise)
            case 'g':
                self.myCube.moveGreen(clockWise)

 

    def inputState(self):
        print("please enter the state of your cube.")
        print()
        print("correct oriantation of cube: ")
        print("Top: Yellow, Front: Red.....")
        print()
        print()
       
        while True:
            cube=np.empty((6,3,3), dtype='<U1')
            faceColors = ['Yellow','Red', 'White', 'Orange', 'Blue', 'Green']
            for face, color in zip(cube, faceColors):
                print(f"enter values of {color} faces: ")
                for x in range(3):
                    for y in range(3):
                        face[x][y]=str(input()) 

            testCube=Cube(cube)
            if testCube.isValidState():
                print("state accepted: ")
                return cube
            else:
                print("\n!!! Invalid Cube State Detected. Please try again. !!!\n")
    
        








