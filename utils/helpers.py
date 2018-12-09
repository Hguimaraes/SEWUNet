import os
import copy
import string
import random
import librosa
import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn.model_selection import train_test_split

import torch
from torch.utils import data


class ConfigObject:
    """Transform a dictionary in a object"""
    def __init__(self, **entries):
        self.__dict__.update(entries)


def getListLibriSpeech(ls_path):
    #  Walk across all folders from LibriSpeech dataset
    # and return a dataset with all path for .flac files
    lp = []
    for root, _, files in os.walk(ls_path):
        for file in files:
            if file.endswith('.flac'):
                lp.append(os.path.join(root, file))

    return lp


def create_tensor(df, config, lsg_params, mode='noise'):
    if mode == 'weight':
        create_tensor_weight(df, config, lsg_params)
    elif mode == 'noise':
        create_tensor_noise(df, config, lsg_params)


def create_tensor_weight(df, config, lsg_params):
    # Split into train and validation
    readers = np.unique(df.READER.values)
    readers_train, readers_val = train_test_split(readers, test_size=0.2)
    df_train = df[df['READER'].isin(readers_train)]
    df_val = df[df['READER'].isin(readers_val)]

    # Call librispeechgenerator
    print(".:. Starting Auto-Encoder Weight Init -TRAIN- data processing .:.")
    lsg = LibriSpeechGenerator(df_train, config)
    ls_generator = data.DataLoader(lsg, collate_fn=customCollate, **lsg_params)
    dataloader_weight_iter(
        ls_generator,
        os.path.join(config.target_weight, 'train', 'train.pt'))

    print(".:. Starting Auto-Encoder Weight Init -VAL- data processing .:.")
    lsg = LibriSpeechGenerator(df_val, config)
    ls_generator = data.DataLoader(lsg, collate_fn=customCollate, **lsg_params)
    dataloader_weight_iter(
        ls_generator,
        os.path.join(config.target_weight, 'val', 'val.pt'))


def create_tensor_noise(df, config, lsg_params):
    # Split into train, validation and test
    readers = np.unique(df.READER.values)
    readers_train, readers_val = train_test_split(readers, test_size=0.2)
    readers_val, readers_test = train_test_split(readers_val, test_size=0.5)

    df_train = df[df['READER'].isin(readers_train)]
    df_val = df[df['READER'].isin(readers_val)]
    df_test = df[df['READER'].isin(readers_test)]

    # Read the US dataset
    # Get UrbanSound and split into train and test
    us_meta_path = os.path.join(config.US_PATH, 'metadata/UrbanSound8K.csv')
    df_us = pd.read_csv(us_meta_path)
    df_us_train, df_us_test = train_test_split(
        df_us, stratify=df_us['class'], test_size=0.2)
    df_us_val, df_us_test = train_test_split(
        df_us_test, stratify=df_us_test['class'], test_size=0.5)

    us_train = UrbanNoise(df_us_train, config)
    us_val = UrbanNoise(df_us_val, config)
    us_test = UrbanNoise(df_us_test, config)

    # Call Librispeech generator
    print(".:. Starting noise data train processing .:.")
    lsg = LibriSpeechGenerator(df_train, urban_sound=us_train, config=config)
    ls_generator = data.DataLoader(lsg, collate_fn=customCollate, **lsg_params)
    dataloader_noise_iter(
        ls_generator,
        os.path.join(config.target_noise, 'train', 'x_train.pt'),
        os.path.join(config.target_noise, 'train', 'y_train.pt'))

    print(".:. Starting noise data val processing .:.")
    lsg = LibriSpeechGenerator(df_val, urban_sound=us_val, config=config)
    ls_generator = data.DataLoader(lsg, collate_fn=customCollate, **lsg_params)
    dataloader_noise_iter(
        ls_generator,
        os.path.join(config.target_noise, 'val', 'x_val.pt'),
        os.path.join(config.target_noise, 'val', 'y_val.pt'))

    print(".:. Starting noise data test processing .:.")
    lsg = LibriSpeechGenerator(df_test, urban_sound=us_test, config=config)
    ls_generator = data.DataLoader(lsg, collate_fn=customCollate, **lsg_params)
    dataloader_noise_iter(
        ls_generator,
        os.path.join(config.target_noise, 'test', 'x_test.pt'),
        os.path.join(config.target_noise, 'test', 'y_test.pt'))


