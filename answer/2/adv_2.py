# 発展２　選択構造

# 0から9のランダムな整数の乱数を変数の中に入れて、その値をあてるゲームを作りなさい。
# 以下に手順を示す。

# ・0から9のランダムな整数の乱数を変数aに入れる
# ・imput()関数を使って、変数bの値をプログラム実行時にコンソールから入力できるようにする
# ・aの値とbの値を比べて、値が等しい場合と等しくない場合で選択構造を使う
# ・プログラムの中身を見なくても遊べるように工夫すること。（例：input()関数を使うときに、何を入力すればよいか説明書きをする、など）

# ヒント：input()関数を使って入力した内容は、必ず「文字列」として扱われてしまう。工夫してinput()関数の中身を整数扱いにする方法を探ろう。

import random

a = random.randint(0,9)
b = int(input("数字あてゲーム ~0から9までのどの数字が正解か当てよう~: "))

if(a == b):
    print("正解！")
else:
    print("不正解……。正解は:", a)