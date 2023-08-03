#!/usr/bin/env python3

##データ入力
while True:
    print("衝突体の高さ(cm)を半角数字で入力してEnterを押してください.")
    while True:
        try:
            height = float(input())
        except:
            print("不正な入力値です.")
        else:
            break

    print("1つ目の弦の長さ(cm)を半角数字で入力してEnterを押してください.")
    while True:
        try:
            chord1 = float(input())
        except:
            print("不正な入力値です.")
        else:
            break

    print("2つ目の弦の長さ(cm)を半角数字で入力してEnterを押してください.")
    while True:
        try:
            chord2 = float(input())
        except:
            print("不正な入力値です.")
        else:
            break

    print("3つ目の弦の長さ(cm)を半角数字で入力してEnterを押してください.")
    while True:
        try:
            chord3 = float(input())
        except:
            print("不正な入力値です.")
        else:
            break

    print(f"衝突体の高さ{height}(cm), 弦の長さ{chord1}(cm), {chord2}(cm), {chord3}(cm)です.")
    print("この入力値で正しいですか? (y/n)")
    while True:
        check = str(input())
        if check == "y" or check == "n":
            break
        print("不正な入力です. この入力値で正しいですか? (y/n)")
    
    if check == "y":
        break

D = (4.0*chord1*chord2*chord3)/(2.0*(chord1*chord1*chord2*chord2+chord2*chord2*chord3*chord3+chord3*chord3*chord1*chord1)-chord1*chord1*chord1*chord1-chord2*chord2*chord2*chord2-chord3*chord3*chord3*chord3)**0.5
print(f"直径{D}(cm)です. 直径の4乗は{D**4}(cm^4)です.")
print("合っていますか? (y/n)")
while True:
    check = str(input())
    if check == "y":
        break
    print("不正な入力です. この入力値で正しいですか? (y/n)")


##データ出力
newest = open("../gnuplot/newest.dat", "w", encoding="utf-8")
newest.write(str(height))
newest.write(" ")
newest.write(str(chord1))
newest.write(" ")
newest.write(str(chord2))
newest.write(" ")
newest.write(str(chord3))
newest.write("\n")
newest.close()
