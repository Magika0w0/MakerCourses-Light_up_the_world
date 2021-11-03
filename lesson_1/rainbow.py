#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO
import time

R, G, B = 16, 20, 21

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


def changeR(number):
    pwmR.ChangeDutyCycle(int((255 - number) / 255 * 100))


def changeG(number):
    pwmG.ChangeDutyCycle(int((255 - number) / 255 * 100))


def changeB(number):
    pwmB.ChangeDutyCycle(int((255 - number) / 255 * 100))


def change(red, green, blue):
    changeR(red)
    changeG(green)
    changeB(blue)


def stay(number):
    time.sleep(number)


def fading(t=0.1):
    zeros = list([0] * 100)
    up = list(range(0, 101, 1))
    down = list(reversed(up))

    for b in zeros + up + down:
        pwmB.ChangeDutyCycle(b)
        for g in up + down + zeros:
            pwmG.ChangeDutyCycle(g)
            for r in down + zeros + up:
                pwmR.ChangeDutyCycle(r)
                time.sleep(t)


if __name__ == '__main__':

    try:
        while True:
            ############################实现你的想法#####################
            change(255, 0, 0)  # 改成红色
            stay(5)  # 保持5秒

            change(255, 175, 0) # orange
            stay(5)

            change(255, 255, 0) # yellow
            stay(5)

            change(0, 255, 0) #green
            stay(5)

            change(0, 255, 255) #cyan
            stay(5)

            change(0, 0, 255) #blue
            stay(5)

            change(255, 0, 255) #purple
            stay(5)

        ###########################以下不可以更改########################

    except KeyboardInterrupt:
        pass

pwmR.stop()
pwmG.stop()
pwmB.stop()

RPi.GPIO.cleanup()
