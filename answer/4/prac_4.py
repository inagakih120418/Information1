# 演習４　関数

# 4-1
# 次のプログラムに加筆し、変数a,b,cの値から台形の面積を求める関数を完成させなさい。
# --------------------------------------

def trapezoid(jyoutei, katei, takasa):

    menseki = (jyoutei + katei) * takasa / 2

    return menseki

a = 3; b = 4; c = 5

print(trapezoid(a, b, c))

# --------------------------------------


# 4-2
# 次のプログラムに加筆し、戻り値を使わずに台形の面積を求める関数にしなさい。
# --------------------------------------

def trapezoid_2(jyoutei, katei, takasa):

    global area

    area = (jyoutei + katei) * takasa / 2

a = 3; b = 4; c = 5

trapezoid_2(a, b, c)

print(area)

# --------------------------------------