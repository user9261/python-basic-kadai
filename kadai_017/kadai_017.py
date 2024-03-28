class Human:
    # コンストラクタを定義する
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # check_adultメソッドを定義   
    def check_adult(self):
      if self.age >= 20:
           print(f"{self.name}は大人です。")
      else:
           print(f"{self.name}は未成年です。")

#インスタンスを登録するリストの作成
human1 = Human("侍太郎", 36)
human2 = Human("侍一郎", 25)
human3 = Human("侍次郎", 20)
human4 = Human("侍花子", 18)
humans = [human1, human2, human3, human4]

#リストの要素数分だけcheck_adultメソッドを呼び出して出力
for human in humans:
  human.check_adult()  





