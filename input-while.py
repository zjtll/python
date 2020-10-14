#coding=UTF_8
#用户输入和while循环
#python 2.7中使用raw_input()获取用户输入解读为字符串，使用input()解读为数字
#python 3 中使用input()获取用户输入并解读为字符串，使用int()解读为数字
# name=raw_input("输入name")
# print(name)
#
# age=input("请输入你的年龄：")
# print(age+1)
#求模运算，% 将俩数相除并返回余数
# print(6%5)
# #向下除取整 // 舍掉余数
# print(7//2)
# num=input("输入一个数：")
# if num%10==0:
#     print("是10的整数")
# else:
#     print("不是10的整数")
# a=1
# while a<=5:
#     print(a)
#     a+=1
# prompt = "Tell me something, and I will repeat it back to you:"
# message = ""
# while message != 'quit':
#     message = raw_input(prompt)
#     if message == 'quit':
#         break
#     else:
#         print(message)
# active=True
# while active:
#     test=raw_input("pls")
#     if test == "quit":
#         active = False
#     else:
#         print(test)
# #使用continue 打印出1-9的奇数 (要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue 语句)
# count=0
# while count < 10:
#     count += 1
#     if count % 2 == 0:
#         continue
#     else:
#         print(count)
#使用while处理列表和字典
#在列表之间移动元素
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#用户输入填充字典
responses={}
policy=True
while policy:
    name=raw_input("输入name:")
    res=raw_input("回答")
    responses[name]=res
    poli=raw_input("还有人回答吗(yes/no)")
    if poli=='no':
        policy=False
    elif poli=='yes':
        continue
    else:
        print("输入值不合法")
        break
for k,y in responses.items():
    print(k + " === " + y + "\n")
print(responses)




