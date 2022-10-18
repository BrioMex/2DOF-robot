
from utime import sleep
from machine import Pin, PWM

class Servo():
    def __init__(self,pin):
        self.pin = pin
        self.pwm = PWM(Pin(self.pin))
        self.pwm.freq(50)
        self.__min=1000
        self.__max=9000
        self.__conversion=(self.__max-self.__min)/180
    
    def move(self,angle: float):
        self.angle = angle
        self.duty=int(self.__min+self.angle*self.__conversion)
        self.pwm.duty_u16(self.duty)
        
    def __str__(self):
        return("Servomotor attached to "+str(self.pin)+" positioned at "+str(self.angle))

if __name__ == '__main__':
    my_servo= Servo(25)
    for i in range(2):
        my_servo.move(0)
        print(my_servo)
        sleep(1)
        my_servo.move(180)
        print(my_servo)
        sleep(1)
    