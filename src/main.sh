#!/bin/bash

#ホームディレクトリを現在のディレクトリに設定
HD=$(pwd)

#数値データの入力からnewest.datを生成
cd ./python3
python3 data_input.py
cd $HD

#old.datからold10.datを生成
cd ./gnuplot
shuf old.dat | head -10 > old10.dat

#alias mk10dat='shuf old.dat | head -10 > old10.dat'
#mk10dat && gnuplot plot.gpl

#gnuplotでgraph.pdfを生成
gnuplot plot.gpl
cd $HD

#newest.datからold.datに追記
cd ./python3
python3 ./newest_to_old.py
cd $HD
