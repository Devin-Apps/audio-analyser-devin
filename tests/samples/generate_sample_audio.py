import wave
import numpy as np

# Parameters for the sine wave
sample_rate = 44100  # Sample rate in Hz
duration = 1         # Duration in seconds
frequency = 440      # Frequency of the sine wave in Hz

# Generate the sine wave
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
audio_data = np.sin(2 * np.pi * frequency * t) * 32767
audio_data = audio_data.astype(np.int16)  # Convert to 16-bit data

# Write the sine wave to a WAV file
with wave.open('sample.wav', 'wb') as wav_file:
    wav_file.setnchannels(1)  # Mono
    wav_file.setsampwidth(2)  # 16-bit
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(audio_data.tobytes())
