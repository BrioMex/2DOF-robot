from math import sin, cos, degrees, radians, atan

class Polar():
        
    def __init__(self,magnitude: float, angle: float):
        self.magnitude = magnitude
        self. angle = angle
    
    def To_rect(self):
        x= self.magnitude*cos(radians(self.angle))
        y= self.magnitude*sin(radians(self.angle))
        return({"x":x,"y":y})
    
    def __str__(self):
        return("Magnitude = "+str(self.magnitude)+"\tAngle = "+str(self.angle))
        

class Rect():
    def __str__(self):
        return('x = '+str(self.x)+'\ty = '+str(self.y))
    
    def __init__(self,x: float, y: float):
        self.x = x
        self. y = y
    
    def To_polar(self):
        magnitude= (self.x**2+self.y**2)**(1/2)
        angle = degrees(atan(self.y/self.x))
        if self.x<0:
            angle += 180
        return({"magnitude":magnitude,"angle":angle})

if __name__ == "__main__":
    polar_coord = Polar(1,45)
    conv_rect =polar_coord.To_rect()
    
    rect_coord = Rect(**conv_rect)
    conv_polar =rect_coord.To_polar()
    
    print(polar_coord,"\n",conv_polar,"\n")
    print(rect_coord,"\n",conv_rect,"\n")