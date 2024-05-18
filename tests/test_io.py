import unittest
from audio_analysis.io import read_audio, write_audio

class TestAudioIO(unittest.TestCase):

    def test_read_audio(self):
        # Test reading a valid WAV file
        audio_data, sample_rate = read_audio('tests/samples/sample.wav')
        self.assertIsNotNone(audio_data)
        self.assertEqual(sample_rate, 44100)

        # Test reading a non-existent file
        with self.assertRaises(FileNotFoundError):
            read_audio('tests/samples/non_existent.wav')

        # Test reading a file with an unsupported format
        with self.assertRaises(ValueError):
            read_audio('tests/samples/unsupported_format.mp3')

if __name__ == '__main__':
    unittest.main()
