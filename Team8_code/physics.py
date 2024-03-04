import math
import random
from typing import List
import pymunk

COLLISION_LINE = 9
COLLISION_COMPOUND = 10
INIT_BALL_NUMBER = 10

# ion     type  collision_type
# Cl-       1     11
# Br-       2     11
# I-        3     11
# SO4 2-    4     12
# CrO4 2-   5     13
# S 2-      6     14
# OH-       7     15
# PO4 2-    8     16
# CO3 2-    9     16
# SO3 2-   10     16
# Hg2 2+   11     21
# Cu+      12     21
# Tl+      13     21
# pb 2+    14     22
# Ag+      15     23
# Sr 2+    16     24
# Ba 2+    17     24
# Ca 2+    18     25
# Mg 2+    19     26
# Cu 2+    20     27
# 萬能     21     28  
# 炸彈     22     29  

ION_collision = [0,11,11,11,12,13,14,15,16,16,16,21,21,21,22,23,24,24,25,26,27,28,29]
precipitation_pairs = [(11,21),(11,22),(11,23),(12,22),(12,24),(12,25),
(13,22),(13,23),(13,24),(14,22),(14,23),(14,27),(15,22),(15,23),(15,26),(15,27),
(16,22),(16,23),(16,24),(16,25),(16,26),(16,27),(11,28),(12,28),(13,28),(14,28),
(15,28),(16,28),(21,28),(22,28),(23,28),(24,28),(25,28),(26,28),(27,28),(28,28),
(COLLISION_LINE,29),(COLLISION_COMPOUND, 29),(11,29),(12,29),(13,29),(14,29),
(15,29),(16,29),(21,29),(22,29),(23,29),(24,29),(25,29),(26,29),(27,29),(28,29)]
ION_anti = [[],
[11,12,13,14,15],
[11,12,13,14,15],
[11,12,13,14,15],
[14,16,17,18],
[14,15,16,17],
[14,15,20],
[14,15,19,20],
[14,15,16,17,18,19,20],
[14,15,16,17,18,19,20],
[14,15,16,17,18,19,20],
[1,2,3],
[1,2,3],
[1,2,3],
[1,2,3,4,5,6,7,8,9,10],
[1,2,3,5,6,7,8,9,10],
[4,5,8,9,10],
[4,5,8,9,10],
[4,8,9,10],
[7,8,9,10],
[6,7,8,9,10],
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]]

blue_com = [620, 720, 820, 1020]
black_com = [614, 615]
green_com = [920]
red_com = [515]

bomb_radius = 75

