

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













