import time
import random
import pyxel

import music
import physics as Phy
from periodictable import PeriodicTable, game, reset
from draw_ions import Ions
from mainmenu import MainMenu
from draw_scene import draw_game_over


SCENE_MAINMENU = 0
SCENE_MAINMENU2 = 1
SCENE_GAMEMODE = 2
SCENE_PERIOD_EXP = 3
SCENE_ION_EXP = 4
SCENE_GAME_PERIOD = 5
SCENE_GAME_ION = 6
SCENE_GAME_OVER = 7
SCENE_YOU_LOSE = 8
SCENE_YOU_WIN = 9

IONPOP_GAMETIME = 60
FREELY_MOVE_TIME = 10
IONPOP_SHOOT_BOTTOM = pyxel.KEY_SPACE

origin_color = [
"000000", "2b335f", "7e2072", "3e9da2",
"8b4852", "466495", "a9c1ff", "eeeeee",
"d4186c", "dd996e", "eecf5d", "70c6a9",
"678ad4", "969696", "e69aa2", "edc7b0"]

window_width, window_height = 400, 400
def convert_coordinates(x, y, radius):
    return x-radius, y-radius

def change_color(pal_no, col):
    pyxel.colors[pal_no] = int("0x" + col, 16)

def reset_color():
    for i in range(16):
        change_color(i, origin_color[i])

