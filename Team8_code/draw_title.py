import pyxel


def draw_title(title_x, title_y):
    K_pos = (2, 64, 160, 56, 56)
    H_pos = (2, 120, 160, 56, 56)
    E_pos = (2, 184, 184, 40, 40) #x + 8, y + 8
    bar_pos = (2, 188, 172, 32, 12)
    M_pos = (2, 72, 216, 40, 40) # x + 8, y + 8
    I_pos = (2, 232, 168, 20, 40)# x + 18, y + 8
    A_pos = (2, 128, 216 ,32, 40)# x + 12, y + 8
    top_left_corner_tile = (2, 120, 160, 8, 8)
    top_right_corner_tile = (2, 168, 160, 8, 8)
    bottom_left_corner_tile = (2, 120, 208, 8, 8)
   
    pyxel.cls(0)
    pyxel.blt(title_x, title_y, *K_pos) #K
    pyxel.text(title_x + 2, title_y + 3, "19", 0)
    pyxel.text(title_x + 10, title_y + 49, "Potassium", 0)

    pyxel.blt(title_x + 56, title_y, *H_pos) #H
    pyxel.text(title_x + 56 + 2, title_y + 3, "1", 0)
    pyxel.text(title_x + 56 + 12, title_y + 49, "Hydrogen", 0)
    
    pyxel.blt(title_x + 56*2 + 8, title_y + 8, *E_pos) #E
    pyxel.blt(title_x + 56*2 + 8 + 4, title_y + 8 - 16, *bar_pos)

    pyxel.blt(title_x + 56*3 + 8, title_y + 8, *M_pos) #M

    pyxel.blt(title_x + 56 *4 + 8, title_y +8, *E_pos) #E

    pyxel.blt(title_x + 56*5 + 18, title_y + 8, *I_pos) #I
    
    for i in range(6):
        pyxel.blt(title_x + 56*5 + 8*i, title_y, *top_left_corner_tile)
        pyxel.blt(title_x + 56*5 + 48, title_y + 8*i, *top_right_corner_tile)
        pyxel.blt(title_x + 56*5 + 8*i, title_y + 48, *bottom_left_corner_tile)
        pyxel.blt(title_x + 56*5 + 48, title_y + 48, 2, 168, 208, 8, 8) #bottom_right_corner_tile

    for i in range(5):
        for j in range(3):
            pyxel.blt(title_x + 56*5 + 6 * j, title_y + 8 + 8 * i, *top_left_corner_tile)
    
    for i in range(5):
        for j in range(2):
            pyxel.blt(title_x + 56*5 + 18 + 20 + 6 * j , title_y + 8 + 8 * i, *top_left_corner_tile)
    pyxel.text(title_x + 56*5 + 2, title_y + 3, "53", 0)
    pyxel.text(title_x + 56*5 + 17, title_y + 49, "Iodine", 0)
    pyxel.blt(title_x + 56*6 + 12, title_y + 8, *A_pos)#A

