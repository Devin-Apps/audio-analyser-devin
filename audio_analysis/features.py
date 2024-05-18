import numpy as np
from scipy.fftpack import dct

def mfcc(signal, sample_rate, num_ceps=13, n_fft=2048, hop_length=512, n_mels=40):
    """
    Compute the Mel-frequency cepstral coefficients (MFCC) for an audio signal.

    Parameters:
    signal (numpy.ndarray): The audio signal from which to compute features.
    sample_rate (int): The sample rate of the signal we are working with.
    num_ceps (int): The number of cepstral coefficients to return.
    n_fft (int): The number of data points used in each block for the FFT.
    hop_length (int): The number of samples to step forward between blocks.
    n_mels (int): The number of Mel bands to generate.

    Returns:
    numpy.ndarray: A 2D array of shape (num_ceps, number of frames) containing the MFCC.
    """
    # Pre-emphasis filter
    pre_emphasis = 0.97
    emphasized_signal = np.append(signal[0], signal[1:] - pre_emphasis * signal[:-1])

    # Framing
    frame_length, frame_step = n_fft, hop_length
    signal_length = len(emphasized_signal)
    frame_length = int(round(sample_rate * 0.025))
    frame_step = int(round(sample_rate * 0.01))
    num_frames = int(np.ceil(float(np.abs(signal_length - frame_length)) / frame_step))

    pad_signal_length = num_frames * frame_step + frame_length
    z = np.zeros((pad_signal_length - signal_length))
    pad_signal = np.append(emphasized_signal, z)

    indices = np.tile(np.arange(0, frame_length), (num_frames, 1)) + np.tile(np.arange(0, num_frames * frame_step, frame_step), (frame_length, 1)).T
    frames = pad_signal[indices.astype(np.int32, copy=False)]

    # Windowing
    frames *= np.hamming(frame_length)

    # Fourier-Transform and Power Spectrum
    NFFT = n_fft
    mag_frames = np.absolute(np.fft.rfft(frames, NFFT))  # Magnitude of the FFT
    pow_frames = ((1.0 / NFFT) * ((mag_frames) ** 2))  # Power Spectrum

    # Filter Banks
    low_freq_mel = 0
    high_freq_mel = (2595 * np.log10(1 + (sample_rate / 2) / 700))  # Convert Hz to Mel
    mel_points = np.linspace(low_freq_mel, high_freq_mel, n_mels + 2)  # Equally spaced in Mel scale
    hz_points = (700 * (10**(mel_points / 2595) - 1))  # Convert Mel to Hz
    bin = np.floor((n_fft + 1) * hz_points / sample_rate)

    fbank = np.zeros((n_mels, int(np.floor(n_fft / 2 + 1))))
    for m in range(1, n_mels + 1):
        f_m_minus = int(bin[m - 1])   # left
        f_m = int(bin[m])             # center
        f_m_plus = int(bin[m + 1])    # right

        for k in range(f_m_minus, f_m):
            fbank[m - 1, k] = (k - bin[m - 1]) / (bin[m] - bin[m - 1])
        for k in range(f_m, f_m_plus):
            fbank[m - 1, k] = (bin[m + 1] - k) / (bin[m + 1] - bin[m])

    filter_banks = np.dot(pow_frames, fbank.T)
    filter_banks = np.where(filter_banks == 0, np.finfo(float).eps, filter_banks)  # Numerical Stability
    filter_banks = 20 * np.log10(filter_banks)  # dB

    # MFCCs
    mfcc = dct(filter_banks, type=2, axis=1, norm='ortho')[:, 1 : (num_ceps + 1)]  # Keep 2-13

    return mfcc
