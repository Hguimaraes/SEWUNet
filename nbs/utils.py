import os
import copy
import string
import random
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils import data
import torch.nn.functional as F
from librosa import output

class ConfigObject:
    def __init__(self, **entries):
        self.__dict__.update(entries)

def reserve_pop(x):
    # Helper function to reverse a list
    return x[::-1][:-1]

def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
    # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
    return ''.join(random.choice(chars) for _ in range(size))

def writer(x, y, out, sr, path):
    n = x.shape[0]

    for i in range(n):
        # Generate a random hash
        name = id_generator()

        # Create paths
        mix_pf = os.path.join(path, name + '_mixture.wav')
        clean_pf = os.path.join(path, name + '_clean.wav')
        sep_pf = os.path.join(path, name + '_separated.wav')

        # Use librosa to write files
        output.write_wav(mix_pf, x[i, 0, :].cpu().numpy(), sr)
        output.write_wav(clean_pf, y[i, 0, :].cpu().numpy(), sr)
        output.write_wav(sep_pf, out[i, 0, :].cpu().numpy(), sr)

class LibriSpeechGenerator(data.Dataset):
    """Pytorch generator for LibriSpeech
    dataset and UrbanSound 8k noise"""
    def __init__(self, config, X, y = None, mode="noise"):
        self.n_samples = config.n_samples
        self.mode = mode
        
        # Working condition
        if self.mode == "noise" and y is None:
            raise ValueError("y should not be None for Noise mode")
        
        # Datasets
        self.X, self.y = X, y

    def __len__(self):
        return self.X.shape[0]

    def __getitem__(self, index):
        if self.mode == "noise":
            return self.X[index, :, :self.n_samples], self.y[index, :, :self.n_samples]
        else:
            return self.X[index, :, :self.n_samples], self.X[index, :, :self.n_samples]