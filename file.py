#coding=UTF_8
#""文件和异常基础学习"""
#读取文件内容,open()打开文件，python在当前执行的文件所在的目录中查找指定的文件
#打开文件 file ,将文件对象存储到as后的变量中，使用变量.read()进行读取
"""
with open('file') as file_object:
    con=file_object.read()
    print(con)
"""
#文件路径当要读取的文件和执行的脚本不在一个目录下就需要指定文件的路径
#1、相对路径就是相对于本脚本文本文件的位置、绝对路径即全路径，例如linux从根开始，win从C:\或D:\
#python使用 \ 反斜杠来做转义字符，如果路径要用 \ 反斜杠在前面加个r表示不进行转义，或者用/斜杠表示路径
# with open(r"C:\Users\XSKY\Desktop\file.txt") as test:
#     connn=test.read()
#     print(connn)
#
# #逐行读取
# import time
# with open('file') as row:
#     for i in row:
#         time.sleep(1)
#         print(i.strip())

#将文件内容各行存到列表中
with open('file') as liebiao:
    a=liebiao.readlines()
print(a)
for i in a:
    print(i.strip())

#使用文件中内容
with open('file') as use:
    b=use.readlines()
pi_string=''
for i in b:
    pi_string +=i.strip()
print(pi_string)
print(len(pi_string.strip()))

# #使用replace方法替换字符串
# message="I really like c language"
# print(message)
# print(message.replace("c","python"))
#
# #写入文件，调用open()方法提供俩个实参，第一个时要打开文件的名称，第二个是打开文件的权限，有读'r',写'w',附加'a',读写'r+'，如果省略了实参默认是只读方式打开文件，
# #如果写入的文件不存在会自动创建，‘w’模式写入如果之前文件有数据会先清空
# with open(r"C:\Users\XSKY\Desktop\file2.txt",'w') as test1:
#     test1.write("hadsfha")
import os
import math
#获取文件大小
filesize=os.path.getsize('www.exe')/1024 ** 2
print(filesize)
print(int(math.ceil(float(10)/4)))
import hashlib
tt="aaa"
a=hashlib.md5(tt).hexdigest()
print(a)

