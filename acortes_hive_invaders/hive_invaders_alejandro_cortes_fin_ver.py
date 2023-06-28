# Hive Invaders
# Alejandro Cortes

from tkinter import *
import random
import tkinter.messagebox as messagebox

width = 1400
height = 800

red_wasp_path = "hive_invaders_red_wasp.png"
blue_wasp_path = "hive_invaders_blue_wasp.png"
bee_path = "hive_invaders_bee.png"
honey_spit_path = "hive_invaders_honey_spit.png"

root = Tk()
root.title('Hive Invaders! <Arrows> To Move! <Space> To Shoot!')
root.resizable(False, False)

canvas = Canvas(root, background = 'black', width = width, height = height)
canvas.pack()

class Spit:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.image = PhotoImage(file = honey_spit_path)
        self.x = x
        self.y = y
        self.y_change = 5
        
    def move(self):
        self.y -= self.y_change
            
    def draw(self):
        self.canvas.create_image(self.x, self.y, anchor = CENTER, image = self.image)
        
    def check_collision(self, wasps):
        for wasp in wasps:
            if (self.x > wasp.x - wasp.image.width() / 2
                and self.x < wasp.x + wasp.image.width() / 2
                and self.y > wasp.y - wasp.image.height() / 2
                and self.y < wasp.y + wasp.image.height() / 2):
                wasps.remove(wasp)
                return True
        return False
                
        
class Bee:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = PhotoImage(file = bee_path)
        self.x = 700
        self.y = (height - self.image.height())
        self.spits = []
        
    def move_left(self, event):
        if self.x > (0 + self.image.width()):
            self.x -= 15
            
    def move_right(self, event):
        if self.x < (width - self.image.width()):
            self.x += 15
            
    def spit_honey(self, event):
        spit = Spit(self.canvas, self.x, self.y)
        self.spits.append(spit)
        
    def update_spits(self):
        for spit in self.spits:
            spit.move()
            if spit.y < 0 or spit.check_collision(wasps):
                self.spits.remove(spit)
                
    def draw_spits(self):
        for spit in self.spits:
            spit.draw()
    
    def draw(self):
        self.canvas.create_image(self.x, self.y, anchor = CENTER, image = self.image)
        
class Wasp:
    direction = 1
    def __init__(self, canvas, x, y, color, difficulty):
        self.canvas = canvas
        self.image = PhotoImage(file = color)
        self.x = x
        self.y = y
        self.x_change = difficulty
        self.y_change = self.image.height() // 2

    def move_side(self):
        self.x += self.x_change * self.direction
        if self.x <= (0 + self.image.width()) or self.x >= (width - self.image.width()):
            Wasp.direction *= -1
            self.move_down()
            
    def move_down(self):
        for wasp in wasps:
            wasp.y += self.y_change
            
    def draw(self):
        self.canvas.create_image(self.x, self.y, anchor = CENTER, image = self.image)

wasp_x_spawn_locations = [325, 450, 575, 700, 825, 950, 1075]
wasp_y_spawn_locations = [60, 140, 220, 300]
wasps = []

wasp_colors = ['red', 'blue']
for y in wasp_y_spawn_locations:
    for x in wasp_x_spawn_locations:
        color = random.choice(wasp_colors)
        if color == ('red'):
            wasps.append(Wasp(canvas, x, y, red_wasp_path, 2))
        if color == ('blue'):
            wasps.append(Wasp(canvas, x, y, blue_wasp_path, 2))

bee = Bee(canvas)
root.bind('<Left>', bee.move_left)
root.bind('<Right>', bee.move_right)
root.bind('<space>', bee.spit_honey)

def check_win_con():
    if len(wasps) == 0:
        result = messagebox.askquestion("You Won!", "You Won! Play again?")
        if result == 'yes':
            restart()
        else:
            exit(0)

def restart():
    canvas.delete(ALL)
    bee.spits.clear()
    wasps.clear()    
    for y in wasp_y_spawn_locations:
        for x in wasp_x_spawn_locations:
            color = random.choice(wasp_colors)
            if color == ('red'):
                wasps.append(Wasp(canvas, x, y, red_wasp_path, 4))
            if color == ('blue'):
                wasps.append(Wasp(canvas, x, y, blue_wasp_path, 8))

def game_loop():
    canvas.delete(ALL)
    bee.draw()
    bee.update_spits()
    bee.draw_spits()
    for wasp in wasps:
        wasp.move_side()
        wasp.draw()
        if wasp.y >= height - wasp.image.height() / 2:
            result = messagebox.askquestion("You Lost!", "You Lost! Play again?")
            if result == 'yes':
                restart()
            else:
                exit(0)
    check_win_con()
    root.update()
    root.after(30, game_loop)

game_loop()
root.mainloop()