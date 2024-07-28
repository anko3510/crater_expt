#!/bin/bash

#ホームディレクトリを取得
HOME=$(pwd | sed -r 's#(([^/]*/){5}).*#\1#')

#main.shのディレクトリを取得
HD=$(pwd)
