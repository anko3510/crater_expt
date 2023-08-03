# クレーター形成実験用スクリプト
このスクリプトはWindows11で動作を確認しています.
## 環境構築
### WSL (Debian) のインストール
```PowerShell
wsl --install -d Debian
```

### 必要なパッケージのインストール
```bash
sudo apt install gnuplot gnuplot-x11
sudo apt install texlive*
sudo apt install git
```

## 本スクリプトのインストール
デスクトップでWindows Terminalを起動し以下のコマンドを入力.
```PowerShell
wsl
```
```bash
git clone https://github.com/anko3510/crater_expt.git
```

## 本スクリプトの実行
デスクトップでWindows Terminalを起動し以下のコマンドを入力.
```PowerShell
wsl
```
```bash
cd ./crater_expt/src
chmod +x ./main.sh
./main.sh
```