from setuptools import setup, find_packages

setup(
    name='EDEN-lyrics-bot',
    version='1.2.0',
    description='Lyrics Generation Bot',
    author='Navkar Nahta',
    author_email='navkar.nahta@gmail.com',
    packages=find_packages(exclude=['tests', '.cache', '.venv', '.git', 'dist']),
    install_requires=[
        'tweepy',
        'numpy',
        'lyricsgenius'
        ]
)
