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

    print("クレーターの直径(mm)を半角数字で入力してEnterを押してください.")
    while True:
        try:
            diameter = float(input())
        except:
            print("不正な入力値です.")
        else:
            break

    print(f"衝突体の高さ{height}(cm), クレーターの直径{diameter}(mm)です.")
    print("この入力値で正しいですか? (y/n)")
    while True:
        check = str(input())
        if check == "y" or check == "n":
            break
        print("不正な入力です. この入力値で正しいですか? (y/n)")
    
    if check == "y":
        break

##データ出力
newest = open("../gnuplot/newest.dat", "w", encoding="utf-8")
newest.write(str(height))
newest.write(" ")
newest.write(str(diameter))
newest.write("\n")
newest.close()
