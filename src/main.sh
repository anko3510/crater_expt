#!/bin/bash

#ホームディレクトリを取得
HOME=$(pwd | sed -r 's#(([^/]*/){5}).*#\1#')

#main.shのディレクトリを取得
HD=$(pwd)

#クレーターの画像を撮影,  tex/figures/crater.jpgにコピー
cd ./python3
python3 crater_shot.py
cd "$HD"

cd "$HOME""Pictures/Camera Roll/"
NEWEST_JPG=$(ls -t *.jpg | head -n1)
cd "$HD"

cd ./tex/figures
cp "$HOME""Pictures/Camera Roll/""$NEWEST_JPG" ./crater.jpg
cd "$HD"

#数値データの入力からnewest.datを生成
cd ./python3
python3 data_input.py
cd "$HD"

#old.datからold10.datを生成
cd ./gnuplot
shuf old.dat | head -10 > old10.dat

#alias mk10dat='shuf old.dat | head -10 > old10.dat'
#mk10dat && gnuplot plot.gpl

#gnuplotでgraph.pdfを生成, tex/figures/graph.pdfにコピー
gnuplot plot.gpl
cp -f graph.pdf ../tex/figures/graph.pdf
cd "$HD"

#newest.datからold.datに追記
cd ./python3
python3 ./newest_to_old.py
cd "$HD"
