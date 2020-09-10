#coding: utf-8
import platform
print("Processor : ", platform.processor())
print("System : ", platform.platform())
print("System Type : " , platform.architecture())
print("Machine Name : ", platform.node())
print("Number Of Processors : " , platform.os.cpu_count())
