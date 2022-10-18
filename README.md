# 2DOF-robot
Simple 2 degree of freedom robot for educational purposes.

Required:
1 Raspberry Pi Pico (any model as of 2022)
2 servomotors
1 OLED (ssd1306)

Connections:

servo1 -> 25 (default value)
servo2 -> 2 (default value)

OLED sda -> 0 (can be changed in main.py)
OLED scl ->  1 (can be changed in main.py)

Usage:

For first time use, run main.py and read the ---   if __name__ == "__main__" ---  block in main.py


Functions:

Declare an instance as follows:
  mr=robot_2dof(l1,l2) #Default Pins for servos: 25 and 2

or using:
  mr=robot_2dof(l1,l2, pin1, pin2)

where: 
  l1 and l2 are each arm lenght
  pin1 and pin2 are the GP terminal (integer value) to which each servo will connect.


To move each servo:
  mr.move_polar(angle1,angle2)
 
 where angle1 and angle2 corresponds to the positional degrees value of each Servo.

Each time the servos are moved, this code will print the final position of the second arm 
and will display the graph of the robot in the OLED screen including the final position.
