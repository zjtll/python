#coding=UTF_8
#异常try-expect，如果try 代码块中的代码运行起来没有问题，Python将跳过except 代码块；如果try 代码块中的代码导致了
#错误，Python将查找这样的except 代码块，并运行其中的代码，即其中指定的错误与引发的错误相同。
#如果不用try 代码异常的时候程序会结束

try:
    print(5 / 0)
except ZeroDivisionError as e:
    print(e)
#处理文件不存在异常
try:
    with open('file1') as f:
        test=f.read()
        print(test)
except Exception as e:
    print("file not find")

#split()方法以空格为分隔符将字符串拆分为多个部分并存储到一个列表中
title="Alice in Wonderland"
sp=title.split()
print(sp)
print(len(sp))

#count()方法用来统计一个单词在字符串中出现的次数
line="Row, cow, cow your boat"
coun=line.count("cow")
print(coun)
#使用pass异常不做任何处理
try:
    print(1/0)
except Exception as e:
    pass
