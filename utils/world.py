import numpy as np
import pyworld as pw
import librosa, math
from hparams import hparams as hp

def logsp_norm(sp):
    return np.clip((sp - hp.sp_min) / (hp.sp_max - hp.sp_min), 0, 1)

def logsp_unnorm(nsp):
    return nsp * (hp.sp_max - hp.sp_min) + hp.sp_min

def world_split(wav, use_ap=True):
    wav = wav.astype(np.float64)
    f0, t = pw.harvest(wav, hp.sample_rate)
    sp = pw.cheaptrick(wav, f0, t, hp.sample_rate)
    if use_ap:
        ap = pw.d4c(wav, f0, t, hp.sample_rate)
        return f0, t, sp, ap
    else:
        return f0, t, sp

def world_join(f0, sp, ap) :
    return pw.synthesize(f0, sp, ap, hp.sample_rate)