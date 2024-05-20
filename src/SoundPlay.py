import pygame


def MusicPlay():

	# 初始化pygame
	pygame.mixer.init()
	
	# 加载第一个.wav文件
	sound1 = pygame.mixer.Sound('output1.wav')
	# 设置第一个文件的音量为100%
	sound1.set_volume(0.9)
	# 播放第一个文件
	sound1.play()
	# 等待第一个文件播放完成
	while pygame.mixer.get_busy():
	    pygame.time.delay(100)
	
	# 加载第二个.wav文件
	sound2 = pygame.mixer.Sound('back.wav')
	# 设置第二个文件的音量为10%
	sound2.set_volume(0.4)
	# 播放第二个文件
	sound2.play()
	# 等待第二个文件播放完成
	while pygame.mixer.get_busy():
	    pygame.time.delay(100)

#	 加载第二个.wav文件
	sound3 = pygame.mixer.Sound('over.wav')
	# 设置第二个文件的音量为10%
	sound3.set_volume(0.9)
	# 播放第二个文件
	sound3.play()
	# 等待第二个文件播放完成
	while pygame.mixer.get_busy():
	    pygame.time.delay(100)