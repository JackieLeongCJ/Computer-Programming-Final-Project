import pyxel

from draw_title import draw_title

#mainmenu2 GUI
test_tube_rack_x, test_tube_rack_y  = 75, 300
test_tube_rack = (0, 110, 64, 103, 48)

spirit_lamp_x , spririt_lamp_y =  275, 300
spririt_lamp = (0, 216, 64, 40, 48)
text_x, text_y = 100, 208
text_hspace, text_vspace = 8, 40

GAM_txt = (1, 0, 24, 72, 24)
E_txt = (1, 24, 0, 24, 24)
M_txt = (1, 48, 24, 24, 24)
O_txt = (1, 0, 72, 24, 24)
D_txt = (1, 48, 48, 24, 24)
X_txt = (1, 72, 72, 24, 24)
I_txt = (1, 72, 48, 24, 24)
T_txt = (1, 0, 0 ,24, 24)
G_txt = (1, 0, 24, 24, 24)
U_txt = (1, 0, 48, 24, 24)


#ION POP explanation GUI
top_left_corner = (2, 0, 0, 16, 16)
top_left_corner_left_edge = (2, 0, 16, 16, 48)
bottom_left_corner = (2, 0, 112, 16, 16)
tople1, tople2, tople3 = (2, 16, 32, 16, 16), (2, 16, 48, 16, 16), (2, 16, 64, 16, 16)
botle1, botle2, botle3 = (2, 16, 80, 16, 16), (2, 16, 96, 16, 16), (2, 16, 112, 16, 16)
top_right_corner = (2, 48, 0, 16, 16)
top_right_corner_edge = (2, 48, 16, 16, 48)
bottom_right_corner = (2, 48 ,112, 16, 16)
middle_tile = (2, 16, 16, 16, 16)
right_arrow = (2, 232, 0, 24, 24)
left_arrow = (2, 232, 24, 24, 24)
ion_selection_icon = (0, 0, 64, 16, 16)
blue_com_icon = (0 ,24, 0, 24, 24)
universal_icon = (0, 48, 48, 16, 16)
red_com_icon = (0, 0, 0, 24, 24)
black_com_icon = (0, 48, 0, 24, 24)
green_com_icon = (0, 72, 0, 24, 24)
black_bomb_icon = (0, 48, 32, 16, 16)

origin_color = [
"000000", "2b335f", "7e2072", "3e9da2",
"8b4852", "466495", "a9c1ff", "eeeeee",
"d4186c", "dd996e", "eecf5d", "70c6a9",
"678ad4", "969696", "e69aa2", "edc7b0"]





#YOU WIN SCENE
Y_text = (2, 64, 0, 28, 40)
O_text = (2, 96, 0, 28, 40)
U_text = (2, 128, 0, 28, 40)
W_text = (2, 96, 40, 44, 40)
I_text = (2, 144, 40, 28, 40)
N_text = (2, 176 ,40, 28, 40)

#YOU LOSE SCENE
L_text = (2, 160, 0, 28, 40)
S_text = (2, 192, 0, 28, 40)
E_text = (2, 64, 40, 28, 40)

#GAME OVER SCENE
G_text = (2, 64, 80, 28, 40)
A_text = (2, 96, 80, 28, 40)
M_text = (2, 192, 80, 44, 40)
V_text = (2, 128, 80, 28, 40)
R_text = (2, 160, 80, 28, 40)

def change_color(pal_no, col):
    pyxel.colors[pal_no] = int("0x" + col, 16)

def reset_color():
    for i in range(16):
        change_color(i, origin_color[i])

def txt_x(n): #n = number of words
    return 200 - (12 * n)

    
def draw_main_menu():
    pyxel.cls(0)
    reset_color()
    change_color(9, "ff9000")

    draw_title(4, 100)
    pyxel.blt(test_tube_rack_x, test_tube_rack_y, *test_tube_rack)#test tube rack
    pyxel.blt(spirit_lamp_x, spririt_lamp_y, *spririt_lamp)
    pyxel.blt(88, 208, 1, 24, 48, 24, 24) #S
    for i in range(2):
        pyxel.blt(112 + 72 * i, 208 + 1, 1, 0, 0, 24, 24) #T
    
    pyxel.blt(140, 208 + 2, 1, 28, 26, 18, 22)# A
    pyxel.blt(162, 208 + 2, 1, 27, 74, 19, 22) # R
    
    #GAME
    pyxel.blt(216, 208 + 2, 1,0 ,26, 72, 24 ) #GAM
    pyxel.blt(288  + 1 , 208, 1, 24, 0, 24, 24) #E

    pyxel.text(216 , 236, " -PRESS ENTER TO START-", pyxel.frame_count % 16) 

