# 简介
这个玩具我将其称之为 大宝摇摇乐 或者 界徐盛处刑器

开启程序后，大宝将对周围环境语音进行实时监听
一旦听到了关键词 "铁索连环 古锭刀 酒 火杀"
将会触发目标动作，爆发出一股强劲的音乐和魔性十足的动作

实乃三国杀打牌必备

# 外设连接

在树莓派4b上接入了一个USB麦克风、一个音响，两个LED灯以及一个舵机
舵机接BCM编码16号引脚，两个二极管LED灯接20号引脚

# API调用

调用个人申请的百度API提供的语音识别技术
如果想要使用该程序，请在ASR.py文件里变量中换上自己百度语音识别的Key
（可以在自己的百度语音识别API里加入训练词库，词库里就放"铁索连环 古定刀 酒 火杀"四个词，识别效果会更佳哦）

# 系统信息

	My system is <Raspbian GNU/Linux 11>.
	My Python version is <Python 3.9.2>.
	My SpeechRecognition library version is <3.10.4>.
	My PyAudio library version is < 0.2.14>
	My baidu-aip versiton is <4.16.13>

# 运行

1.请安装好需要的库，不同版本可能会有不适配的问题
2.安装好后，第二步请在ASR.py文件里输入自己的度语音识别的key
3.然后在src文件夹下开启终端输入'python main.py'即可运行
4.关闭程序得用终端'ctrl+C'哦
