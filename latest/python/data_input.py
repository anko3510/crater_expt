# データ入力とプロット用スクリプト

# 衝突体の高さを入力
while True:
    print("衝突体の高さ(cm)を半角数字で入力してEnterを押してください.")
    while True:
        try:
            height = float(input(">>>"))  # 高さを入力
        except ValueError:
            print("不正な入力値です. 数字を入力してください.")
        else:
            break

    print(f"衝突体の高さは {height:5.1f} cm です.")
    print("この入力値で正しいですか? (y/n)")
    while True:
        check = input(">>>").strip().lower()
        if check in ("y", "n"):
            break
        print("不正な入力です. yまたはnで答えてください.")
    
    if check == "y":
        break

print()
print("衝突体を落としてクレーターを作成してください．")
print("作成しましたか？(y)")
while True:
    check = input(">>>").strip().lower()
    if check == "y":
        break
    print("不正な入力です. yで答えてください.")

print()
print("クレーターの画像を撮影してください.")
print("撮影しましたか? (y)")
while True:
    check = input(">>>").strip().lower()
    if check == "y":
        break
    print("不正な入力です. yで答えてください.")
print()

# クレーターの弦の長さを入力
while True:
    print("1つ目の弦の長さ(cm)を半角数字で入力してEnterを押してください.")
    while True:
        try:
            chord1 = float(input(">>>"))  # 1つ目の弦の長さを入力
        except ValueError:
            print("不正な入力値です. 数字を入力してください.")
        else:
            break

    print()
    print("2つ目の弦の長さ(cm)を半角数字で入力してEnterを押してください.")
    while True:
        try:
            chord2 = float(input(">>>"))  # 2つ目の弦の長さを入力
        except ValueError:
            print("不正な入力値です. 数字を入力してください.")
        else:
            break

    print()
    print("3つ目の弦の長さ(cm)を半角数字で入力してEnterを押してください.")
    while True:
        try:
            chord3 = float(input(">>>"))  # 3つ目の弦の長さを入力
        except ValueError:
            print("不正な入力値です. 数字を入力してください.")
        else:
            break

    print()
    print(f"弦の長さは {chord1:5.2f} cm, {chord2:5.2f} cm, {chord3:5.2f} cm です.")
    print("この入力値で正しいですか? (y/n)")
    while True:
        check = input().strip().lower()
        if check in ("y", "n"):
            break
        print("不正な入力です. yまたはnで答えてください.")
    
    if check == "y":
        break

# クレーターの直径とその4乗を計算
D = (2.0 * chord1 * chord2 * chord3) / (2.0 * (chord1**2 * chord2**2 + chord2**2 * chord3**2 + chord3**2 * chord1**2) - chord1**4 - chord2**4 - chord3**4)**0.5
print()
print(f"クレーターの直径は{D:5.2f} cm です. 直径の4乗は{D**4:5.2e} cm^4 です.")

# データをファイルに書き込む
with open("./data.dat", "a", encoding="utf-8") as newest:
    newest.write(f"{height}, {chord1}, {chord2}, {chord3}, {D}, {D**4}\n")
