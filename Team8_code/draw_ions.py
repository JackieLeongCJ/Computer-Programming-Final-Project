import pyxel

COM_WHITE = (0, 72, 88, 24, 24)
COM_BLACK = (0, 48, 64, 24, 24)
COM_YELLOW = (0, 0, 88, 24, 24) 
COM_BLUE = (0, 24, 88, 24, 24) 
COM_RED = (0, 24, 64, 24, 24) 
COM_GREEN = (0, 48, 88, 24, 24) 

ION_WHITE = (0, 0, 48, 16, 16)
ION_WHITE2 = (0, 32, 48, 16, 16)
ION_YELLOW = (0, 16, 32, 16, 16)
ION_BLUE = (0, 0, 64, 16, 16)
ION_RED = (0, 16, 48, 16, 16)
ION_GREEN = (0, 32, 32, 16, 16)
ION_BLACK = (0, 0, 32, 16, 16)

class Ions():
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16
        self.type = type
       
    def draw(self):
        if self.type == 1:
            pyxel.blt(self.x, self.y, *ION_BLUE)
            pyxel.text(self.x + 3, self.y + 2, "  -\nCl", 0)
        elif self.type == 2:
            pyxel.blt(self.x, self.y, *ION_BLUE)
            pyxel.text(self.x + 3, self.y + 2, "  -\nBr", 0)
        elif self.type == 3:
            pyxel.blt(self.x, self.y, *ION_BLUE)
            pyxel.text(self.x + 5, self.y + 2, " -\nI", 0)
        elif self.type == 4:
            pyxel.blt(self.x, self.y, *ION_BLUE)
            pyxel.text(self.x + 1, self.y + 2, "  2-\nSO4", 0)
        elif self.type == 5:
            pyxel.blt(self.x, self.y, *ION_BLUE)
            pyxel.text(self.x + 0, self.y + 2, "  2-\nCrO4", 0)
        elif self.type == 6:
            pyxel.blt(self.x, self.y, *ION_BLUE)
            pyxel.text(self.x + 4, self.y + 2, " 2-\nS", 0)
        elif self.type == 7:
            pyxel.blt(self.x, self.y, *ION_BLUE)
            pyxel.text(self.x + 3, self.y + 2, "  -\nOH", 0)
        elif self.type == 8:
            pyxel.blt(self.x, self.y, *ION_BLUE)
            pyxel.text(self.x + 1, self.y + 2, "  3-\nPO4", 0)
        elif self.type == 9:
            pyxel.blt(self.x, self.y, *ION_BLUE)
            pyxel.text(self.x + 1, self.y + 2, "  2-\nCO3", 0)
        elif self.type == 10:
            pyxel.blt(self.x, self.y, *ION_BLUE)
            pyxel.text(self.x + 1, self.y + 2, "  2-\nSO3", 0)

        elif self.type == 11:
            pyxel.blt(self.x, self.y, *ION_RED)
            pyxel.text(self.x + 1, self.y + 2, "  2+\nHg2", 0)
        elif self.type == 12:
            pyxel.blt(self.x, self.y, *ION_RED)
            pyxel.text(self.x + 3, self.y + 2, "  +\nCu", 0)
        elif self.type == 13:
            pyxel.blt(self.x, self.y, *ION_RED)
            pyxel.text(self.x + 3, self.y + 2, "  +\nTl", 0)
        elif self.type == 14:
            pyxel.blt(self.x, self.y, *ION_RED)
            pyxel.text(self.x + 3, self.y + 2, " 2+\nPb", 0)
        elif self.type == 15:
            pyxel.blt(self.x, self.y, *ION_RED)
            pyxel.text(self.x + 3, self.y + 2, "  +\nAg", 0)
        elif self.type == 16:
            pyxel.blt(self.x, self.y, *ION_RED)
            pyxel.text(self.x + 3, self.y + 2, " 2+\nSr", 0)
        elif self.type == 17:
            pyxel.blt(self.x, self.y, *ION_RED)
            pyxel.text(self.x + 3, self.y + 2, " 2+\nBa", 0)
        elif self.type == 18:
            pyxel.blt(self.x, self.y, *ION_RED)        
            pyxel.text(self.x + 3, self.y + 2, " 2+\nCa", 0)
        elif self.type == 19:
            pyxel.blt(self.x, self.y, *ION_RED)
            pyxel.text(self.x + 3, self.y + 2, " 2+\nMg", 0)
        elif self.type == 20:
            pyxel.blt(self.x, self.y, *ION_RED)
            pyxel.text(self.x + 3, self.y + 2, " 2+\nCu", 0)
        elif self.type == 21:
            pyxel.blt(self.x, self.y, *ION_WHITE)
            pyxel.text(self.x + 2, self.y + 6, " ? ", 0)
        elif self.type == 22:
            pyxel.blt(self.x, self.y, *ION_BLACK)
            pyxel.text(self.x + 1, self.y + 6, "bomb", 7)

        elif self.type == 111:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 1, self.y + 10, "Hg2Cl2", 0)
        elif self.type == 112:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 4, self.y + 10, "CuCl", 0)
        elif self.type == 113:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 4, self.y + 10, "TlCl", 0)
        elif self.type == 114:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "PbCl2", 0)
        elif self.type == 115:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 4, self.y + 10, "AgCl", 0)

        elif self.type == 211:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 1, self.y + 10, "Hg2Br2", 0)
        elif self.type == 212:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 4, self.y + 10, "CuBr", 0)
        elif self.type == 213:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 4, self.y + 10, "TlBr", 0)
        elif self.type == 214:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "PbBr2", 0)
        elif self.type == 215:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 4, self.y + 10, "AgBr", 0)

        elif self.type == 311:
            pyxel.blt(self.x, self.y, *COM_YELLOW)
            pyxel.text(self.x + 3, self.y + 10, "Hg2I2", 0)
        elif self.type == 312:
            pyxel.blt(self.x, self.y, *COM_YELLOW)
            pyxel.text(self.x + 6, self.y + 10, "CuI", 0)
        elif self.type == 313:
            pyxel.blt(self.x, self.y, *COM_YELLOW)
            pyxel.text(self.x + 6, self.y + 10, "TlI", 0)
        elif self.type == 314:
            pyxel.blt(self.x, self.y, *COM_YELLOW)
            pyxel.text(self.x + 4, self.y + 10, "PbI2", 0)
        elif self.type == 315:
            pyxel.blt(self.x, self.y, *COM_YELLOW)
            pyxel.text(self.x + 6, self.y + 10, "AgI", 0)

        elif self.type == 414:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "PbSO4", 0)
        elif self.type == 416:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "SrSO4", 0)
        elif self.type == 417:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "BaSO4", 0)
        elif self.type == 418:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "CaSO4", 0)

        elif self.type == 514:
            pyxel.blt(self.x, self.y, *COM_YELLOW)
            pyxel.text(self.x + 4, self.y + 6, " Pb\nCrO4", 0)
        elif self.type == 515:
            pyxel.blt(self.x, self.y, *COM_RED)
            pyxel.text(self.x + 5, self.y + 6, "Ag2\nCrO4", 0)
        elif self.type == 516:
            pyxel.blt(self.x, self.y, *COM_YELLOW)
            pyxel.text(self.x + 4, self.y + 6, " Sr\nCrO4", 0)
        elif self.type == 517:
            pyxel.blt(self.x, self.y, *COM_YELLOW)
            pyxel.text(self.x + 4, self.y + 6, " Ba\nCrO4", 0)
        
        elif self.type == 614:
            pyxel.blt(self.x, self.y, *COM_BLACK)
            pyxel.text(self.x + 6, self.y + 10, "PbS", 7)
        elif self.type == 615:
            pyxel.blt(self.x, self.y, *COM_BLACK)
            pyxel.text(self.x + 4, self.y + 10, "Ag2S", 7)
        elif self.type == 620:
            pyxel.blt(self.x, self.y, *COM_BLUE)
            pyxel.text(self.x + 6, self.y + 10, "CuS", 0)

        elif self.type == 714:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 6, " Pb\n(OH)2", 0)
        elif self.type == 715:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 4, self.y + 10, "AgOH", 0)
        elif self.type == 719:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 6, " Mg\n(OH)2", 0)
        elif self.type == 720:
            pyxel.blt(self.x, self.y, *COM_BLUE)
            pyxel.text(self.x + 3, self.y + 6, " Cu\n(OH)2", 0)

        elif self.type == 814:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 0, self.y + 6, " Pb3\n(PO4)2", 0)
        elif self.type == 815:
            pyxel.blt(self.x, self.y, *COM_YELLOW)
            pyxel.text(self.x + 3, self.y + 10, "Ag3PO4", 0)
        elif self.type == 816:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 0, self.y + 6, " Sr3\n(PO4)2", 0)
        elif self.type == 817:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 0, self.y + 6, " Ba3\n(PO4)2", 0)
        elif self.type == 818:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 0, self.y + 6, " Ca3\n(PO4)2", 0)
        elif self.type == 819:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 0, self.y + 6, " Mg3\n(PO4)2", 0)
        elif self.type == 820:
            pyxel.blt(self.x, self.y, *COM_BLUE)
            pyxel.text(self.x + 0, self.y + 6, " Cu3\n(PO4)2", 0)

        elif self.type == 914:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "PbCO3", 0)
        elif self.type == 915:
            pyxel.blt(self.x, self.y, *COM_YELLOW)
            pyxel.text(self.x + 1, self.y + 10, "Ag2CO3", 0)
        elif self.type == 916:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "SrCO3", 0)
        elif self.type == 917:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "BaCO3", 0)
        elif self.type == 918:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "CaCO3", 0)
        elif self.type == 919:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "MgCO3", 0)
        elif self.type == 920:
            pyxel.blt(self.x, self.y, *COM_GREEN)
            pyxel.text(self.x + 3, self.y + 10, "CuCO3", 0)

        elif self.type == 1014:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "PbSO3", 0)
        elif self.type == 1015:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 1, self.y + 10, "Ag2SO3", 0)
        elif self.type == 1016:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "SrSO3", 0)
        elif self.type == 1017:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "BaSO3", 0)
        elif self.type == 1018:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "CaSO3", 0)
        elif self.type == 1019:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 3, self.y + 10, "MgSO3", 0)
        elif self.type == 1020:
            pyxel.blt(self.x, self.y, *COM_BLUE)
            pyxel.text(self.x + 3, self.y + 10, "CuSO3", 0)
        elif self.type > 2100:
            pyxel.blt(self.x, self.y, *COM_WHITE)
            pyxel.text(self.x + 6, self.y + 10, "???", 0)
        