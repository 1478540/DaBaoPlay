#调用百度API实现语音识别

import time
from aip import AipSpeech
import speech_recognition as sr
import numpy as np
import math



# 请在这边输入自己相应的
# 百度语音识别的 APP_ID, API_KEY, SECRET_KEY
APP_ID = 'xxxxxx'
API_KEY = 'xxxxxxxx'
SECRET_KEY = 'xxxxxxx'
# 初始化百度语音识别客户端
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)



#录音一句话并识别，请确保插入麦克风
# total_time: 录音最长时常
# delay_time: 最长允许延迟时常(开始录音delay_time后若没有声音则结束)
def SHORT_ASR_BaiduApi(total_time,delay_time):
    
    global client

    # 初始化识别器
    r = sr.Recognizer()

    # 从默认麦克风获取数据
    with sr.Microphone(sample_rate=48000) as source:
        print("请说话...")
        audio = r.listen(source, timeout=delay_time, phrase_time_limit=total_time)

    # 转换为符合百度API要求的格式：PCM数据(推荐)、单声道、16000采样率、16位小端序
    audio_data = audio.get_raw_data(convert_rate=16000, convert_width=2)

    # 使用百度语音识别
    try:
        print("百度语音识别结果：")
        result = client.asr(audio_data, 'pcm', 16000, {'dev_pid': 1537})

        # 输出识别结果
        if result['err_no'] == 0:
            return result['result']
        else:
            print("百度语音识别错误信息：", result['err_msg'])
    except sr.UnknownValueError:
        print("无法理解音频")
    except sr.RequestError as e:
        print("服务请求错误; {0}".format(e))




password=['铁索连环','古定刀','酒','火杀']
global_is_set=True               #用于Trigger_ASR_BaiduApi函数全局变量,判断Trrigger_ASR_BaiduApi是否应该退出

#在一段对话中等待口令，直到识别口令才返回True
# password: 用于验证的口令字符串数组
def Trigger_ASR_BaiduApi():
    global global_is_set
    global_is_set=True 
     
    # 初始化识别器
    r = sr.Recognizer()
    m = sr.Microphone(sample_rate=48000)

    r.dynamic_energy_threshold=False #关闭动态调整噪音环境，严格控制噪音水准
    r.energy_threshold=3000  #手动设置噪音阈值

    with m as s:
        print("请说话...")
        while True:
            audio=r.listen(s,phrase_time_limit=10)
            process_audio(r,audio)

            if not global_is_set:
                break
    
    return True


#处理音频的回调函数，返回值无实际意义，关键在于对全局变量global_is_set的设置
def process_audio(recognizer, audio):
    global password
    global global_is_set

    try:
        # 转换为符合百度API要求的格式：PCM数据(推荐)、单声道、16000采样率、16位小端序
        audio_data = audio.get_raw_data(convert_rate=16000, convert_width=2)

        text=process_data(audio_data)
        if check_password(text,password,0.5):
            global_is_set=False
            return True

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


#使用百度API，返回语音识别的字符串
def process_data(data):
    global client

    # 使用百度语音识别
    try:
        print("百度语音识别结果：")
        result = client.asr(data, 'pcm', 16000, {'dev_pid': 1537})

        # 判断识别结果
        if result['err_no'] == 0:
            text=result['result']
            print(text[0])
            return text[0]
        
    except Exception as e:
        print(f"处理音频时出错: {e}")


#检测目标字符串是否包含口令
# data 是一个目标字符串
# password 是作为密钥的字符串数组
# right_rate 只要识别出的词组占据password的比例达到right_rate，即返回True
def check_password(data, password, right_rate):
    # 如果 data 不是字符串类型，则直接返回 False
    if not isinstance(data, str):
        return False
        
    # 统计符合条件的密码字符串数量
    matching_count = 0
    
    # 遍历密码数组中的每一个密码
    for pwd in password:
        # 如果密码中的字符严格按照顺序出现在数据字符串中，认为密码符合条件
        if pwd in data:
            matching_count += 1

    # 计算需要满足条件的最小密码字符串数量（向上取整）
    required_count = math.ceil(len(password) * right_rate)
    
    # 如果符合条件的密码字符串数量达到或超过所需数量，返回True
    return matching_count >= required_count








