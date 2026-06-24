# 简易电话簿
phone_book = {}

def add_contact():
    name = input("请输入姓名：")
    tel = input("请输入手机号：")
    phone_book[name] = tel
    print("添加成功！")

def search_contact():
    name = input("查询姓名：")
    if name in phone_book:
        print(f"{name}：{phone_book[name]}")
    else:
        print("无此联系人")

while True:
    print("\n1.添加联系人  2.查询联系人  0.退出")
    op = input("请选择功能：")
    if op == "1":
        add_contact()
    elif op == "2":
        search_contact()
    elif op == "0":
        break
        sda
        sss