class Human:
    # コンストラクタを定義する
    def __init__(self, name, age):
        self.name = name
        self.age = age


# インスタンス化する
human = Human("侍太郎", 36)

# 属性にアクセスし、値を出力する
print(human.name)
print(human.age)
