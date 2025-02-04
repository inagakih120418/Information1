# 演習６ 探索

# 6-1 次のプログラムを修正して、正常に線形探索が行えるようにしなさい。
# --------------------------------------

a = [31, 26, 105, 10, 260, 49, -12, 25, 50]
n = len(a)

s = int(input("探索値の入力（ [31, 26, 105, 10, 260, 49, -12, 25, 50]の内、どれか一つの数を入力） "))

for i in range(0, n, 1):
    if a[n] == s:
        print(s, "は", i, "番目に存在します")
        break

# --------------------------------------



# 6-2 次のプログラムのどこかに「count = count + 1」を記述し、二分探索を繰り返した回数が正しく計算されるようにしなさい。
# --------------------------------------

a = [-12, 10, 25, 26, 31, 49, 50, 105, 260]
n = len(a)

s = int(input("探索値の入力（[-12, 10, 25, 26, 31, 49, 50, 105, 260]の内、どれか一つの数を入力） "))

lower = 0
upper = n - 1
count = 1

while lower <= upper:
    median = int((lower + upper) / 2)
    if a[median] == s:
        print(s, "は", median, "番目に存在")
        print("繰り返し回数: ", count)
        break
    elif a[median] > s:
        upper = median - 1
    else:
        lower = median + 1


# --------------------------------------