class App:
    def __init__(self):
        #pyxel init
        pyxel.init(window_width,window_height, display_scale= 2, title ="Khemeia", fps = 60)

        pyxel.load("resources.pyxres")
        
        pyxel.mouse(visible=True)
        pyxel.fullscreen(True)

        self.game_ion_running = False
        self.game_period_running = False

        self.mainmenu = MainMenu()

        # set music
        music.set_sound()

        pyxel.run(self.update, self.draw)
            
    def update(self):
        self.mainmenu.update()
        if self.mainmenu.scene == SCENE_GAME_ION:######
            if not self.game_ion_running:
                self.game_ion_setup_pymunk()
            self.game_ion_update()
        if self.mainmenu.scene == SCENE_GAME_PERIOD:######
            if not self.game_period_running:
                self.game_period_setup()
            self.game_period_update()        
        # update music
        music.update_sound()
        
    def draw(self):
        self.mainmenu.draw()
        if self.mainmenu.scene == SCENE_GAME_ION:
            self.game_ion_draw()
        if self.mainmenu.scene == SCENE_GAME_PERIOD:
            self.game_period_draw()
        if self.mainmenu.scene == SCENE_GAME_OVER:
            # print("$", self.score, self.wrong)
            draw_game_over(self.score, self.wrong)

    def game_period_setup(self):
        #score
        self.score=0
        self.wrong=0
        #question and choice
        self.correct=0
        self.appear=[]
        self.r_appear=[]
        self.ques=[]
        self.ABCD=[]
        self.list_element=[]
        #answer text
        self.At=0
        self.Bt=0
        self.Ct=0
        self.Dt=0
        self.x=random.randrange(5)
        self.y=random.randrange(4)

        self.ques_pool = [i for i in range(20)]
        self.game_period_running = True

    def game_period_update(self):
        PeriodicTable.update(self)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if game.check_ans(self):
                if len(self.ques_pool) > 0:
                    reset.reset_ques(self)
                else:
                    game.end_game(self)

    def game_period_draw(self):
        pyxel.cls(0)
        reset_color()
        pyxel.rectb(15,15,375,160,6)
        pyxel.text(20, 70, '1', 7)
        pyxel.text(20, 90, '2', 7)
        pyxel.text(20, 110, '3', 7)
        pyxel.text(20, 130, '4', 7)
        list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        for j in range (18):
            pyxel.text(33+20*j,140,str(list[j]),7)

        PeriodicTable.draw(self)
        pyxel.text(20, 20, f"SCORE {self.score}", 7)
        pyxel.text(100, 20, f"WRONG {self.wrong}", 7)
        
    def game_ion_setup_pymunk(self):
        self.physics = Phy.Physics()

        x = self.physics.get_position_to_shoot() - 8
        y = window_height - 24
        type = self.physics.get_ion_type_to_shoot()
        self.ion_to_shoot = Ions(x, y, type)

        self.ions = dict()
        ions_set = self.physics.get_particle_info()
        for i in ions_set:
            x, y, type = i.body.position.x, i.body.position.y, i.type
            x, y = convert_coordinates(x, y, i.body.radius)
            # print(x, y)
            ion = Ions(x, y, type)
            self.ions[i.ID]= ion

        self.game_ion_start_time = time.time()
        self.game_ion_now_second = 0
        self.game_ion_running = True
        self.game_ion_pause = False
        self.game_ion_hold_pause = False
        self.game_ion_pause_begintime = self.game_ion_start_time

        self.game_ion_exploded = [False, 0, 0]
        self.game_ion_last_explosion_time = self.game_ion_start_time
        self.game_ion_freely_move_endtime = self.game_ion_start_time
        self.game_ion_freely_move = False
        self.pre_dx = 2

    def game_ion_update(self):
        if not self.game_ion_pause:
            self.physics.update()
        self.game_ion_event()   
        if not self.game_ion_pause:         
            ion_info = self.physics.get_particle_info()
            ion_to_remove = self.physics.get_particle_to_remove()
            self.game_ion_exploded = self.physics.is_bomb_exploded()
            if self.physics.is_time_freezed():
                self.game_ion_start_time += min(time.time()-self.game_ion_last_explosion_time, 5)
                self.game_ion_last_explosion_time = time.time()
            if self.physics.is_ready_to_freely_move():
                # print("Freely move begin.")
                self.game_ion_freely_move = True
                self.game_ion_freely_move_endtime = time.time() + FREELY_MOVE_TIME
                self.pre_dx = self.physics.get_direction_for_shooter_to_move()

            for id in ion_to_remove:
                if id in self.ions:
                    del self.ions[id]
            for i in ion_info:
                x, y, type = i.body.position.x, i.body.position.y, i.type
                x, y = convert_coordinates(x, y, i.radius)
                if i.ID not in self.ions:
                    self.ions[i.ID] = Ions(x, y, type)
                else:
                    self.ions[i.ID].x = x  
                    self.ions[i.ID].y = y
            if time.time()-self.game_ion_start_time >= self.game_ion_now_second:
                # print(self.game_ion_now_second)
                self.game_ion_now_second += 1
            if self.game_ion_now_second > IONPOP_GAMETIME:
                self.game_ion_running = False
                self.mainmenu.scene = SCENE_YOU_LOSE
            if self.physics.get_ion_number() == 0:
                self.game_ion_running = False
                self.mainmenu.scene = SCENE_YOU_WIN

            self.ion_to_shoot.x = self.physics.get_position_to_shoot() - 8
            self.ion_to_shoot.type = self.physics.get_ion_type_to_shoot()

    def game_ion_event(self):  
        # print(pyxel.mouse_x, pyxel.mouse_y)
        if self.mainmenu.scene == SCENE_GAME_ION:
            if pyxel.btnp(pyxel.KEY_BACKSPACE):
                # print("P1", self.game_ion_pause, self.game_ion_hold_pause)
                if not self.game_ion_pause and not self.game_ion_hold_pause:
                    self.game_ion_pause_begintime = time.time()
                    self.game_ion_pause = True
                # print("P2", self.game_ion_pause, self.game_ion_hold_pause)
                if self.game_ion_pause and self.game_ion_hold_pause:
                    self.game_ion_pause = False
                self.game_ion_start_time += time.time() - self.game_ion_pause_begintime
            
            if pyxel.btnr(pyxel.KEY_BACKSPACE):
                # print("R1", self.game_ion_pause, self.game_ion_hold_pause)
                if self.game_ion_pause and not self.game_ion_hold_pause:
                    self.game_ion_hold_pause = True
                # print("R2", self.game_ion_pause, self.game_ion_hold_pause)
                if not self.game_ion_pause and self.game_ion_hold_pause:
                    self.game_ion_hold_pause = False

            if not self.game_ion_pause:
                if pyxel.btnr(IONPOP_SHOOT_BOTTOM):
                    self.physics.shoot_ion()
                if self.game_ion_freely_move and time.time() <= self.game_ion_freely_move_endtime:
                    if pyxel.btnp(pyxel.KEY_RIGHT, 1, True) and not pyxel.btnp(pyxel.KEY_LEFT, 1, True):
                        self.physics.set_direction_for_shooter_to_move(2)
                    elif not pyxel.btnp(pyxel.KEY_RIGHT, 1, True) and pyxel.btnp(pyxel.KEY_LEFT, 1, True):
                        self.physics.set_direction_for_shooter_to_move(-2)
                    else:
                        self.physics.set_direction_for_shooter_to_move(0)
                elif self.game_ion_freely_move and time.time() > self.game_ion_freely_move_endtime:
                    self.physics.reset_direction_for_shooter_to_move(self.pre_dx)
                    self.game_ion_freely_move = False
                    # print("Freely move end.")

    def game_ion_draw(self):
        blast_effect = [(1, 80, 0 , 32, 32), (1, 144, 0, 32, 32), (1, 112, 0, 32, 32)]
        pyxel.cls(0)
        reset_color()
        if self.game_ion_exploded[0]:
            for i in range(3):
                pyxel.blt(self.game_ion_exploded[1]-30, self.game_ion_exploded[2], *blast_effect[i])
                pyxel.blt(self.game_ion_exploded[1] + 30, self.game_ion_exploded[2], *blast_effect[i])
                pyxel.blt(self.game_ion_exploded[1], self.game_ion_exploded[2] + 30, *blast_effect[i])
                pyxel.blt(self.game_ion_exploded[1], self.game_ion_exploded[2] -30, *blast_effect[i])
            # pyxel.circ(self.game_ion_exploded[1], self.game_ion_exploded[2], 60, 7)
            self.game_ion_exploded[0] = False
        change_color(1,"393939")
        change_color(2,"666666")
        change_color(13,"969696")
        change_color(9,"FFFFFF")
        change_color(5,"DFDFDF")
        for id in self.ions:
            self.ions[id].draw()
        self.ion_to_shoot.draw()
        if self.game_ion_pause:
            pyxel.tri(150, 150, 150, 250, 250, 200, 13)
        
        if time.time()-self.game_ion_start_time < self.game_ion_now_second - 1:
            pyxel.rectb(5, 375, 36, 16, pyxel.frame_count % 16)
            pyxel.rectb(4, 374, 38, 18, pyxel.frame_count % 16)
            pyxel.text(10, 380, f"time:{self.game_ion_now_second}", pyxel.frame_count % 16)
        else:
            pyxel.rectb(5, 375, 36, 16, 7)
            pyxel.rectb(4, 374, 38, 18, 7)
            pyxel.text(10, 380, f"time:{self.game_ion_now_second}", 7)

    def conv_coord_pyxel2pymunk(point):
        return point[0], window_height - point[1]
    
    def conv_coord_pymunk2pyxel(pymunk_point):
        return pymunk_point[0], window_height - pymunk_point[1]
    
App()