def draw_main_menu2(mainmenu2_selection_index):
    reset_color()
    pyxel.cls(0)        #GAME
    draw_title(4, 100)
    change_color(9, "ff9000")
    
    #GUIDE
    pyxel.blt(txt_x(5), text_y - 8 -20, *G_txt)
    pyxel.blt(txt_x(5) + 24, text_y - 8 -20, *U_txt)
    pyxel.blt(txt_x(5) + 24 * 2, text_y - 8 -20, *I_txt)
    pyxel.blt(txt_x(5) + 24 * 3, text_y - 8 -20, *D_txt)
    pyxel.blt(txt_x(5) + 24 * 4, text_y - 8 -20, *E_txt)

    pyxel.blt(test_tube_rack_x, test_tube_rack_y, *test_tube_rack)
    pyxel.blt(spirit_lamp_x, spririt_lamp_y, *spririt_lamp)
    pyxel.blt(text_x, text_y + 2 + 8, *GAM_txt) #GAM
    
    pyxel.blt(text_x + 24 * 3 + 1, text_y + 8 + 2, *E_txt)# E
    

    #MODE
    pyxel.blt(text_x + 24 * 4 + 8, text_y + 8 + 2, *M_txt) #M
    pyxel.blt(text_x + 24 * 5 + 8 + 1, text_y + 8 + 1, *O_txt) #o
    pyxel.blt(text_x + 24 * 6 + 8 + 1, text_y + 8 + 1, *D_txt) #D
    pyxel.blt(text_x + 24 * 7 + 8, text_y + 8 + 1, *E_txt)

    #EXIT
    pyxel.blt(152, 248 + 8, *E_txt) #E
    pyxel.blt(176, 248 + 8, *X_txt) #X
    pyxel.blt(200, 248 + 8, *I_txt) #I
    pyxel.blt(224, 248 + 8, *T_txt) #T

    if mainmenu2_selection_index == 0:
        for i in range(2):
            pyxel.blt(txt_x(5) - 8 - 16 + (24*5 + 8 + 8 + 16)*i, 172 + 4 + 8, 0, 0, 64, 16, 16)
    if mainmenu2_selection_index == 1:
        for i in range(2):
            pyxel.blt(76 + 232 * i, 208 + 4 + 8, 0, 0, 64, 16, 16)
    if mainmenu2_selection_index == 2:
        for i in range(2):    
            pyxel.blt(128 + 128 * i, 248 + 4 + 8, 0, 0, 64, 16, 16)


def draw_gamemode(gamemode_selection_index):
    change_color(13, "ffdd50")
    pyxel.cls(0)
    pyxel.blt(72, 216, 1, 0 , 112, 256 ,144) #PERIODIC TABLE
    pyxel.blt(72, 40, 0, 0, 112, 256, 144) #ION POP
    #left arrow
    pyxel.blt(20, 10, *left_arrow)
    if gamemode_selection_index == 0:
        pyxel.blt(20 + 24 + 8, 14, *ion_selection_icon)
    if gamemode_selection_index == 1:
        for i in range(2):
            pyxel.blt(48 + 288 * i, 104, *ion_selection_icon)
    if gamemode_selection_index == 2:
        for i in range(2):    
            pyxel.blt(48 + 288 * i, 280, *ion_selection_icon)
    
