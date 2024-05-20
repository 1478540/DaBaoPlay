#SG90舵机利用pwm原理工作
#红线(中间)连接5V电压，棕/黑线连接GND，橙色线连接信号引脚


import RPi.GPIO as GPIO
import time

#该函数为控制 舵机按照一定的角度来回摆动
# signal_pin: 控制信号引脚BCM编号
# angle: 来回偏转角度（0~180）
# delay: 延迟时间(秒)
# times：来回摆动次数
def SwingFunction(signal_pin,angle,delay,times):
    GPIO.setup(signal_pin,GPIO.OUT,initial=False)
    p=GPIO.PWM(signal_pin,50) #频率50Hz，周期20ms

    duty_cycle=angle/18+2.5 #计算占空比
    p.start(0)

    while times>0 :
        times=times-1

        p.ChangeDutyCycle(2.5)
        time.sleep(delay)
        p.ChangeDutyCycle(duty_cycle)
        time.sleep(delay)
    
    p.stop()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
SwingFunction(21,90,0.4,10)

