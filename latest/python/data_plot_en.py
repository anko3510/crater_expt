# 必要なライブラリのインポート
import numpy as np
import matplotlib.pyplot as plt

# 定数の設定
g = 9.8         # 重力加速度 [m/s^2]
m = 13.8e-3     # 鉄球の質量 [kg]

# データのインポート
Data = np.loadtxt("data.dat", delimiter=",")  # データを読み込み
Height = Data[:,0]      # 高さ [cm]（最初の列）
R = Data[:,4] / 2       # 半径 [cm]
R4 = Data[:,5] / 16     # 半径の4乗 [cm^4]（6列目のデータを16で割る）

# プロットの設定
## フォント設定
# plt.rcParams["font.family"] = "IPAexGothic"  # 日本語フォントの設定
plt.rcParams["mathtext.fontset"] = "cm"      # 数式フォントの設定

## 図と軸の設定
fig, ax1 = plt.subplots(layout="constrained")
ax1.set_title(f"Your data : Height {Height[-1]:.3g} cm, Radius {R[-1]:.3g} cm, Energy {(m * g * Height[-1] / 100):.3g} J")
ax1.set_xscale("log")  # X軸を対数スケールに設定
ax1.set_yscale("log")  # Y軸を対数スケールに設定
ax1.set_xlim(10, 200)  # X軸の範囲を設定
ax1.set_ylim(1**4, 4**4)  # Y軸の範囲を設定
ax1.set_xlabel(r"Height $h$ [cm]")  # X軸ラベルを設定
ax1.set_ylabel(r"(Radius)⁴ $r^4$ [cm⁴]")  # Y軸ラベルを設定
ax1.grid(True, which="both", linestyle=":")  # グリッドを表示

# 第2軸の追加
ax2 = ax1.secondary_xaxis("top")  # 上部に第2のX軸を追加
ax2.set_xlabel(r"Impact Energy $E$ [J]")
xticks = ax2.get_xticks()
ax2.set_xticks(xticks, [f"{x:.3g}" for x in (m * g * xticks / 100)])

# データのプロット
ax1.scatter(Height[-1],   R4[-1],   c = "C0", label="Your data")  # 最後のデータ点（あなたの記録）
ax1.scatter(Height[0:-1], R4[0:-1], c = "C1", label="Other data")  # その他のデータ点

# 目安の線のプロット
meyasu_x = np.linspace(5, 200, 100)
mayasu_y0 = 1e1  * meyasu_x
meyasu_y1 = 1e0  * meyasu_x
meyasu_y2 = 1e-1 * meyasu_x
meyasu_y3 = 1e-2 * meyasu_x

# ax1.plot(meyasu_x, meyasu_y0, c = "C2", linestyle=":", label=r"$r^4 = 10 h$")
ax1.plot(meyasu_x, meyasu_y1, c = "C3", linestyle=":", label=r"$r^4 = h$")
ax1.plot(meyasu_x, meyasu_y2, c = "C4", linestyle=":", label=r"$r^4 = 0.1 h$")
ax1.plot(meyasu_x, meyasu_y3, c = "C5", linestyle=":", label=r"$r^4 = 0.01 h$")

# 凡例の表示
ax1.legend(loc="upper left")

# グラフの保存
plt.savefig("graph.svg")
