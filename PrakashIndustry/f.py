
import aifc
import numpy as np
from numpy.ma import arange
import matlab.engine as me
eng = me.start_matlab()
eng.trie(nargout=0)


filename = '/home/dheeraj/Downloads/Whale Data/whale_data/data/train/train1.aiff'

def featueExtraction(filename):
    c = aifc.open(filename)
    x = c.getsampwidth()
    c = np.real(c)
    n = np.size(c)
    print(c.real.data)
    i_common1 = 0
    i_common2 = 0
    nfft = 512
    nt = 20
    fs = 2000
    dt = 1 / fs
    nf = nfft / 2 + 1
    tt =arange(dt * (nfft - 1) / 2,nt * dt, (n - 1) * dt - (nfft / 2) * dt)
    ntt = np.size(tt)
    # y = np.zeros((nf, ntt),float)
    # s_energy = np.zeros(1, ntt,float)
    # print(y)



    pass









featueExtraction(filename)