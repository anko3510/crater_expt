#!/usr/bin/env python3

newest = open("../gnuplot/newest.dat", "r", encoding="utf-8")
newest_old = newest.readline()
newest.close()

newest = open("../gnuplot/old.dat", "a", encoding="utf-8")
newest.write(newest_old)
newest.close()
