import pyxel,random

# SCENE_GAMEMODE = 0  # no
# SCENE_GAME_PERIOD = 5  # 5
# SCENE_GAME_OVER = 7  # 7

SCENE_MAINMENU = 0
SCENE_MAINMENU2 = 1
SCENE_GAMEMODE = 2
SCENE_PERIOD_EXP = 3
SCENE_ION_EXP = 4
SCENE_GAME_PERIOD = 5
SCENE_GAME_ION = 6
SCENE_GAME_OVER = 7

element=[[0,0],[16,0],[32,0],[48,0],[0,16],[16,16],[32,16],[48,16],[0,32],[16,32],[32,32],[48,32],[0,48],[16,48],[32,48],[48,48],[0,64],[16,64],[32,64],[48,64]]
abcd=[]
coordinate=[[1,1],[18,1],[13,2],[17,2],[1,2],[2,2],[14,2],[18,2],[1,3],[2,3],[15,2],[13,3],[1,4],[2,4],[16,2],[14,3],[15,3],[16,3],[17,3],[18,3]]

class PeriodicTable:
    def __init__(self):
        # pyxel.run(self.update, self.draw)
        pass
    
    def update(self):
        # element=[[0,0],[16,0],[32,0],[48,0],[0,16],[16,16],[32,16],[48,16],[0,32],[16,32],[32,32],[48,32],[0,48],[16,48],[32,48],[48,48],[0,64],[16,64],[32,64],[48,64]]
        # abcd=[]
        # coordinate=[[1,1],[18,1],[13,2],[17,2],[1,2],[2,2],[14,2],[18,2],[1,3],[2,3],[15,2],[13,3],[1,4],[2,4],[16,2],[14,3],[15,3],[16,3],[17,3],[18,3]]
        
        while len(self.appear)==0:
            rand1=random.randrange(0, len(self.ques_pool))
            correct_ans=self.ques_pool[rand1]
            self.ques_pool.pop(rand1)
            self.ABCD.append(coordinate[correct_ans])
            self.correct=self.ABCD[0]
            self.list_element.append(element[correct_ans])
            self.ques=self.list_element.pop(0)
            self.appear.append(self.ques)


        
        while len(self.ABCD)<4:
            randcoordinate=random.randrange(0,len(coordinate))
            abcd.append(coordinate[randcoordinate])
            choice=abcd.pop(0)
            if choice not in  self.ABCD:
                self.ABCD.append(choice)
            else:
                continue
            random.shuffle(self.ABCD)

            
    def question(self):
        #question generate
        # print("#", self.ques)
        pyxel.blt(150,40, 2, self.ques[0],self.ques[1]+160, 16, 16)        
        
    def answer(self):
        #answer selection ABCD
        A=pyxel.rect(60,200,50,35,5)#A
        self.At=self.ABCD[0]
        pyxel.text(70,215,str(self.ABCD[0]),7)
        B=pyxel.rect(220,200,50,35,5)#B
        self.Bt=self.ABCD[1]
        pyxel.text(230,215,str(self.ABCD[1]),7)
        C=pyxel.rect(60,255,50,35,5)#C
        self.Ct=self.ABCD[2]
        pyxel.text(70,270,str(self.ABCD[2]),7)
        D=pyxel.rect(220,255,50,35,5)#D
        self.Dt=self.ABCD[3]
        pyxel.text(230,270,str(self.ABCD[3]),7)
        
    def draw(self):
        for i in range (4):
            #group1
            pyxel.blt(25,60+20*i, 2, 0, 240, 16,16)
        for i in range (3):
            #group2
            pyxel.blt(45,80+20*i, 2, 0, 240, 16,16)
        for i in range (10):
            #transition elements
            pyxel.blt(65+20*i,120, 2, 0, 240, 16,16)
        for i in range (6):
            #group 5-8
            for j in range (3):
                pyxel.blt(265+20*i,80+20*j, 2, 0, 240, 16,16)
        #He
        pyxel.blt(365,60, 2, 0, 240, 16,16)
        PeriodicTable.question(self)
        PeriodicTable.answer(self)
        
class game:
    def check_ans(self):
        pyxel.text(190, 180, '1', 7)
        if 60 <= pyxel.mouse_x <= 60 + 50 and 200 <= pyxel.mouse_y <= 200+35:
            # print(self.At, self.correct)
            if self.At==self.correct:
                self.score+=1
            else:
                self.wrong+=1
        elif 220 <= pyxel.mouse_x <= 220 + 50 and 200 <= pyxel.mouse_y <= 200+35:
            # print(self.Bt, self.correct)
            if self.Bt==self.correct:
                self.score+=1
            else:
                self.wrong+=1
        elif 60 <= pyxel.mouse_x <= 60 + 50 and 255 <= pyxel.mouse_y <= 255+35:
            # print(self.Ct, self.correct)
            if self.Ct==self.correct: 
                self.score+=1
            else:
                self.wrong+=1
        elif 220 <= pyxel.mouse_x <= 220 + 50 and 255 <= pyxel.mouse_y <= 255+35:
            # print(self.Dt, self.correct)
            if self.Dt==self.correct:
                self.score+=1
            else:
                self.wrong+=1
        else: 
            return False
        pyxel.text(20, 20, f"SCORE {self.score}", 7)
        pyxel.text(100, 20, f"SCORE {self.wrong}", 7)
        return True
    
    def end_game(self):
        if self.score + self.wrong == 20:
            self.mainmenu.scene = SCENE_GAME_OVER
            self.game_period_running = False
            
         
