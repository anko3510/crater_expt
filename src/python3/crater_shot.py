#!/usr/bin/env python3

print("クレーターの画像を撮影してください.")
print("撮影しましたか? (y)")
while True:
    check = str(input())
    if check == "y":
        break
    print("不正な入力です. 撮影しましたか? (y)")
