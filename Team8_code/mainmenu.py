import pyxel
import draw_scene


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


class MainMenu():
    def __init__(self):
        self.scene = SCENE_MAINMENU
        self.mainmenu2_selection_index = 1
        self.gamemode_selection_index = 1
        self.ionexp_selection_index = 0
        self.press_space = False


    def update(self):
        # print("&",self.scene)
        if self.scene == SCENE_MAINMENU:
            self.update_main_menu()
        if self.scene == SCENE_MAINMENU2:
            self.update_main_menu2()
        if self.scene == SCENE_GAMEMODE:
            self.update_gamemode()       
        if self.scene == SCENE_ION_EXP:
            self.update_ion_exp()
        if self.scene == SCENE_PERIOD_EXP:
            self.update_period_exp()
        if self.scene == SCENE_GAME_OVER:
            self.update_you_lose()
        if self.scene == SCENE_YOU_LOSE:
            self.update_you_lose()
        if self.scene == SCENE_YOU_WIN:
            self.update_you_lose()
    def draw(self):
        
        if self.scene == SCENE_MAINMENU:
            draw_scene.draw_main_menu()
        if self.scene == SCENE_MAINMENU2:          
            draw_scene.draw_main_menu2(self.mainmenu2_selection_index)
        if self.scene == SCENE_GAMEMODE:            
            draw_scene.draw_gamemode(self.gamemode_selection_index)
        if self.scene == SCENE_ION_EXP:
            draw_scene.draw_ion_exp(self.ionexp_selection_index)
        if self.scene == SCENE_PERIOD_EXP:
            draw_scene.draw_period_exp()
        if self.scene == SCENE_YOU_LOSE:
            draw_scene.draw_you_lose()
        if self.scene == SCENE_YOU_WIN:
            draw_scene.draw_you_win()
        
    def update_main_menu(self):
        if self.press_space == True and pyxel.btnr(pyxel.KEY_RETURN):
            self.press_space = False
        if self.press_space == False and pyxel.btn(pyxel.KEY_RETURN):
            self.press_space = True
            self.scene = SCENE_MAINMENU2
            

    def update_main_menu2(self):
        
        if self.press_space == True and pyxel.btnr(pyxel.KEY_RETURN):
            self.press_space = False
        if self.press_space == False and pyxel.btnp(pyxel.KEY_RETURN):
            self.press_space = True
            # print(self.mainmenu2_selection_index)
            if self.mainmenu2_selection_index == 0:
                self.scene = SCENE_ION_EXP
            if self.mainmenu2_selection_index == 1:
                self.scene = SCENE_GAMEMODE
                # self.mainmenu2_selection_index = 0
            if self.mainmenu2_selection_index == 2:
                pyxel.quit()
        # print(self.mainmenu2_selection_index)
        # print(self.scene)
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.mainmenu2_selection_index = min(2, self.mainmenu2_selection_index + 1)
        if pyxel.btnp(pyxel.KEY_UP):
            self.mainmenu2_selection_index = max(0, self.mainmenu2_selection_index - 1)

    def update_gamemode(self):
        # print(self.gamemode_selection_index)
        if self.press_space == True and pyxel.btnr(pyxel.KEY_RETURN):
            self.press_space = False
        if self.press_space == False and pyxel.btnp(pyxel.KEY_RETURN):
            self.press_space = True
            if self.gamemode_selection_index == 0:
                self.scene = SCENE_MAINMENU2
                # self.gamemode_selection_index = 1
            if self.gamemode_selection_index == 1:
                self.scene = SCENE_GAME_ION              
            if self.gamemode_selection_index == 2:
                self.scene = SCENE_GAME_PERIOD
                self.gamemode_selection_index = 1
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.gamemode_selection_index = min(2, self.gamemode_selection_index + 1)
        if pyxel.btnp(pyxel.KEY_UP):
            self.gamemode_selection_index = max(0, self.gamemode_selection_index - 1)
    
    def update_ion_exp(self):
        if self.press_space == True and pyxel.btnr(pyxel.KEY_RETURN):
            self.press_space = False
        if self.press_space == False and pyxel.btn(pyxel.KEY_RETURN):
            self.press_space = True
            if self.ionexp_selection_index == 0: 
                self.scene = SCENE_PERIOD_EXP
            if self.ionexp_selection_index == 1:
                self.scene = SCENE_MAINMENU2
        
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.ionexp_selection_index = min(1, self.ionexp_selection_index + 1)
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.ionexp_selection_index = max(0, self.ionexp_selection_index - 1)

    def update_period_exp(self):
        if self.press_space == True and pyxel.btnr(pyxel.KEY_RETURN):
            self.press_space = False
        if self.press_space == False and pyxel.btnp(pyxel.KEY_RETURN):
            self.press_space = True
            self.scene = SCENE_ION_EXP

    def update_you_lose(self):
        if self.press_space == True and pyxel.btnr(pyxel.KEY_RETURN):
            self.press_space = False
        if self.press_space == False and pyxel.btnp(pyxel.KEY_RETURN):
            self.press_space = True
            self.scene = SCENE_MAINMENU
    
    # def update_you_win(self):
    #     if self.press_space == True and pyxel.btnr(pyxel.KEY_RETURN):
    #         self.press_space = False
    #     if self.press_space == False and pyxel.btnp(pyxel.KEY_RETURN):
    #         self.press_space = True
    #         self.scene = SCENE_MAINMENU

    # def update_game_over(self):
    #     if self.press_space == True and pyxel.btnr(pyxel.KEY_RETURN):
    #         self.press_space = False
    #     if self.press_space == False and pyxel.btnp(pyxel.KEY_RETURN):
    #         self.press_space = True
    #         self.scene = SCENE_MAINMENU