def dataloader_weight_iter(ls_generator, file_name):
    data = []
    device = 'cpu'
    for local_batch, _ in tqdm(ls_generator):
        # Save tensors
        data.append(local_batch.to(device))

    data = torch.cat(data, dim=0)
    torch.save(data, file_name)

    del data


def dataloader_noise_iter(ls_generator, file_x, file_y):
    # Constants
    data = []
    target = []
    device = 'cpu'

    for local_batch, local_label in tqdm(ls_generator):
        # Save tensors
        data.append(local_batch.to(device))
        target.append(local_label.to(device))

    data = torch.cat(data, dim=0)
    target = torch.cat(target, dim=0)

    torch.save(data, file_x)
    torch.save(target, file_y)

    del data, target


def customCollate(batch):
    data = [x[0] for x in batch if x is not None]
    target = [y[1] for y in batch if y is not None]
    return [torch.cat(data, dim=0), torch.cat(target, dim=0)]


class LibriSpeechGenerator(data.Dataset):
    """Pytorch generator for LibriSpeech
    dataset and UrbanSound 8k noise"""
    def __init__(self, ls_paths, config, urban_sound=None):
        self.ls_paths = ls_paths.reset_index(drop=True)
        self.us = urban_sound
        self.samples = config.samples
        self.sr = config.sr

    def __len__(self):
        """
        Total number of samples. Note that we will
        augment this dataset with random noises.
        """
        return len(self.ls_paths)

    def __getitem__(self, index):
        try:
            data = self.ls_paths.path[index]
            y, _ = librosa.load(data, sr=self.sr)
            y = self.split_samples(y)

            # Apply additive noises
            if self.us is not None:
                X = self.__combine_signals(y, self.sr)
            else:
                X = copy.copy(y)

            # Add number of channels
            X = np.expand_dims(X, axis=1)
            y = np.expand_dims(y, axis=1)

            return torch.tensor(X), torch.tensor(y)
        except Exception:
            pass

    def split_samples(self, signal):
        n = signal.shape[0] // self.samples
        splited = np.array_split(signal[:n * self.samples], n)
        return np.array(splited)

    def __combine_signals(self, signals, sr):
        """Function to apply a random noise to the signal"""
        combined = []
        for signal in signals:
            n = signal.shape[0]
            noise, _ = librosa.load(self.us.get_noise()[0], sr=sr)
            m = noise.shape[0]

            # If the audio signal is longer then the noise
            if n >= m:
                # Tile the noise signal
                factor = int(np.ceil(n / m))
                noise = np.tile(noise, factor)[:n]
            else:
                noise = noise[:n]

            # apply additive noise
            snr = np.random.uniform(low=0, high=5)

            combined.append(self.insert_controlled_noise(signal, noise, snr))
        return np.array(combined)

    def insert_controlled_noise(self, signal, noise, desired_snr_db=5):
        if signal.shape[0] != noise.shape[0]:
            raise ValueError("Incompatible shape between noise and signal")

        # Calculate the power of signal and noise
        n = signal.shape[0]
        S_signal = signal.dot(signal) / n
        S_noise = noise.dot(noise) / n

        # Proportion factor
        K = (S_signal / S_noise) * (10 ** (-desired_snr_db / 10))

        # Rescale the noise
        new_noise = np.sqrt(K) * noise

        return new_noise + signal


class UrbanNoise(object):
    """Urban Noise object to insert random noise on datasets"""
    def __init__(self, metadata, config):
        self.us_path = config.US_PATH
        self.metadata = copy.deepcopy(metadata)
        # Possible use only this classes
        # class_n = [0, 2, 3, 5, 9]
        # self.metadata = self.metadata[self.metadata['class'].isin(class_n)]
        self.metadata['path'] = self.metadata.apply(
            lambda x: os.path.join(
                self.us_path,
                'audio',
                'fold' + str(x['fold']),
                x['slice_file_name']
            ), axis=1)

    def get_noise(self):
        """Return a random element from dataframe"""
        return self.metadata.sample(n=1, replace=True)['path'].values
