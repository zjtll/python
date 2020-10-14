#coding=UTF_8
#存储数据
import json
number = [2,3,5,7,11,13]
file1='number.json'     #指定数字列表number存储到文件的名称
with open(file1,'w') as f_json: #写入模式打开文件
    json.dump(number,f_json)     #使用json.dump(number,f_json) 将number列表中的数据存储到number.json中

with open(file1,'r') as f:
    a=json.load(f)           #使用json.load()读取
    print(a)
aaa="dsf  sdf sdf grg  reg"
print(aaa.split())
