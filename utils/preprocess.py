import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from helpers import ConfigObject
from helpers import getListLibriSpeech
from helpers import create_tensor

# Increase resource limit
# import resource
# rlimit = resource.getrlimit(resource.RLIMIT_NOFILE)
# resource.setrlimit(resource.RLIMIT_NOFILE, (16384, rlimit[1]))

# Parameters
_params = {
    "SET_SEED": 1234,
    "test_size": 0.2,
    "LS_PATH": '../data/raw_data/LibriSpeech/',
    "US_PATH": '../data/raw_data/UrbanSound8K/',
    "sr": 16000,
    "samples": 65536,
    "target_weight": "../data/processed/aewi/",
    "target_noise": "../data/processed/noisy/"
}

# Data loader parameters to generate the tensors
np.random.seed(_params['SET_SEED'])
lsg_params = {
    'batch_size': 32,
    'shuffle': False,
    'num_workers': 8
}


def main():
    config = ConfigObject(**_params)

    # Get librispeech and split into train and test
    ls_paths = getListLibriSpeech(config.LS_PATH)
    ls_df = pd.DataFrame({'path': ls_paths})
    ls_df['READER'] = ls_df['path'].apply(lambda x: x.split('/')
                                                     .pop()
                                                     .split('-')[0])

    # # Split into train for weight init network and for training the network
    # readers = np.unique(ls_df.READER.values)
    # readers_init, readers_net = train_test_split(readers, test_size=0.5)
    # ls_df_init = ls_df.loc[ls_df['READER'].isin(readers_init)]
    # ls_df_net = ls_df.loc[ls_df['READER'].isin(readers_net)]

    # # Create the tensors for weight init and full-network
    # create_tensor(ls_df_init, config, lsg_params, 'weight')
    # create_tensor(ls_df_net, config, lsg_params)


if __name__ == '__main__':
    main()
