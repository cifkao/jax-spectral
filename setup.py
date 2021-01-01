import setuptools
# To use a consistent encoding
from codecs import open
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='jax-spectral',
    version='0.0.1',
    description='scipy.signal.spectral for JAX',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        'jax>=0.2.6'
    ],
)