class reset():
    def reset_ques(self):
        self.ABCD.clear()
        r=self.appear.pop(0) 
        self.r_appear.append(r)
        PeriodicTable.update(self)
        PeriodicTable.question(self)
        PeriodicTable.answer(self)
    
     
# class App:
#     def __init__(self):
#         pyxel.init(400, 400, display_scale=2, title="Periodic Table", fps = 120)
#         pyxel.load("periodic.pyxres")
#         pyxel.mouse(visible=True)
#         self.scene = SCENE_GAMEMODE
#         #score
#         self.score= 0
#         self.wrong=0
#         #question and choice
#         self.correct=0
#         self.appear=[]
#         self.r_appear=[]
#         self.ques=0
#         self.ABCD=[]
#         self.list_element=[]
#         #answer text
#         self.At=0
#         self.Bt=0
#         self.Ct=0
#         self.Dt=0
        
#         self.x=random.randrange(5)
#         self.y=random.randrange(4)
#         pyxel.run(self.update, self.draw)
        
#     def update(self):
#         if pyxel.btnp(pyxel.KEY_Q):
#             pyxel.quit()
#         if self.scene == SCENE_GAMEMODE:
#             self.update_title_scene()
#         elif self.scene == SCENE_GAME_PERIOD:
#             self.game_period_update()
#         elif self.scene == SCENE_GAME_OVER:
#             self.update_gameover_scene()
        
#     def update_title_scene(self):
#         if pyxel.btnp(pyxel.KEY_RETURN):
#             self.scene = SCENE_GAME_PERIOD
#             self.score=0
#             self.wrong=0

#     def game_period_update(self):  # need
#         PeriodicTable.update(self)
#         if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
#             if game.check_ans(self):
#                 reset.reset_ques(self)
#                 game.end_game(self)

#     def update_gameover_scene(self):   # maybe need
#         if pyxel.btnp(pyxel.KEY_RETURN):
#             self.scene = SCENE_GAMEMODE

#     def draw(self):
#         pyxel.cls(0)
         
#         if self.scene == SCENE_GAMEMODE:
#             self.draw_title_scene()
#         elif self.scene == SCENE_GAME_PERIOD:
#             self.game_period_draw()
#         elif self.scene == SCENE_GAME_OVER:
#             self.draw_gameover_scene()
       
#     def draw_title_scene(self):
#         pyxel.mouse(True)
#         pyxel.blt(40,60, 1,0, 0, 48,48)#P
#         pyxel.blt(80,60, 1,0, 56, 48,48)#E
#         pyxel.blt(120,60, 1,0, 112, 48,48)#R
#         pyxel.blt(160,60, 1,0, 168, 48,48)#I
#         pyxel.blt(200,60, 1,56, 0, 48,48)#O
#         pyxel.blt(240,60, 1,56, 56, 48,48)#D
#         pyxel.blt(280,60, 1,0, 168, 48,48)#I
#         pyxel.blt(320,60, 1,56, 112, 48,48)#C
        
#         pyxel.blt(100,120, 1,56, 168, 48,48)#T
#         pyxel.blt(140,120, 1,112, 0, 48,48)#A
#         pyxel.blt(180,120, 1,112, 56, 48,48)#B
#         pyxel.blt(220,120, 1,112, 112, 48,48)#L
#         pyxel.blt(260,120, 1,0, 56, 48,48)#E
#         pyxel.text(150, 200, "-PRESS ENTER TO START-", 6)
        
#     def game_period_draw(self):
#         pyxel.rectb(15,15,375,160,6)
#         pyxel.text(20, 70, '1', 7)
#         pyxel.text(20, 90, '2', 7)
#         pyxel.text(20, 110, '3', 7)
#         pyxel.text(20, 130, '4', 7)
#         list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
#         for j in range (18):
#             pyxel.text(33+20*j,140,str(list[j]),7)

#         PeriodicTable.draw(self)
#         pyxel.text(20, 20, f"SCORE {self.score}", 7)
#         pyxel.text(100, 20, f"WRONG {self.wrong}", 7)
        
#     def draw_gameover_scene(self):
#         pyxel.blt(120,60, 2,0, 0, 48,48)#G
#         pyxel.blt(160,60, 1,112, 0, 48,48)#A
#         pyxel.blt(200,60, 2,0, 56, 48,48)#G
#         pyxel.blt(240,60, 1,0, 56, 48,48)#E
#         pyxel.blt(120,120, 1,56, 0, 48,48)#O
#         pyxel.blt(160,120, 2,0, 112, 48,48)#V
#         pyxel.blt(200,120, 1,0, 56, 48,48)#E
#         pyxel.blt(240,120, 1,0, 112, 48,48)#R

#         pyxel.text(190, 190, f"SCORE: {self.score}", 7)
#         pyxel.text(190, 205, f"WRONG: {self.wrong}", 7)
#         pyxel.text(150, 220, "- PRESS ENTER To RESTART -", pyxel.frame_count % 16)

# App()