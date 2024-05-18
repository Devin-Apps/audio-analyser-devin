import numpy as np
from scipy.signal import stft as scipy_stft, istft as scipy_istft

def fft(audio_data):
    """
    Compute the one-dimensional discrete Fourier Transform.

    Parameters:
    audio_data (numpy.ndarray): The audio signal to transform.

    Returns:
    numpy.ndarray: The transformed audio signal.
    """
    return np.fft.fft(audio_data)

def ifft(transformed_data):
    """
    Compute the inverse one-dimensional discrete Fourier Transform.

    Parameters:
    transformed_data (numpy.ndarray): The transformed audio signal to invert.

    Returns:
    numpy.ndarray: The original audio signal.
    """
    return np.fft.ifft(transformed_data)

def calculate_stft(audio_data, sample_rate, n_fft=2048, hop_length=512, win_length=None):
    """
    Compute the Short-Time Fourier Transform of the audio signal.

    Parameters:
    audio_data (numpy.ndarray): The audio signal to transform.
    sample_rate (int): The sample rate of the audio signal.
    n_fft (int): The number of data points used in each block for the FFT.
    hop_length (int): The number of samples to step forward between blocks.
    win_length (int): The size of the window function.

    Returns:
    tuple: The frequencies, time bins and STFT matrix.
    """
    frequencies, times, stft_matrix = scipy_stft(audio_data, fs=sample_rate, nperseg=n_fft, noverlap=hop_length, nfft=win_length)
    return frequencies, times, stft_matrix

def calculate_istft(stft_matrix, sample_rate, hop_length=512, win_length=None):
    """
    Compute the inverse Short-Time Fourier Transform to reconstruct the audio signal.

    Parameters:
    stft_matrix (numpy.ndarray): The STFT matrix to invert.
    sample_rate (int): The sample rate of the audio signal.
    hop_length (int): The number of samples to step forward between blocks.
    win_length (int): The size of the window function.

    Returns:
    numpy.ndarray: The reconstructed audio signal.
    """
    _, audio_data = scipy_istft(stft_matrix, fs=sample_rate, nperseg=hop_length, nfft=win_length)
    return audio_data
