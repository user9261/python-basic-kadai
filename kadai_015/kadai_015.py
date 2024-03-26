class Human:
    # コンストラクタを定義する
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # printinfoメソッドを定義   
    def printinfo(self):
      print("名前:",self.name)
      print("年齢:",self.age)  


# インスタンス化する
human = Human("侍太郎", 36)

# printinfoメソッドにアクセスして値を出力する
human.printinfo()
