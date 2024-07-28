#!/bin/bash

# ホームディレクトリを取得
HOME=$(pwd | sed -r 's#(([^/]*/){5}).*#\1#')

# main.shのディレクトリを取得
HD=$(pwd)

# データ入力・グラフ作成・ ./tex/figures/graph.pdf に移動
cd ./python
python data_input.py
echo "グラフ作成中…"
python data_plot.py
mv graph.svg ./../pandoc/figures/graph.svg
cd "$HD"

# 撮影したクレーターの画像を ./tex/figures/crater.jpg にコピー
NEWEST_JPG=$(ls -t "$HOME""Pictures/Camera Roll/"*.jpg | head -n1)
cp "$NEWEST_JPG" ./pandoc/figures/crater.jpg

# pandoc + firefox で印刷する PDF を作成
cd ./pandoc
echo "html 作成中…"
pandoc -s index.md -o index.html -d default.yaml --metadata-file=metadata.yaml
mv index.html ../index.html
cd "$HD"
echo "結果の html"
echo "$HD""/index.html"