class Physics(object):
    def __init__(self) -> None:
        self._space = pymunk.Space()
        self._space.gravity = (0.0, 0.0)

        self._screen_width = 400
        self._screen_height = 400

        self._now_x = self._screen_width/2
        self._dx = 2

        self.check_collide = False
        self._dt = 1.0 / 60.0
        self._physics_steps_per_frame = 1

        self._add_static_scenery()

        # 沉澱表配對
        self._ions: List[pymunk.Circle] = []
        self._compounds: List[pymunk.Circle] = []
        self._bombs: List[pymunk.Circle] = []
        handler = []
        for i in precipitation_pairs:
            a, b = i[0], i[1]
            hl = self._space.add_collision_handler(a, b)
            hl.data["ions"] = self._ions
            hl.post_solve = self.post_solve_hit
            handler.append(hl)

        self.ions_to_add = []
        self.ions_to_remove = []
        self.compounds_to_remove = []
        self.compounds_to_add = []
        self.ID = 0

        self.exploded = [False, 0, 0]
        self.time_freezer = False
        self.freely_move = False
        self.move_mode = 0

        # 建立初始物件，離子隨機出現在場上
        for i in range(INIT_BALL_NUMBER):
            self.now_ion_type = random.randrange(1, len(ION_collision)-2)
            x = random.randint(25, self._screen_width-25)
            y = random.randint(25, self._screen_height-25)
            self._create_ion(self.now_ion_type, x, y)
        self.now_ion_type = self.new_ion_type()

    def find_com_type(self, ion1, ion2):  # 陰離子*100 + 陽離子
        if ion1.type == 21:      # 萬能 => type > 2100
            return ion1.type*100 + ion2.type
        elif ion2.type == 21:
            return ion1.type + ion2.type*100
        elif ion1.type <= 10 and ion2.type > 10:  # ion1 => anion, ion2 => cation
            return ion1.type*100 + ion2.type
        elif ion1.type > 10 and ion2.type <= 10:  # ion1 => cation, ion2 => anion
            return ion1.type + ion2.type*100

    def become_compound(self, space, ion, target, position, ions):
        x, y = position
        if ion in self._ions and target in self._ions:
            self._ions.remove(ion)
            self._ions.remove(target)
            self.ions_to_remove.append(ion)
            self.ions_to_remove.append(target)
            self._space.remove(ion, ion.body)
            self._space.remove(target, target.body)
            com_type = self.find_com_type(ion, target)
            self._create_compound(com_type, x, y)

    def post_solve_hit(self, arbiter, space, data):
        a, b = arbiter.shapes
        position = arbiter.contact_point_set.points[0].point_a

        if a.collision_type == 29:
            # print(f"bomb at {position}")
            b.collision_type = 0
            b.group = 1
            self.explosion(a, position)
        if b.collision_type == 29:
            # print(f"bomb at {position}")
            b.collision_type = 0
            b.group = 1
            self.explosion(b, position)
        if a.collision_type <= 29 and b.collision_type <= 29:
            b.collision_type = 0
            b.group = 1
            self._space.add_post_step_callback(self.become_compound, b, a, position, data["ions"], )

    def explosion(self, bomb, position):
        self.exploded = [True,position[0],position[1]]
        ions_to_remove = []
        for ion in self._ions:
            if self.distance(position, ion.body.position) <= bomb_radius**2:
                ions_to_remove.append(ion)
        for ion in ions_to_remove:
                self._ions.remove(ion)
                self.ions_to_remove.append(ion)
                self._space.remove(ion, ion.body)
        coms_to_remove = []
        for com in self._compounds:
            if self.distance(position, com.body.position) <= bomb_radius**2:
                coms_to_remove.append(com)
        for com in coms_to_remove:
                self._compounds.remove(com)
                self.compounds_to_remove.append(com)
                self._space.remove(com, com.body)   
             
        self._bombs.remove(bomb)
        self.ions_to_remove.append(bomb)
        self._space.remove(bomb, bomb.body)

    def distance(self, A, B):
        return (A[0]-B[0])**2 + (A[1]-B[1])**2

    def new_ion_type(self):
        rand1 = random.randrange(0, len(self._ions))
        ion = self._ions[rand1]
        rand2 = random.randrange(0, len(ION_anti[ion.type]))
        anti_ion = ION_anti[ion.type][rand2]
        return anti_ion

    def _add_static_scenery(self) -> None:
        static_body = self._space.static_body
        static_lines = [    # 設置牆壁範圍
            pymunk.Segment(static_body, (0.0, 0.0), (0.0, self._screen_height), 0.0),
            pymunk.Segment(static_body, (0.0, self._screen_height-12), (self._screen_width, self._screen_height-12), 0.0),
            pymunk.Segment(static_body, (self._screen_width, self._screen_height), (self._screen_width, 0.0), 0.0),
            pymunk.Segment(static_body, (self._screen_width, 0.0), (0.0, 0.0), 0.0),
        ]
        for line in static_lines:
            line.elasticity = 0.95
            line.friction = 1.0
            line.collision_type = COLLISION_LINE
        static_lines[1].collision_type = 0
        self._space.add(*static_lines)

    def update(self) -> None:
        for x in range(self._physics_steps_per_frame):
            self._space.step(self._dt)
        if self.move_mode == 0:
            if self._now_x >= self._screen_width-8 or self._now_x <= 8:
                self._dx = -self._dx
        if self.move_mode == 1:
            if self._now_x >= self._screen_width-8 and self._dx > 0:
                self._dx = 0
            if self._now_x <= 8 and self._dx < 0:
                self._dx = 0
        self._now_x += self._dx  # 發射位置隨時間改變
        
        for com in self._compounds:
            if com.body.position.y > self._screen_height-30:
                self.specific_effect(com)
                self.compounds_to_remove.append(com)
                self._space.remove(com, com.body)
                self._compounds.remove(com)

    def specific_effect(self, com):
        if com.type in blue_com:  # 萬能離子
            # print("blue com")
            self.now_ion_type = 21
        elif com.type in black_com:  # 凍結時間
            # print("black com")
            self.time_freezer = True
        elif com.type in green_com:  # 自由移動
            # print("green com")
            self.freely_move = True
        elif com.type in red_com:  # 炸彈
            # print("red com")
            self.now_ion_type = 22

    def _create_ion(self, ion_type, x, y, Vx=0, Vy=0) -> None:
        # print("new ion:", ion_type)
        mass = 10
        radius = 8
        inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
        body = pymunk.Body(mass, inertia)
        body.mass = mass
        body.radius = radius
        body.position = x, y
        body.velocity = Vx, Vy
        body.velocity_func = lambda body, gravity, damping, dt: pymunk.Body.update_velocity(body, (0,0), 0.98, self._dt)
        shape = pymunk.Circle(body, radius, (0, 0))
        shape.elasticity = 0.1
        shape.friction = 1.0
        shape.collision_type = ION_collision[ion_type]
        shape.type = ion_type
        shape.ID = self.ID
        self.ID += 1
        self._space.add(body, shape)
        if ion_type == 22:
            # print("create a bomb")
            self._bombs.append(shape)
        else:
            self._ions.append(shape)

    def _create_compound(self, com_type, x, y, Vx=0, Vy=0) -> None:
        # print("new compound:", com_type)
        mass = 20
        radius = 12
        inertia = pymunk.moment_for_circle(mass, 0,radius, (0, 0))
        body = pymunk.Body(mass, inertia)
        body.mass = mass
        body.radius = radius
        body.position = x, y
        body.velocity = Vx, Vy
        body.velocity_func = lambda body, gravity, damping, dt: pymunk.Body.update_velocity(body, (0,6000), 0, self._dt)
        shape = pymunk.Circle(body, radius, (0, 0))
        shape.elasticity = 0.95
        shape.friction = 1.0
        shape.color = (125, 50, 125, 255)
        shape.type = com_type
        shape.collision_type = COLLISION_COMPOUND
        shape.ID = self.ID
        self.ID += 1
        self._space.add(body, shape)
        self._compounds.append(shape)

    def get_particle_info(self): # -> list: 所有離子位置
        return [ion for ion in self._ions] + [com for com in self._compounds] + [bomb for bomb in self._bombs]

    def get_particle_to_remove(self):
        res = [ion.ID for ion in self.ions_to_remove] + [com.ID for com in self.compounds_to_remove]
        self.ions_to_remove = []
        return res
    
    def get_ion_type_to_shoot(self):
        return self.now_ion_type

    def get_ion_number(self):
        return len(self._ions) + len(self._compounds)

    def is_bomb_exploded(self):
        if self.exploded[0]:
            self.exploded[0] = False
            return [True, self.exploded[1], self.exploded[2]]
        return [False, 0, 0]

    def is_time_freezed(self):
        if self.time_freezer:
            self.time_freezer = False
            return True
        return False

    def is_ready_to_freely_move(self):
        if self.freely_move:
            self.freely_move = False
            return True
        return False

    def get_position_to_shoot(self):
        return self._now_x

    def get_direction_for_shooter_to_move(self):
        return self._dx

    def set_direction_for_shooter_to_move(self, dx):
        self.move_mode = 1
        self._dx = dx

    def reset_direction_for_shooter_to_move(self, dx):
        self.move_mode = 0
        self._dx = dx

    def shoot_ion(self):
        Vx = 0
        Vy = -800
        self._create_ion(self.now_ion_type, x=self._now_x , y=self._screen_height, Vx=Vx, Vy=Vy)
        self.now_ion_type = self.new_ion_type()
