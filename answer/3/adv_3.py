# 発展３　反復構造

#変数numを作り、numの値が素数かどうかを判別するプログラムを作りなさい。


# ヒント：反復構造を途中でやめる場合は、「break」を使う

num = 102

if num == 2:
    print(num, "は素数です")

for i in range(2,num,1):
    mod = num % i
    if mod == 0:
        print(num, "は素数ではありません")
        break
    elif i == num - 1:
        print(num, "は素数です")