def draw_ion_exp(ionexp_selelection_index): #edit the frame size at the above
    w, h = 5, 6
    frame_x , frame_y = (400 - (16 * 2 + 48 * w))/2 , (400 - (16 * 2 + 48 * h))/2
    reset_color()
    change_color(1,"393939")
    change_color(2,"666666")
    change_color(13,"969696")
    change_color(4,"FFFFFF")
    change_color(5,"DFDFDF")
    pyxel.cls(0)

    #left arrow
    pyxel.blt(20, 10, *left_arrow)
    #right arrow
    pyxel.blt(356, 10, *right_arrow)

    if ionexp_selelection_index == 0:
        pyxel.blt(356 - 8 -16, 14 ,*ion_selection_icon)
    if ionexp_selelection_index == 1:
        pyxel.blt(20 + 24 + 8, 14, *ion_selection_icon)

    pyxel.blt(frame_x, frame_y, *top_left_corner)
    for i in range(h):
        pyxel.blt(frame_x, frame_y + 16 + 48 * i, *top_left_corner_left_edge)
    pyxel.blt(frame_x, frame_y + 16 + 48 * h, *bottom_left_corner)

    for i in range(w):
        pyxel.blt(frame_x + 16 + 48 * i, frame_y, *tople1)
        pyxel.blt(frame_x + 32 + 48 * i, frame_y, *tople2)
        pyxel.blt(frame_x + 48 + 48 * i, frame_y, *tople3)

    pyxel.blt(frame_x + 16 + 48 * w, frame_y, *top_right_corner)

    for i in range(w):
        pyxel.blt(frame_x + 16 + 48 * i, frame_y + 16 + 48 * h ,*botle1)
        pyxel.blt(frame_x + 32 + 48 * i, frame_y + 16 + 48 * h, *botle2)
        pyxel.blt(frame_x + 48 + 48 * i, frame_y + 16 + 48 * h, *botle3)

    pyxel.blt(frame_x + 16 + 48 * w, frame_y + 16 + 48 * h, *bottom_right_corner)

    for i in range(h):
        pyxel.blt(frame_x + 16 + 48 * w, frame_y + 16 + 48 * i, *top_right_corner_edge)
    
    for i in range(3 * w):
        for j in range(3 * h):
            pyxel.blt(frame_x + 16 + 16 * i, frame_y + 16 + 16 * j, *middle_tile)

    pyxel.text(frame_x + 10, frame_y + 16, "Game Control\n \n* Press space bar to shoot ions.\n\n* Press backspace to pause the game.\
\n\n* Hold left and right key to control the shooter", 0)

    pyxel.text(frame_x + 10, frame_y + 52 + 18, "Game Rules:\n \n\
* Ten ions are spawned randomly on the screen when the game\n \n  started. \n\
\n* According to the precipitation table, ions that form\n \n \
  insoluble compounds would precipitate when they collide.\n \n\
* To win the game, you need to clear all the ions on the \n \n \
  screen within 60 seconds. Hence, spamming space bar may \n \n\
  not help.", 0)

    pyxel.text(frame_x + 10, frame_y + 150 + 18, "Special Gadget:\n \n\
* By obtaining the following precipitate, you will grant some\n \n\
special abilities.", 0)
    #universal ion
    pyxel.blt(frame_x + 24, frame_y + 190 + 18, *blue_com_icon)
    pyxel.text(frame_x + 16, frame_y + 220 + 18, "Next ion is\nchanged to a \nuniversal ion", 0)
    pyxel.blt(frame_x + 28, frame_y + 240 + 18, *universal_icon)
    pyxel.text(frame_x + 28 + 2, frame_y + 240 + 6 + 18, " ? ", 0)
    pyxel.text(frame_x + 16, frame_y + 240 + 18 + 18, "that can form\nprecipitate\nwith any ions", 0)

    #bomb
    pyxel.blt(frame_x + 90, frame_y + 190 + 18, *red_com_icon)
    pyxel.text(frame_x + 76, frame_y + 220 + 18, "Next ion is\nchanged to a\nbomb, which has\n\
clear AoE on \nnearby ions", 0)
    pyxel.blt(frame_x + 94, frame_y + 260 + 18, *black_bomb_icon )

    #control
    pyxel.blt(frame_x + 96 + 60, frame_y + 190 + 18, *green_com_icon)
    pyxel.text(frame_x + 78 + 65, frame_y + 220 + 18,"Player can \ncontrol the\nmovement of\nthe shooter\nfor 10 seconds",0)

    pyxel.blt(frame_x + 96 + 60*2, frame_y + 190 + 18, *black_com_icon)
    pyxel.text(frame_x + 88 + 60*2, frame_y + 220 + 18,"Timer is \nfreezed for \n5 seconds." ,0)
    

def draw_period_exp():
    w, h = 5, 3
    frame_x , frame_y = (400 - (16 * 2 + 48 * w))/2 , (400 - (16 * 2 + 48 * h))/2
    reset_color()
    pyxel.cls(0)

    #left arrow
    pyxel.blt(20, 10, *left_arrow)
    #ion selection icon
    pyxel.blt(20 + 24 + 8, 14, *ion_selection_icon)

    pyxel.blt(frame_x, frame_y, *top_left_corner)
    for i in range(h):
        pyxel.blt(frame_x, frame_y + 16 + 48 * i, *top_left_corner_left_edge)
    pyxel.blt(frame_x, frame_y + 16 + 48 * h, *bottom_left_corner)

    for i in range(w):
        pyxel.blt(frame_x + 16 + 48 * i, frame_y, *tople1)
        pyxel.blt(frame_x + 32 + 48 * i, frame_y, *tople2)
        pyxel.blt(frame_x + 48 + 48 * i, frame_y, *tople3)

    pyxel.blt(frame_x + 16 + 48 * w, frame_y, *top_right_corner)

    for i in range(w):
        pyxel.blt(frame_x + 16 + 48 * i, frame_y + 16 + 48 * h ,*botle1)
        pyxel.blt(frame_x + 32 + 48 * i, frame_y + 16 + 48 * h, *botle2)
        pyxel.blt(frame_x + 48 + 48 * i, frame_y + 16 + 48 * h, *botle3)

    pyxel.blt(frame_x + 16 + 48 * w, frame_y + 16 + 48 * h, *bottom_right_corner)

    for i in range(h):
        pyxel.blt(frame_x + 16 + 48 * w, frame_y + 16 + 48 * i, *top_right_corner_edge)
    
    for i in range(3 * w):
        for j in range(3 * h):
            pyxel.blt(frame_x + 16 + 16 * i, frame_y + 16 + 16 * j, *middle_tile)

    # pyxel.text(frame_x + 10, frame_y + 16, "Game Control\n \n* Press space bar to shoot ions. ", 0)

    pyxel.text(frame_x + 10, frame_y + 16, "Game Rules:\n \n\
* The game generates an element of proton number from 1 - 20.\n \n\
* Player needs to fill the element to the correspoding cell by\n \n \
clicking one of the boxes with coordinates.\n \n\
* The question does not repeat, and the game ends after 20 \n\nquestions.\n \n \
  \n \n", 0)




