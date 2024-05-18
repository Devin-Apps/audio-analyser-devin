import wave

def read_audio(file_path):
    """
    Reads a WAV audio file and returns the audio data and sample rate.

    Parameters:
    file_path (str): The path to the WAV audio file.

    Returns:
    tuple: A tuple containing the audio data as a bytes object and the sample rate as an int.
    """
    # Check if the file extension is '.wav'
    if not file_path.lower().endswith('.wav'):
        raise ValueError("Unsupported file format: Only WAV files are supported.")

    with wave.open(file_path, 'rb') as wav_file:
        sample_rate = wav_file.getframerate()
        audio_data = wav_file.readframes(wav_file.getnframes())
    return audio_data, sample_rate

def write_audio(audio_data, sample_rate, file_path):
    """
    Writes audio data to a WAV audio file at the specified file path.

    Parameters:
    audio_data (bytes): The audio data to write to the file.
    sample_rate (int): The sample rate of the audio data.
    file_path (str): The path to the WAV audio file to write.
    """
    with wave.open(file_path, 'wb') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_data)
