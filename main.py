

import numpy as np





class Cube:
    def __init__(self, stateData) -> None:
        self.state=np.array(stateData)





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
            self.state[3][0][0], self.state[3][1][0], self.state[3][2][0] = temp[2], temp[1], temp[0]
        else:
            self.state[5] = np.rot90(self.state[5], k=1)
            self.state[0][0][2], self.state[0][1][2], self.state[0][2][2] = self.state[3][2][0], self.state[3][1][0], self.state[3][0][0]
            self.state[3][0][0], self.state[3][1][0], self.state[3][2][0] = self.state[2][2][2], self.state[2][1][2], self.state[2][0][2]
            self.state[2][0][2], self.state[2][1][2], self.state[2][2][2] = self.state[1][0][2], self.state[1][1][2], self.state[1][2][2]
            self.state[1][0][2], self.state[1][1][2], self.state[1][2][2] = temp[0], temp[1], temp[2]


    def moveBlue(self, clockWise=True):
        temp = np.array([self.state[0][0][0], self.state[0][1][0], self.state[0][2][0]])

        if clockWise:
            self.state[4] = np.rot90(self.state[4], k=-1)
            self.state[0][0][0], self.state[0][1][0], self.state[0][2][0] = self.state[3][2][2], self.state[3][1][2], self.state[3][0][2]
            self.state[3][0][2], self.state[3][1][2], self.state[3][2][2] = self.state[2][2][0], self.state[2][1][0], self.state[2][0][0]
            self.state[2][0][0], self.state[2][1][0], self.state[2][2][0] = self.state[1][0][0], self.state[1][1][0], self.state[1][2][0]
            self.state[1][0][0], self.state[1][1][0], self.state[1][2][0] = temp[0], temp[1], temp[2]
        else:
            self.state[4] = np.rot90(self.state[4], k=1)
            self.state[0][0][0], self.state[0][1][0], self.state[0][2][0] = self.state[1][0][0], self.state[1][1][0], self.state[1][2][0]
            self.state[1][0][0], self.state[1][1][0], self.state[1][2][0] = self.state[2][0][0], self.state[2][1][0], self.state[2][2][0]
            self.state[2][0][0], self.state[2][1][0], self.state[2][2][0] = self.state[3][2][2], self.state[3][1][2], self.state[3][0][2]
            self.state[3][0][2], self.state[3][1][2], self.state[3][2][2] = temp[2], temp[1], temp[0]
