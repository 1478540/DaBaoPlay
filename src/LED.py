#简单的发光二极管
#短引脚接地，长引脚接signal_pin

import RPi.GPIO as GPIO
import time


#LED灯规律闪烁
# signal_pin: 控制信号引脚BCM编号
# continue_time: 闪烁持续时间(秒)
# delay: 闪烁延迟时间(秒)
# times：闪烁次数
def LEDFlicker(signal_pin,continue_time,delay,times):
    GPIO.setup(signal_pin,GPIO.OUT,initial=False)

    while times>0:
        times=times-1

        GPIO.output(signal_pin,GPIO.HIGH)
        time.sleep(continue_time)
        GPIO.output(signal_pin,GPIO.LOW)
        time.sleep(delay)


def test1(m):
	print(m)
	GPIO.setup(20,GPIO.OUT,initial=False)
	GPIO.output(20,GPIO.HIGH)







