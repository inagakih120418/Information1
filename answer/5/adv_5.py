# 発展５　配列

# 任意の配列の先頭2要素を結合する関数を作りなさい。
# また、append()を使って、空の配列に2回文を追加し、その配列を作成した関数で使いなさい。
# （配列名、関数名は何でもよい）

# 例）["おはよう"] と ["こんにちは"]を結合して、コンソールに「おはようこんにちは」と表示させる関数

def join(t):
    sentence = t[0] + t[1]
    return sentence

text = []

text.append(input("1文目: "))
text.append(input("2文目: "))

print(join(text))