import unittest
import numpy as np
import os
from audio_analysis.io import write_audio, read_audio

class TestWriteAudio(unittest.TestCase):

    def test_write_audio(self):
        # Create a sample audio data
        sample_rate = 44100
        duration = 1  # seconds
        frequency = 440  # Hz
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        audio_data = np.sin(2 * np.pi * frequency * t) * 32767
        audio_data = audio_data.astype(np.int16)

        # Write the audio data to a WAV file
        file_path = 'tests/samples/test_output.wav'
        write_audio(audio_data, sample_rate, file_path)

        # Check if the file was created
        self.assertTrue(os.path.exists(file_path))

        # Read the written audio file and verify its content
        read_data, read_rate = read_audio(file_path)
        self.assertTrue(np.array_equal(audio_data, read_data))
        self.assertEqual(sample_rate, read_rate)

        # Clean up the created file
        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
