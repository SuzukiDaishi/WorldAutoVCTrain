import numpy as np
import librosa, math
from hparams import hparams as hp

def load_wav(filename):
    x = librosa.load(filename, sr=hp.sample_rate)[0]
    return x

def save_wav(y, filename) :
    librosa.output.write_wav(filename, y, hp.sample_rate)