from distutils.core import setup
from pypandoc import convert

long_description = convert('README.md', 'rst')

setup(
    name = 'visualcaptcha',
    packages = ['visualcaptcha'],
    version = '0.0.1',
    description = 'visualCaptcha backend package for python',
    long_description = long_description,
    author = 'Bruno Bernardino',
    author_email = 'me@brunobernardino.com',
    url = 'https://github.com/emotionLoop/visualCaptcha-python',
    download_url = 'https://github.com/emotionLoop/visualCaptcha-python/tarball/0.0.1',
    keywords = ['captcha', 'visualcaptcha', 'security'],
    classifiers = [],
)