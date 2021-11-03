#!/usr/bin/env python
# encoding: utf-8
import RPi.GPIO
import time

t = 0.1

R,G,B=16,20,21
 
RPi.GPIO.setmode(RPi.GPIO.BCM)
 
RPi.GPIO.setup(R, RPi.GPIO.OUT)
RPi.GPIO.setup(G, RPi.GPIO.OUT)
RPi.GPIO.setup(B, RPi.GPIO.OUT)
 
pwmR = RPi.GPIO.PWM(R, 70)
pwmG = RPi.GPIO.PWM(G, 70)
pwmB = RPi.GPIO.PWM(B, 70)
 
pwmR.start(0)
pwmG.start(0)
pwmB.start(0)
 
try:
    while True:

 # 调整红绿蓝LED的各个颜色的亮度组合出各种颜色
        for r in xrange (0, 101, 2):
            pwmR.ChangeDutyCycle(r)
            for g in xrange (0, 101, 2):
                pwmG.ChangeDutyCycle(g)
                for b in xrange (0, 101, 2):
                    pwmB.ChangeDutyCycle(b)
                    time.sleep(t)
 
except KeyboardInterrupt:
    pass
 
pwmR.stop()
pwmG.stop()
pwmB.stop()
 
RPi.GPIO.cleanup()
