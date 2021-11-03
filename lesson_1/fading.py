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

def fading():
    zeros = list([0] * 100 )
    up = list(range (0, 101, 1))
    down = list(reversed(up))

    for r in zeros + up + down:
        pwmR.ChangeDutyCycle(r)
        for g in up + down + zeros:
            pwmG.ChangeDutyCycle(g)
            for b in down + zeros + up:
                pwmB.ChangeDutyCycle(b)
                time.sleep(t)

try:
    while True:
        fading()
        # 调整红绿蓝LED的各个颜色的亮度组合出各种颜色

except KeyboardInterrupt:
    pass
 
pwmR.stop()
pwmG.stop()
pwmB.stop()
 
RPi.GPIO.cleanup()
