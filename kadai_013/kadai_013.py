def add_two_arguments(price, consumption_tax):
    
  total = price * consumption_tax

  #変数$totalの値を出力する
  print(f"{total}円")

# 関数を呼び出し、引数として購入金額と消費税を渡す
add_two_arguments(1200, 1.1)