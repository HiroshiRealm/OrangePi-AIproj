# OrangePi-AIproj
在香橙派本地部署一个拥有真人语调的同声传译器

## 项目阶段性任务目标

我们这个project有两个主要可以优化的方向，可以采用迭代开发的方式：
1. 先做一个在线版本，后做离线版本。也就是一个需要联网，另一个不需要联网。（也就是speech recognition和machine translation这两过程，目前是直接调用联网API更加省事，下一个版本再考虑将模型放在本地。）
2. 可以先做一个非实时IO版本，也就是输入一段A语言音频，将这段音频用相同语气但是B语言输出。后做实时版本，也就是支持从麦克风输入，从扬声器输出。（prototype中是从麦克风输入从扬声器输出的。但是并不清楚用了Sovits之后性能如何，能否支持这种"实时转换"）

## To-do list(序号代表顺序)
1. 在香橙派上跑通prototype (目前在x86-Windows下能成功运行, 但香橙派是 Ascend-Linux)
1. 找到用shell/python脚本等非WebGUI进行GPT-sovits推理的方式。集成到prototype中在x86-windows下跑通
2. 将使用了sovits模型的python程序迁移到香橙派上并能成功运行( 里面应该还有一些问题, 比如说用pytorch写的sovits代码能不能正常在香橙派下运行, 以及原先下载好的模型格式是不是需要更改等, 尚未尝试)
3. 做PPT，写实验报告。完成一个初步能交的版本
4. 根据时间尝试将speech recognition和machine translation 选择一个小模型下载下来部署到本地. 
