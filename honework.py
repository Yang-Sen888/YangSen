players={}

def add_player():
    name=input("输入球员的名字：")
    if name in players:
        print("输入重复")
        return
    age=input("请输入球员年龄：")
    team=input("请输入所属球队：")
    players[name]={"年龄":age,"队伍":team}
    print("添加成功")

add_player()