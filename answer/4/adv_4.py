# 発展４　関数

# 発展３で作った、素数を判別するプログラムをユーザ定義関数にしなさい。

num = 127

def prime(num):
    if num == 2:
        print(num, "は素数です")
    for i in range(2,num,1):
        mod = num % i
        if mod == 0:
            print(num, "は素数ではありません")
            break
        elif i == num - 1:
            print(num, "は素数です")

prime(num)