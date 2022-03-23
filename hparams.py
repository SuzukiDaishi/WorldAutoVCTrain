class hparams:
    sample_rate = 16000
    
    dim_neck = 32
    dim_emb = 256
    dim_pre = 512
    freq = 32

    hop_length = 256
    seq_len_factor = 64
    seq_len = seq_len_factor * hop_length

    ## world vocoder
    sp_max = 4.3340
    sp_min = -38.6925
