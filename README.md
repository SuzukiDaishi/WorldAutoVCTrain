# WorldAutoVCTrain

This program is a training script for WorldAutoVC, a real-time zero-shot voice quality conversion model.

このプログラムは，リアルタイムゼロショット声質変換モデルであるWorldAutoVCの学習用スクリプトです．

## How to use

```bash
# 
git clone 
cd WorldAutoVCTrain

# JVSデータセットをダウンロードして使える形に変形
./scripts/downloadJVS.sh

# 学習データの準備
python preprocess.py

# 学習する
python train.py
```
