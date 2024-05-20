
import LED
import SG90
import GPIO
import threading
import SoundPlay
import time
import ASR
 

def goal_function():
	# 创建线程对象，目标函数是swing_servo，传递参数给该函数
	thread_servo = threading.Thread(target=SG90.SwingFunction, args=(16,80,0.2,32))
	# 创建线程对象，目标函数是blink_led，传递参数给该函数
	thread_led = threading.Thread(target=LED.LEDFlicker, args=(20,0.1,0.1,64))
	thread_music = threading.Thread(target=SoundPlay.MusicPlay)
	
#	# 启动线程
	thread_music.start()
	time.sleep(6)
	thread_led.start()
	thread_servo.start()

	
#	# 等待所有线程完成
	thread_servo.join()
	thread_led.join()
	thread_music.join()

if __name__ == '__main__':
	GPIO.initialGPIO()

	try:
		print('程序开始:')

		while True:
			if ASR.Trigger_ASR_BaiduApi():
				goal_function()
				
		print('程序结束')
	except Exception as err:
		print(err)
	finally:
		GPIO.overGPIO()
	
	

