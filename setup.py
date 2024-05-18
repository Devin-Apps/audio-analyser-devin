from setuptools import setup, find_packages

setup(
    name='audio_analysis_lib',
    version='0.1.0',
    author='Devin',
    author_email='devin@example.com',
    description='A Python library for audio analysis, similar to librosa.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/user/audio_analysis_lib',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.15.0',
        'scipy>=1.0.0',
        'librosa', # We can remove this if we're not using librosa as a dependency
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
