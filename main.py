

import numpy as np





class Cube:
    def __init__(self, stateData) -> None:
        self.state=np.array(stateData)

    def isValidState(self):
        redStickerCount=0
        yellowStickerCount=0
        whiteStickerCount=0
        blueStickerCount=0
        greenStickerCount=0
        orangeStickerCount=0

        for i in range(6):
            for values in self.state[i]:
                match values:
                    case 'r':
                        redStickerCount+=1
                    case 'y':
                        yellowStickerCount+=1
                    case 'w':
                        whiteStickerCount+=1
                    case 'b':
                        blueStickerCount+=1
                    case 'g':
                        greenStickerCount+=1
                    case 'o':
                        orangeStickerCount+=1
                    case _:
                        print(f"unknown move: {values}")

        if redStickerCount == yellowStickerCount == whiteStickerCount == blueStickerCount == greenStickerCount == orangeStickerCount==9):
            return True
        else:
            return False

















