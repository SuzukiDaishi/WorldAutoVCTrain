# WorldAutoVCTrain

This program is a training script for WorldAutoVC, a real-time zero-shot voice quality conversion model.  

AutoVC.pytorch by peisuke is used in some parts of this program.  

本プログラムは，リアルタイムゼロショット声質変換モデルであるWorldAutoVCの学習用スクリプトです．  

本プログラムの一部で，peisuke氏の[AutoVC.pytorch](https://github.com/peisuke/AutoVC.pytorch)を使用しています．

## How to use

```bash
# clone
git clone https://github.com/SuzukiDaishi/WorldAutoVCTrain.git
cd WorldAutoVCTrain

# Download JVS corpus
./scripts/downloadJVS.sh

# Dataset processing
python preprocess.py

# train model
python train.py
```

# References
- [peisuke/AutoVC.pytorch](https://github.com/peisuke/AutoVC.pytorch): Used in part in this repository.
- [auspicious3000/autovc](https://github.com/auspicious3000/autovc): Original implementation of AutoVC.
- [AUTOVC: Zero-Shot Voice Style Transfer with Only Autoencoder Loss](https://arxiv.org/abs/1905.05879): AutoVC's paper.
- [JVS (Japanese versatile speech) corpus](https://sites.google.com/site/shinnosuketakamichi/research-topics/jvs_corpus): This is the dataset used in this program.