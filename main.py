

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



<<<<<<< HEAD
    def moveRed(self, clockWise=True):
        # Temp stores Yellow Bottom Row (Row 2)
        temp = np.array([self.state[0][2][0], self.state[0][2][1], self.state[0][2][2]])
        
        if clockWise:
            self.state[1] = np.rot90(self.state[1], k=-1)
            
            # 1. Yellow Bottom Row (Row 2) gets Blue Right Col (Col 2) [Reversed]
            self.state[0][2][0], self.state[0][2][1], self.state[0][2][2] = self.state[4][2][2], self.state[4][1][2], self.state[4][0][2]
            
            # 2. Blue Right Col (Col 2) gets White Top Row (Row 0) [Reversed]
            self.state[4][2][2], self.state[4][1][2], self.state[4][0][2] = self.state[2][0][2], self.state[2][0][1], self.state[2][0][0]
            
            # 3. White Top Row (Row 0) gets Green Left Col (Col 0) [Reversed]
            self.state[2][0][2], self.state[2][0][1], self.state[2][0][0] = self.state[5][0][0], self.state[5][1][0], self.state[5][2][0]
            
            # 4. Green Left Col (Col 0) gets Temp (Yellow) [Reversed]
            # Note: Your original code reversed the temp assignment (temp[2], temp[1]...)
            self.state[5][0][0], self.state[5][1][0], self.state[5][2][0] = temp[2], temp[1], temp[0]
            
        else:
            self.state[1] = np.rot90(self.state[1], k=1)
            
            # 1. Yellow Bottom Row gets Green Left Col
            self.state[0][2][0], self.state[0][2][1], self.state[0][2][2] = self.state[5][0][0], self.state[5][1][0], self.state[5][2][0]
            
            # 2. Green Left Col gets White Top Row
            self.state[5][0][0], self.state[5][1][0], self.state[5][2][0] = self.state[2][0][2], self.state[2][0][1], self.state[2][0][0]
            
            # 3. White Top Row gets Blue Right Col
            self.state[2][0][2], self.state[2][0][1], self.state[2][0][0] = self.state[4][2][2], self.state[4][1][2], self.state[4][0][2]
            
            # 4. Blue Right Col gets Temp (Yellow)
            self.state[4][2][2], self.state[4][1][2], self.state[4][0][2] = temp[0], temp[1], temp[2]
=======
    
>>>>>>> f844a81 (feat: add isValidState helper function)













