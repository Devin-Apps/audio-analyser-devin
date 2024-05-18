import numpy as np
from scipy.signal import resample

def change_pitch(audio_data, sample_rate, semitone_shift):
    """
    Change the pitch of an audio signal by a number of semitones.

    Parameters:
    audio_data (numpy.ndarray): The audio signal to process.
    sample_rate (int): The sample rate of the audio signal.
    semitone_shift (float): The number of semitones to shift the pitch.

    Returns:
    numpy.ndarray: The pitch-shifted audio signal.
    """
    # Calculate the pitch shift factor
    pitch_shift_factor = 2 ** (semitone_shift / 12.0)

    # Resample the audio data to change the pitch
    resampled_audio = resample(audio_data, int(len(audio_data) / pitch_shift_factor))

    return resampled_audio

def time_stretch(audio_data, stretch_factor):
    """
    Stretch the time of an audio signal without changing its pitch.

    Parameters:
    audio_data (numpy.ndarray): The audio signal to process.
    stretch_factor (float): The factor by which to stretch the audio signal.

    Returns:
    numpy.ndarray: The time-stretched audio signal.
    """
    # Resample the audio data to stretch the time
    stretched_audio = resample(audio_data, int(len(audio_data) * stretch_factor))

    return stretched_audio
