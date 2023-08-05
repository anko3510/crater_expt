# クレーター形成実験用スクリプト
このスクリプトはWindows11で動作を確認しています.
## 環境構築
### Windows Terminalのインストール
[Windows Terminal (Microsoft Store)][https://www.microsoft.com/store/productid/9N0DX20HK701?ocid=pdpshare]

### WSL (Debian) のインストール
```PowerShell
wsl --install -d Debian
```

### パッケージの更新
```bash
sudo apt update
sudo apt upgrade
```

### 必要なパッケージのインストール
```bash
sudo apt install gnuplot gnuplot-x11
sudo apt install texlive*
sudo apt install git
```

## 本スクリプトのインストール
デスクトップで右クリック> ターミナルで開く を選び, 以下のコマンドを入力.
```PowerShell
wsl -d debian
```
```bash
git clone https://github.com/anko3510/crater_expt.git
```

## 本スクリプトの実行
デスクトップで右クリック> ターミナルで開く を選び, 以下のコマンドを入力.
```PowerShell
wsl -d debian
```
```bash
cd ./crater_expt/src
chmod +x ./main.sh
./main.sh
```

[def]: url