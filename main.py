from servomotor import Servo
from coords import Polar
from math import asin, cos, sin, radians, degrees
from json import dumps
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from utime import sleep

class robot_2dof():    
    def __init__(self, l1:float, l2:float, pin1:int =25, pin2:int =2):
        self.l1 = {"magnitude":l1,"angle":0}
        self.l2 = {"magnitude":l2,"angle":0}
        self.lmaxc = 1/(l1+l2)*(63-16)/2
        self.origin =(64,(64-15)//2+15)
        self.servo1 = Servo(pin1)
        self.servo2 = Servo(pin2)
        self.init_oled()
        self.move_polar()
        
        
        
    def update_position(self):
        C = radians(180-self.l2["angle"])
        magnitude = (self.l1["magnitude"]**2+self.l2["magnitude"]**2-2*self.l1["magnitude"]*self.l2["magnitude"]*cos(C))**(1/2)
        angle = degrees(asin(self.l2["magnitude"]/magnitude*sin(C)))+self.l1["angle"]
        self.position = {"magnitude": magnitude, "angle": angle}
        self.draw_arms()
    
    def rect_position(self):
        pos=Polar(**self.position)
        pos=pos.To_rect()
        return(pos)
        
    def polar_position(self):
        pos=Polar(**self.position)
        return(pos)
    
    def move_polar(self, angle1: float=0, angle2: float=0):
        self.l1["angle"]=angle1
        self.l2["angle"]=angle2
        self.servo1.move(self.l1["angle"])
        self.servo2.move(self.l2["angle"])
        self.update_position()
        
    def init_oled(self):
        i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
        self.oled = SSD1306_I2C(128, 64, i2c)
        self.oled.text("2 DOF Robot sim", 0, 0)
        self.oled.show()
        sleep(1)
        self.draw_axis()
    
    def draw_axis(self):
        self.oled.fill(0)
        self.oled.hline(32,self.origin[1],64,1)
        self.oled.vline(self.origin[0], 16, 64, 1)
        self.oled.show()
    
    def draw_arms(self):
        self.draw_axis()
        pos1=Polar(**self.l1)
        pos1=pos1.To_rect()
        pos1["x"]=pos1["x"]*self.lmaxc
        pos1["y"]=pos1["y"]*self.lmaxc
        
        self.oled.line(self.origin[0], self.origin[1], self.origin[0]+int(pos1["x"]), self.origin[1]-int(pos1["y"]), 1)
        self.oled.show()
        
        pos2=Polar(**self.position)
        pos2=pos2.To_rect()
        self.oled.text("x="+str(round(pos2["x"],2))+"\ty="+str(round(pos2["y"],2)), 0, 0)
        pos2["x"]=pos2["x"]*self.lmaxc
        pos2["y"]=pos2["y"]*self.lmaxc
        self.oled.line(self.origin[0]+int(pos1["x"]), self.origin[1]-int(pos1["y"]), self.origin[0]+int(pos2["x"]), self.origin[1]-int(pos2["y"]),1)
        
        self.oled.show()
        print("x="+str(round(pos2["x"],2))+"\ty="+str(round(pos2["y"],2)))
        
        
if __name__ == "__main__":
    mr=robot_2dof(10,10)
    for angle in range(121):
        mr.move_polar(angle,angle)
        sleep(0.01)
    #mr.move_polar(90,0)