def draw_you_lose():
    hspacing = 16
    word_spacing = 4
    font_xpos = (400 - (28 * 7 + hspacing + word_spacing*5))/2
    font_ypos = (400 - 40)/2
    pyxel.cls(0)
    pyxel.blt(font_xpos, font_ypos, *Y_text)
    pyxel.blt(font_xpos + 28 + word_spacing, font_ypos, *O_text)
    pyxel.blt(font_xpos + 28*2 + word_spacing*2, font_ypos, *U_text)

    pyxel.blt(font_xpos + 28*3 + hspacing + word_spacing *2, font_ypos, *L_text )
    pyxel.blt(font_xpos + 28*4 + hspacing + word_spacing*3, font_ypos, *O_text)
    pyxel.blt(font_xpos + 28*5 + hspacing + word_spacing*4, font_ypos, *S_text)
    pyxel.blt(font_xpos + 28*6 + hspacing + word_spacing*5, font_ypos, *E_text )

    pyxel.text(font_xpos + 28*5 + hspacing + word_spacing*4, font_ypos + 40 + 8, "RETAKE CHEMISTRY", 7)
    pyxel.text(font_xpos + 28*2 + word_spacing*2 + 8, font_ypos + 40 + 8 + 16, "- Press Enter To Restart -", pyxel.frame_count % 16)


def draw_you_win():
    hspacing = 16
    word_spacing = 4
    font_xpos = (400 - (28 * 6 + hspacing + word_spacing*4))/2 - 8
    font_ypos = (400 - 40)/2
    pyxel.cls(0)
    pyxel.blt(font_xpos, font_ypos, *Y_text)
    pyxel.blt(font_xpos + 28 + word_spacing, font_ypos, *O_text)
    pyxel.blt(font_xpos + 28*2 + word_spacing*2, font_ypos, *U_text)

    pyxel.blt(font_xpos + 28*3 + hspacing + word_spacing *2, font_ypos, *W_text )
    pyxel.blt(font_xpos + 28*4 + hspacing + word_spacing*3 + 16, font_ypos, *I_text)
    pyxel.blt(font_xpos + 28*5 + hspacing + word_spacing*4 + 16, font_ypos, *N_text)

    pyxel.text(font_xpos + 28*3 + hspacing + word_spacing *2 + 24, font_ypos + 40 + 8,"I BET YOU TO TRY AGAIN", 7)
    pyxel.text(font_xpos + 28*2 + word_spacing*2 - 16, font_ypos + 40 + 8 + 16, "- Press Enter To Restart -", pyxel.frame_count % 16)

def draw_game_over(score, wrong):
    hspacing = 16
    word_spacing = 4
    font_xpos = (400 - (28 * 8 + hspacing + word_spacing*6))/2 - 16
    font_ypos = (400 - 40)/2
    pyxel.cls(0)
    pyxel.blt(font_xpos, font_ypos, *G_text)
    pyxel.blt(font_xpos + 28 + word_spacing, font_ypos, *A_text)
    pyxel.blt(font_xpos + 28*2 + word_spacing*2, font_ypos, *M_text)
    pyxel.blt(font_xpos + 28*3 + word_spacing*3 + 16, font_ypos, *E_text)

    pyxel.blt(font_xpos + 28*4 + hspacing + word_spacing * 3 + 16, font_ypos, *O_text)
    pyxel.blt(font_xpos + 28*5 + hspacing + word_spacing * 4 + 16, font_ypos, *V_text)
    pyxel.blt(font_xpos + 28*6 + hspacing + word_spacing * 5 + 16, font_ypos, *E_text)
    pyxel.blt(font_xpos + 28*7 + hspacing + word_spacing * 6 + 16, font_ypos, *R_text)

    pyxel.text(font_xpos + 28*3 + word_spacing*3 + 2, font_ypos + 40 + 8 ,f"Score: {score}        Wrong: {wrong}", 7)
    pyxel.text(font_xpos + 28*3 + word_spacing*3 + 2, font_ypos + 40 + 8 + 16, "- Press Enter To Restart -", pyxel.frame_count % 16)
    