import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils import data
import torch.nn.functional as F
import matplotlib.pyplot as plt


class VSConvBlock(nn.Module):
    """"""
    def __init__(self, in_ch, out_ch, activation,
                 dilation=1, padding=0, kernel_size=15):
        """"""
        super(VSConvBlock, self).__init__()
        self.padding = padding

        self.padding_layer = nn.ReflectionPad1d(self.padding)
        self.conv = nn.Conv1d(in_ch, out_ch,
                              kernel_size=kernel_size,
                              stride=1,
                              dilation=dilation)
        self.batch = nn.BatchNorm1d(out_ch)
        self.activation = activation

    def forward(self, x):
        # Block 1
        x = self.padding_layer(x)
        x = self.conv(x)
        x = self.batch(x)
        x = self.activation(x)

        return x


class DownSamplingBlock(nn.Module):
    """Encoder block of the Fully-convolutional Network"""
    def __init__(self, in_ch, out_ch, activation,
                 padding=0, dilation=1, kernel_size=15):
        super(DownSamplingBlock, self).__init__()
        self.block = VSConvBlock(in_ch, out_ch,
                                 activation=activation,
                                 kernel_size=kernel_size,
                                 padding=padding,
                                 dilation=dilation)

    def forward(self, x):
        x = self.block(x)
        return x[:, :, ::2], x


class UpSamplingBlock(nn.Module):
    """Decoder block of the Fully-convolutional Network"""
    def __init__(self, in_ch, out_ch, activation,
                 padding=None, kernel_size=5, mode="linear"):
        super(UpSamplingBlock, self).__init__()
        self.mode = mode
        self.padding = padding or (kernel_size // 2)

        # Convolution block
        self.conv = VSConvBlock(in_ch, out_ch,
                                activation=activation,
                                kernel_size=kernel_size,
                                padding=self.padding)

        # Deconvolution block
        self.deconv = nn.ConvTranspose1d(
            in_channels=in_ch - out_ch,
            out_channels=in_ch - out_ch,
            kernel_size=2,
            stride=2,
            padding=0,
            output_padding=0,
            bias=True,
            dilation=1
        )

        self.deconv_activation = activation

    def forward(self, x, x_enc):
        if self.mode == "linear":
            x = F.interpolate(x, scale_factor=2,
                              mode='linear', align_corners=True)
        else:
            x = self.deconv(x)
            x = self.deconv_activation(x)

        # Concat with Skip connection
        x = torch.cat([x, x_enc], dim=1)
        return self.conv(x)


class OutBlock(nn.Module):
    """Convolutional block similar to VSConvBlock.
    The network input is fed into this layer"""
    def __init__(self, in_ch, out_ch, activation, padding=0):
        super(OutBlock, self).__init__()
        self.conv = VSConvBlock(in_ch, out_ch,
                                activation=activation,
                                kernel_size=1,
                                padding=padding)

    def forward(self, x, x_enc):
        x = torch.cat([x, x_enc], dim=1)
        return self.conv(x) - x_enc
