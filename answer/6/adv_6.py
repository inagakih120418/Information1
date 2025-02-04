# 発展６ 探索

# 次の配列を使い、二分探索を行うプログラムを書きなさい。
# （配列以降のプログラムは、なるべくbasicかpracticeの二分探索を参考にすること）

a = ["クッパ", "ピーチ", "マリオ", "ルイージ"]

n = len(a)

s = input("探索値の入力（[\"クッパ\", \"ピーチ\", \"マリオ\", \"ルイージ\"]の内、どれか一つの数を入力） ") # コンソールで配列a の中にある数を一つ入力する（入力した値は変数s に代入される）

lower = 0                                # 変数lower に0（配列a の添え字の最小値）を代入 ……下限値
upper = n - 1                            # 変数upper に n - 1（配列a の添字の最大値）を代入 ……上限値

while lower <= upper:                    # 条件を満たすまで以下を繰り返す
    median = int((lower + upper) / 2)    # 変数median に lower と upper の丁度真ん中になる値を代入（少数切り捨て） ……中央値
    if a[median] == s:                   # もし 「1) 配列a[median] と 変数s が等しい場合」は以下を実行
        print(s, "は", median, "番目に存在")
        break                            # for文やwhile文を強制終了する
    elif a[median] > s:                  # 1) ではなく、もし「2) 配列a[median]が 変数s より大きい場合」は以下を実行
        upper = median - 1
    else:                                # 1) でもなく、2) でもない場合は以下を実行
        lower = median + 1